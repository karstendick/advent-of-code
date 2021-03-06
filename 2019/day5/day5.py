from copy import deepcopy

def parse_instruction(instruction):
    opcode = instruction % 100
    param1_mode = (instruction // 100) % 10
    param2_mode = (instruction // 1000) % 10
    param3_mode = (instruction // 10000) % 10
    return opcode, param1_mode, param2_mode, param3_mode

def get_param(param_num, mode, program, p):
    if mode == 0:
        param = program[program[p+param_num]]
    elif mode == 1:
        param = program[p+param_num]
    else:
        raise ValueError(f'Invalid parameter mode: {param1_mode}. Expected one of: 0,1.')
    return param

# import pdb; pdb.set_trace();

filename = 'input.txt'
#filename = 'example.txt'
# filename = 'echo-example.txt'
# filename = 'multiply-example.txt'
with open(filename, 'r') as f:
    input = f.read().rstrip('\n')

program_input = [int(i) for i in input.split(',')]

program = deepcopy(program_input)
p = 0
input = 1
output = None
while True:
    instruction = program[p]
    opcode, param1_mode, param2_mode, param3_mode = parse_instruction(instruction)
    print(f'instruction: {instruction}:{opcode}, {param1_mode}, {param2_mode}, {param3_mode}')

    if opcode == 99:
        break
    elif opcode == 1:
        param1 = get_param(1, param1_mode, program, p)
        param2 = get_param(2, param2_mode, program, p)
        sum = param1 + param2
        output_pos = program[p+3]
        program[output_pos] = sum
        p += 4
    elif opcode == 2:
        param1 = get_param(1, param1_mode, program, p)
        param2 = get_param(2, param2_mode, program, p)
        product = param1 * param2
        output_pos = program[p+3]
        program[output_pos] = product
        p += 4
    elif opcode == 3:
        param1 = get_param(1, param1_mode, program, p)
        output_pos = program[p+1]
        program[output_pos] = input
        p += 2
    elif opcode == 4:
        param1 = get_param(1, param1_mode, program, p)
        output = param1
        print(f'output: {output}')
        p += 2
    else:
        raise ValueError(f'Invalid opcode: {opcode}. Expected one of: 1,2,99.')
    # print(f'program: {program}')

print(f'input: {input}; output: {output}')

# print(f'program[0]: {program[0]}\nprogram: {program}')
