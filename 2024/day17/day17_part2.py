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
initB = B
initC = C

def starts_with(array, prefix):
    return array[:len(prefix)] == prefix

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

A = z3.BitVec('A', 64)
constraints = []
# for initA in range(1, 2):
try:
    outputs = []
    ip = 0
    # A = initA
    B = initB
    C = initC
    i = 0
    while ip < program_len - 1:  # Need 2 values to read
        i += 1
        # if i > 10**6:
        #     print(f'Too many loops!')
        #     break
        opcode = program[ip]
        operand = program[ip + 1]
        if opcode == adv:
            # division stored to A
            combo_op = get_combo_operand(operand)
            numerator = A
            # denominator = 2**combo_op
            # denominator = 1 << combo_op
            # result = numerator // denominator
            result = numerator >> combo_op
            A = result
        elif opcode == bxl:
            # bitwise XOR
            result = B ^ operand
            B = result
        elif opcode == bst:
            # store combo operand to B
            combo_op = get_combo_operand(operand)
            # result = combo_op % 8
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
            # result = combo_op % 8
            result = combo_op & 0x07
            constraints.append(result == program[len(outputs)])
            outputs.append(result)
            # constraints.append(program[:len(outputs)] == outputs)
            # array[:len(prefix)] == prefix
            # if not starts_with(program, outputs):
            #     print(f'outputs: {outputs}; program: {program}')
            #     raise Exception('Non-matching output.')
        elif opcode == bdv:
            # division stored to B
            combo_op = get_combo_operand(operand)
            numerator = A
            # denominator = 2**combo_op
            # denominator = 1 << combo_op
            # result = numerator // denominator
            result = numerator >> combo_op
            B = result
        elif opcode == cdv:
            # division stored to C
            combo_op = get_combo_operand(operand)
            numerator = A
            # denominator = 2**combo_op
            # denominator = 1 << combo_op
            # result = numerator // denominator
            result = numerator >> combo_op
            C = result
        else:
            raise Exception(f"Unexpected opcode: {opcode}")
        ip += 2
except Exception as e:
    print(f'Swallowing exception: {e}.')
if outputs == program:
    print(f'FOUND IT!!')
            

# print(f"A, B, C: ({A}, {B}, {C})")
# print(outputs)
# print(",".join(str(x) for x in outputs))

# x = Int('x')
# y = Int('y')
# solve(x > 2, y < 10, x + 2*y == 7)

# x = Real('x')
# y = Real('y')
# solve(x**2 + y**2 > 3, x**3 + y < 5)

constraints.append(A == 0)
z3.solve(*constraints)

# 1557573509065258 is too high
#  488848206866991 is too high
