import ast
import functools

from aoc22_util.input import *

def is_in_order(left, right):  
    for l, r in zip(left, right):
        if type(l) == int and type(r) == int:
            if l < r:
                return True
            if l > r:
                return False
        else:
            if type(l) == int:
                l = [l]
            if type(r) == int:
                r = [r]
            
            res = is_in_order(l, r)
            if res is None:
                continue
            return res

    if len(left) == len(right):
        return None
    return len(left) < len(right)


def part_one():
    index = 1
    first_in_pair = None
    total = 0

    for line in file_readlines_stripped("13/sample.txt"):
        if line == "":
            index += 1
            first_in_pair = None
            continue
        
        if first_in_pair is None:
            first_in_pair = line
            continue

        if is_in_order(ast.literal_eval(first_in_pair), ast.literal_eval(line)):
            total += index
            print(index)

    print(total)

def part_two():
    packets = []
    for line in file_readlines_stripped("13/input.txt"):
        if line != "":
            packets.append(ast.literal_eval(line))
    divider_1 = [[2]]
    divider_2 = [[6]]
    packets.extend([divider_1, divider_2])

    packets.sort(key=functools.cmp_to_key(lambda l, r: -1 if is_in_order(l, r) else 1))

    for p in packets:
        print(p)

    print((packets.index(divider_1) + 1) * (packets.index(divider_2) + 1))


if __name__ == "__main__":
    # part_one()
    part_two()
