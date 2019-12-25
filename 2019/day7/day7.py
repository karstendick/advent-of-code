from copy import deepcopy
from itertools import permutations

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
# filename = 'example1.txt'
#filename = 'example2.txt'
#filename = 'example3.txt'
with open(filename, 'r') as f:
    input = f.read().rstrip('\n')

program_input = [int(i) for i in input.split(',')]

def run_program(input1, input2):
    program = deepcopy(program_input)
    print(f'program: {program}')
    p = 0
    input1_read = False
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
            if input1_read:
                program[output_pos] = input2
            else:
                program[output_pos] = input1
                input1_read = True
            p += 2
        elif opcode == 4:
            param1 = get_param(1, param1_mode, program, p)
            output = param1
            print(f'output: {output}')
            p += 2
        elif opcode == 5:
            param1 = get_param(1, param1_mode, program, p)
            param2 = get_param(2, param2_mode, program, p)
            if param1 != 0:
                p = param2
            else:
                p += 3
        elif opcode == 6:
            param1 = get_param(1, param1_mode, program, p)
            param2 = get_param(2, param2_mode, program, p)
            if param1 == 0:
                p = param2
            else:
                p += 3
        elif opcode == 7:
            param1 = get_param(1, param1_mode, program, p)
            param2 = get_param(2, param2_mode, program, p)
            output_pos = program[p+3]
            if param1 < param2:
                program[output_pos] = 1
            else:
                program[output_pos] = 0
            p += 4
        elif opcode == 8:
            param1 = get_param(1, param1_mode, program, p)
            param2 = get_param(2, param2_mode, program, p)
            output_pos = program[p+3]
            if param1 == param2:
                program[output_pos] = 1
            else:
                program[output_pos] = 0
            p += 4
        else:
            raise ValueError(f'Invalid opcode: {opcode}. Expected one of: 1,2,3,4,5,6,7,99.')
        # print(f'program: {program}')
    return output

def run_amplifiers(arr):
    output1 = run_program(arr[0],0)
    output2 = run_program(arr[1],output1)
    output3 = run_program(arr[2],output2)
    output4 = run_program(arr[3],output3)
    output5 = run_program(arr[4],output4)
    return output5

max_output = 0
for arr in permutations(range(5)):
    output = run_amplifiers(arr)
    if output > max_output:
        max_output = output

print(f'max_output: {max_output}')
