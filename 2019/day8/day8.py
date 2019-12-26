filename = 'input.txt'
# filename = 'example.txt'
with open(filename, 'r') as f:
    input = f.read().rstrip('\n')
input = [int(i) for i in input]

width = 25
height = 6

# width = 3
# height = 2

N = len(input)
num_layers = N//(width*height)

print(f'num_layers: {num_layers}')

n = width*height
layers = []
for i in range(num_layers):
    layers.append(input[i*n:(i+1)*n])

print(f'layers: {layers}')
# import pdb; pdb.set_trace();
zero_counts = [len(list(filter(lambda x: x==0, layer))) for layer in layers]
print(f'zero_counts: {zero_counts}')


fewest_zeros_count = min(zero_counts)

fewest_zeros_index = None
for i, zero_count in enumerate(zero_counts):
    if zero_count == fewest_zeros_count:
        fewest_zeros_index = i
        break

fewest_zeros_layer = layers[fewest_zeros_index]
print(f'fewest_zeros_layer: {fewest_zeros_layer}')
num_ones = fewest_zeros_layer.count(1)
num_twos = fewest_zeros_layer.count(2)
print(f'product: {num_ones*num_twos}')
