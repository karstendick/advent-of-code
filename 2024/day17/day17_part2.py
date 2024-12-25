import z3

program = []
with open("input.txt", "r") as f:
    for line in f:
        if line.startswith("Register A:"):
            A = int(line.split()[2])
        elif line.startswith("Register B:"):
            B = int(line.split()[2])
        elif line.startswith("Register C:"):
            C = int(line.split()[2])
        elif line.startswith("Program:"):
            program = [int(x) for x in line.split()[1].split(",")]

print(f"A, B, C: ({A}, {B}, {C})")
print(program)


def starts_with(array, prefix):
    return array[: len(prefix)] == prefix


def get_combo_operand(op):
    if op == 4:
        return A
    elif op == 5:
        return B
    elif op == 6:
        return C
    elif op == 7:
        raise Exception(
            "Combo operand 7 is reserved and will not appear in valid programs"
        )
    elif op < 0 or op > 7:
        raise Exception(f"Unexpected combo operand: {op}")
    else:  # Literal values 0..3
        return op


adv, bxl, bst, jnz, bxc, out, bdv, cdv = range(8)
program_len = len(program)

A = z3.BitVec("A", 64)
constraints = []
constraints.append(A > 0)
constraints.append(A < 202975183645229)
# constraints.append(A < 202975183645226)
try:
    outputs = []
    outputs_len = 0
    ip = 0
    while ip < program_len - 1 and outputs_len < len(program):  # Need 2 values to read
        opcode = program[ip]
        operand = program[ip + 1]
        if opcode == adv:
            # division stored to A
            combo_op = get_combo_operand(operand)
            numerator = A
            result = numerator >> combo_op
            A = result
        elif opcode == bxl:
            # bitwise XOR
            result = B ^ operand
            B = result
        elif opcode == bst:
            # store combo operand to B
            combo_op = get_combo_operand(operand)
            result = combo_op & 0x07
            B = result
        elif opcode == jnz:
            # jump if not zero
            constraints.append(A != 0)
            ip = operand
            continue
        elif opcode == bxc:
            # bitwise XOR of B and C
            result = B ^ C
            B = result
        elif opcode == out:
            # output
            combo_op = get_combo_operand(operand)
            result = combo_op & 0x07
            constraints.append(result == program[len(outputs)])
            outputs.append(result)
            outputs_len += 1
        elif opcode == bdv:
            # division stored to B
            combo_op = get_combo_operand(operand)
            numerator = A
            result = numerator >> combo_op
            B = result
        elif opcode == cdv:
            # division stored to C
            combo_op = get_combo_operand(operand)
            numerator = A
            result = numerator >> combo_op
            C = result
        else:
            raise Exception(f"Unexpected opcode: {opcode}")
        ip += 2
except Exception as e:
    print(f"Swallowing exception: {e}.")

constraints.append(A == 0)
solver = z3.Solver()
solver.add(*constraints)
if solver.check() == z3.sat:
    result = solver.model().evaluate(A)
    print(result)
    print(solver.model())
    solver.add(A < result)
