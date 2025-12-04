inp = []
with open("input.txt", "r") as f:
    for line in f:
        inp.append([int(c) for c in line.strip()])

# print(inp)

N = 12
total_joltage = 0

for bank in inp:
    digits = [0] * N
    for i in range(len(bank) - N):
        battery = bank[i]
        for j in range(N):
            if battery > digits[j]:
                digits[j] = battery
                for k in range(j + 1, N):
                    digits[k] = 0
                break

    # handle last N batteries in the bank
    for j in range(N):
        battery = bank[len(bank) - N + j]
        for k in range(N - j):
            if battery > digits[j + k]:
                digits[j + k] = battery
                for l in range(j + k + 1, N):
                    digits[l] = 0
                break

    max_joltage = 0
    for j in range(N):
        max_joltage += digits[j] * 10 ** (N - j - 1)
    total_joltage += max_joltage
    # print(f'max_joltage: {max_joltage}')

print(total_joltage)
# 171010026613719 is too high

