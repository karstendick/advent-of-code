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
outputs = []
ip = 0
while ip < program_len - 1:  # Need 2 values to read
    opcode = program[ip]
    operand = program[ip + 1]
    if opcode == adv:
        # division stored to A
        combo_op = get_combo_operand(operand)
        numerator = A
        denominator = 2**combo_op
        result = numerator // denominator
        A = result
    elif opcode == bxl:
        # bitwise XOR
        result = B ^ operand
        B = result
    elif opcode == bst:
        # store combo operand to B
        combo_op = get_combo_operand(operand)
        result = combo_op % 8
        B = result
    elif opcode == jnz:
        # jump if not zero
        if A != 0:
            ip = operand
            continue
    elif opcode == bxc:
        # bitwise XOR of B and C
        result = B ^ C
        B = result
    elif opcode == out:
        # output
        combo_op = get_combo_operand(operand)
        result = combo_op % 8
        outputs.append(result)
    elif opcode == bdv:
        # division stored to B
        combo_op = get_combo_operand(operand)
        numerator = A
        denominator = 2**combo_op
        result = numerator // denominator
        B = result
    elif opcode == cdv:
        # division stored to C
        combo_op = get_combo_operand(operand)
        numerator = A
        denominator = 2**combo_op
        result = numerator // denominator
        C = result
    else:
        raise Exception(f"Unexpected opcode: {opcode}")
    ip += 2

print(f"A, B, C: ({A}, {B}, {C})")
print(outputs)
print(",".join(str(x) for x in outputs))
