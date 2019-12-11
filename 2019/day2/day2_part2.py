from copy import deepcopy

filename = 'input.txt'
#filename = 'example.txt'
with open(filename, 'r') as f:
    input = f.read().rstrip('\n')

program_input = [int(i) for i in input.split(',')]
# p = 0 # index of current position

# initalization
# program[1] = 12
# program[2] = 2

for noun in range(1,100):
    for verb in range(1,100):
        program = deepcopy(program_input)
        p = 0
        program[1] = noun
        program[2] = verb
        while True:
            opcode = program[p]
            # print(f'p, opcode: {p},{opcode}')
            if opcode == 99:
                break
            elif opcode == 1:
                sum = program[program[p+1]] + program[program[p+2]]
                output_pos = program[p+3]
                program[output_pos] = sum
            elif opcode == 2:
                product = program[program[p+1]] * program[program[p+2]]
                output_pos = program[p+3]
                program[output_pos] = product
            else:
                raise ValueError(f'Invalid opcode: {opcode}. Expected one of: 1,2,99.')
            # print(f'program: {program}')
            p += 4
        output = program[0]
        if output == 19690720:
            print (f'Found it! noun,verb: {noun},{verb}')
        # print(f'noun,verb,output: {noun},{verb},{output}')

# print(f'program[0]: {program[0]}\nprogram: {program}')
