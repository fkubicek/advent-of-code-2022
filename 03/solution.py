from aoc22_util.input import *


def item_to_value(item: str):
    if item.islower():
        return ord(item) - ord("a") + 1
    return ord(item) - ord("A") + 27


def items_str_to_set(items):
    return set([x for x in items])


def part_one():

    total = 0

    for line in file_readlines_stripped("03/input.txt"):
        half_index = len(line) // 2

        comp_1 = items_str_to_set(line[:half_index])
        comp_2 = items_str_to_set(line[half_index:])

        item = (comp_1 & comp_2).pop()
        total += item_to_value(item)

        # print(item, item_to_value(item))

    print(total)


def part_two():

    total = 0

    lines = list(file_readlines_stripped("03/input.txt"))
    group_size = 3

    for group in zip(*[lines[i::group_size] for i in range(group_size)]):

        group = list(map(items_str_to_set, group))

        item = group[0].intersection(*group[1:]).pop()
        total += item_to_value(item)

        # print(group, item, item_to_value(item))

    print(total)


if __name__ == "__main__":
    part_one()
    part_two()
