import re

from aoc22_util.input import *

LINE_PATTERN = re.compile("^(\d+)-(\d+),(\d+)-(\d+)")

def parse_pair(line):
    match = re.match(LINE_PATTERN, line)
    groups = list(map(int, match.groups()))
    return groups[:2], groups[2:]

def interval_inclusion(outer, inner):
    return (
        (inner[0] >= outer[0]) and
        (inner[1] <= outer[1])
    )

def interval_overlap(int_1, int_2):
    return not (int_1[1] < int_2[0] or int_1[0] > int_2[1])

if __name__ == "__main__":

    total_p1 = 0
    total_p2 = 0

    for line in file_readlines_stripped("04/input.txt"):
        int_1, int_2 = parse_pair(line)

        print(int_1, int_2)

        if interval_inclusion(int_1, int_2) or interval_inclusion(int_2, int_1):
            total_p1 += 1
        
        if interval_overlap(int_1, int_2):
            total_p2 += 1

    print(total_p1, total_p2)
