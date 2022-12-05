import re

from aoc22_util.input import *

INSTRUCTION_PATTERN = re.compile("^move (\d+) from (\d+) to (\d+)")

def parse_instruction(line):
    match = re.match(INSTRUCTION_PATTERN, line)
    g = match.groups()
    return int(g[0]), int(g[1]) - 1, int(g[2]) - 1


lines = iter(file_readlines_no_newlines("05/input.txt"))

stacks = None

while True:
    line = next(lines)
    top_crates = line[1::4]

    if not stacks:
        stacks = [[] for _ in range(len(top_crates))]

    if any(char.isdigit() for char in top_crates):
        break

    for i, crate in enumerate(top_crates):
        if crate != " ":
            stacks[i].append(crate)

for stack in stacks:
    stack.reverse()
    print(stack)

next(lines)

for line in lines:
    count, origin, targer = parse_instruction(line)

    print(count, origin, targer)
    crates = stacks[origin][-count:]
    for i in range(count):
        stacks[origin].pop()
    stacks[targer].extend(crates)

for stack in stacks:
    print(stack[-1], end="")
