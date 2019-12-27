filename = 'input.txt'
# filename = 'example-part2.txt'
with open(filename, 'r') as f:
    input = f.read().rstrip('\n')
input = [int(i) for i in input]

width = 25
height = 6

# width = 2
# height = 2

N = len(input)
num_layers = N//(width*height)

print(f'num_layers: {num_layers}')

n = width*height
layers = []
for i in range(num_layers):
    layers.append(input[i*n:(i+1)*n])

print(f'layers: {layers}')

# output = [ [-1]*n for i in range(num_layers)]
# output = [x[:] for x in [[-1] * n] * num_layers]
output = [-1]*n
# import pdb; pdb.set_trace();
print(f'layers: {layers}')
print(f'output: {output}')
for i in range(n):
    for layer in layers:
        if layer[i] == 0:
            print(f'outputting 0 at index {i}')
            output[i] = 0
            break
        elif layer[i] == 1:
            print(f'outputting 1 at index {i}')
            output[i] = 1
            break

print(output)

def print_output(output, width, height):
    i = 0
    for row in range(height):
        for col in range(width):
            if output[i] == 0:
                print('.', end='')
            elif output[i] == 1:
                print('X', end='')
            i += 1
        print(' ')

print_output(output, width, height)
