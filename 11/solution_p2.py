import math

class Monkey:

    monkeys = []

    def __init__(
        self,
        starting_items,
        operation,
        divide_by,
        target_true,
        target_false
        ) -> None:

        self.items = starting_items
        self.operation = operation
        self.divide_by = divide_by
        self.target_true = target_true
        self.target_false = target_false

        self.inspected_item_count = 0

        Monkey.monkeys.append(self)
    
    def turn(self):
        for worry_level in self.items:
            self.inspected_item_count += 1
            worry_level = self.operation(worry_level)
            worry_level = worry_level % Monkey.lcm
            if worry_level % self.divide_by == 0:
                Monkey.monkeys[self.target_true].items.append(worry_level)
            else:
                Monkey.monkeys[self.target_false].items.append(worry_level)
        self.items = []

def prepare_monkeys_sample():
    Monkey(
        [79, 98],
        lambda old: old * 19,
        23,
        2,
        3
    )

    Monkey(
        [54, 65, 75, 74],
        lambda old: old + 6,
        19,
        2,
        0
    )

    Monkey(
        [79, 60, 97],
        lambda old: old * old,
        13,
        1,
        3
    )

    Monkey(
        [74],
        lambda old: old + 3,
        17,
        0,
        1
    )

def prepare_monkeys_input():
    Monkey(
        [83, 62, 93],
        lambda old: old * 17,
        2,
        1,
        6
    )

    Monkey(
        [90, 55],
        lambda old: old + 1,
        17,
        6,
        3
    )

    Monkey(
        [91, 78, 80, 97, 79, 88],
        lambda old: old + 3,
        19,
        7,
        5
    )

    Monkey(
        [64, 80, 83, 89, 59],
        lambda old: old + 5,
        3,
        7,
        2
    )

    Monkey(
        [98, 92, 99, 51],
        lambda old: old * old,
        5,
        0,
        1
    )

    Monkey(
        [68, 57, 95, 85, 98, 75, 98, 75],
        lambda old: old + 2,
        13,
        4,
        0
    )

    Monkey(
        [74],
        lambda old: old + 4,
        7,
        3,
        2
    )

    Monkey(
        [68, 64, 60, 68, 87, 80, 82],
        lambda old: old * 19,
        11,
        4,
        5
    )


if __name__ == "__main__":

    # prepare_monkeys_sample()
    prepare_monkeys_input()

    Monkey.lcm = math.lcm(*map(lambda monkey: monkey.divide_by, Monkey.monkeys))

    rounds = 10000
    for _ in range(rounds):
        for monkey in Monkey.monkeys:
            monkey.turn()

    counts = list(map(lambda monkey: monkey.inspected_item_count, Monkey.monkeys))
    counts.sort()
    print(counts, counts[-1] * counts[-2])
