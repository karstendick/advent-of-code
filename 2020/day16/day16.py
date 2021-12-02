with open('input.txt', 'r') as f:
    sections = f.read().split('\n\n')

# print(sections)

field_lines = sections[0].split('\n')

nearby_ticket_lines = sections[2].split('\n')[1:]

# print(field_lines)
# print(nearby_ticket_lines)

valid_values = [False for _ in range(1000)]
for field_line in field_lines:
    words = field_line.split()
    lower, upper = map(int, words[-3].split('-'))
    # L[2:4] = ["foo"] * (4-2)
    valid_values[lower:upper + 1] = [True] * (upper + 1 - lower)
    lower, upper = map(int, words[-1].split('-'))
    valid_values[lower:upper + 1] = [True] * (upper + 1 - lower)

# print(valid_values)

error_rate = 0
for nearby_ticket_line in nearby_ticket_lines:
    # print(f"nearby_ticket_line: {nearby_ticket_line}")
    if not nearby_ticket_line:
        continue
    values = list(map(int, nearby_ticket_line.split(',')))
    # print(values)
    for value in values:
        if not valid_values[value]:
            error_rate += value

print(error_rate)
