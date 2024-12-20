from collections import defaultdict

filepath = 'day1_input.txt'

n1_arr = []
n2_arr = []

with open(filepath) as fp:
    while True:
        line = fp.readline()

        if not line:
            break

        [n1, n2] = line.split("   ")

        n1_arr.append(int(n1))
        n2_arr.append(int(n2))

n1_arr.sort()
n2_arr.sort()

total_sum = 0

for n1, n2 in zip(n1_arr, n2_arr):
    total_sum += abs(n1 - n2)

print(total_sum)

## PART 2

n2_freq = defaultdict(int)

for n2 in n2_arr:
    n2_freq[n2] += 1

similarity_score = 0

for n1 in n1_arr:
    similarity_score += n1 * n2_freq[n1]

print(similarity_score)