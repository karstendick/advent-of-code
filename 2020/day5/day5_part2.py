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

# print(max(seat_ids)) # part 1 answer

seat_ids = sorted(seat_ids)
last_seat = None
for seat in seat_ids:
    if last_seat and seat - last_seat == 2:
        print(seat - 1)
        break
    last_seat = seat
