file = open("input.txt", "r")

sum_partial = 0
sums_aggregated = []

for line in file.readlines():
    line = line.strip()
    if line == "":
        sums_aggregated.append(sum_partial)
        sum_partial = 0
        continue
    sum_partial += int(line)

sums_aggregated.sort()

print(sums_aggregated)
print(sum(sums_aggregated[-3:]))
