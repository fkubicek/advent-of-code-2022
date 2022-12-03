from aoc22_util.input import *

sum_partial = 0
sums_aggregated = []

for line in file_readlines_stripped("01/input.txt"):
    if line == "":
        sums_aggregated.append(sum_partial)
        sum_partial = 0
        continue
    sum_partial += int(line)

sums_aggregated.sort()

print(sums_aggregated)
print(sum(sums_aggregated[-3:]))
