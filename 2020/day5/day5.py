# example = 'FBFBBFFRLR'
example = 'BFFFBBFRRR'

passes = []
with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip()
      passes.append(line)

def pass_to_seat_id(bpass):

    bpass_bin = bpass\
        .replace('F', '0')\
        .replace('B','1')\
        .replace('L','0')\
        .replace('R','1')
    return int(bpass_bin, 2)
    

seat_ids = [pass_to_seat_id(bpass) for bpass in passes]

print(max(seat_ids))
