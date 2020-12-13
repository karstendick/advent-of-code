with open('input.txt', 'r') as f:
    earliest_timestamp = int(f.readline())
    bus_ids = [int(b) for b in f.readline().strip().split(',') if b != 'x']

print(earliest_timestamp)
print(bus_ids)

done = False
for ts in range(earliest_timestamp, 10**8):
    if done:
        break
    for bus_id in bus_ids:
        if ts % bus_id == 0:
            wait_time = ts - earliest_timestamp
            print(f"{wait_time * bus_id} | {ts} | {wait_time} | {bus_id}")
            done = True
            break
