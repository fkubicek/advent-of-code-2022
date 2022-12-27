class Monkey:

    monkeys = []

    def __init__(
        self,
        starting_items,
        operation,
        test,
        target_true,
        target_false
        ) -> None:

        self.items = starting_items
        self.operation = operation
        self.test = test
        self.target_true = target_true
        self.target_false = target_false

        self.inspected_item_count = 0

        Monkey.monkeys.append(self)
    
    def turn(self):
        for worry_level in self.items:
            self.inspected_item_count += 1
            worry_level = self.operation(worry_level)
            worry_level = worry_level // 3
            if self.test(worry_level):
                Monkey.monkeys[self.target_true].items.append(worry_level)
            else:
                Monkey.monkeys[self.target_false].items.append(worry_level)
        self.items = []

def prepare_monkeys_sample():
    Monkey(
        [79, 98],
        lambda old: old * 19,
        lambda worry_level: worry_level % 23 == 0,
        2,
        3
    )

    Monkey(
        [54, 65, 75, 74],
        lambda old: old + 6,
        lambda worry_level: worry_level % 19 == 0,
        2,
        0
    )

    Monkey(
        [79, 60, 97],
        lambda old: old * old,
        lambda worry_level: worry_level % 13 == 0,
        1,
        3
    )

    Monkey(
        [74],
        lambda old: old + 3,
        lambda worry_level: worry_level % 17 == 0,
        0,
        1
    )

def prepare_monkeys_input():
    Monkey(
        [83, 62, 93],
        lambda old: old * 17,
        lambda worry_level: worry_level % 2 == 0,
        1,
        6
    )

    Monkey(
        [90, 55],
        lambda old: old + 1,
        lambda worry_level: worry_level % 17 == 0,
        6,
        3
    )

    Monkey(
        [91, 78, 80, 97, 79, 88],
        lambda old: old + 3,
        lambda worry_level: worry_level % 19 == 0,
        7,
        5
    )

    Monkey(
        [64, 80, 83, 89, 59],
        lambda old: old + 5,
        lambda worry_level: worry_level % 3 == 0,
        7,
        2
    )

    Monkey(
        [98, 92, 99, 51],
        lambda old: old * old,
        lambda worry_level: worry_level % 5 == 0,
        0,
        1
    )

    Monkey(
        [68, 57, 95, 85, 98, 75, 98, 75],
        lambda old: old + 2,
        lambda worry_level: worry_level % 13 == 0,
        4,
        0
    )

    Monkey(
        [74],
        lambda old: old + 4,
        lambda worry_level: worry_level % 7 == 0,
        3,
        2
    )

    Monkey(
        [68, 64, 60, 68, 87, 80, 82],
        lambda old: old * 19,
        lambda worry_level: worry_level % 11 == 0,
        4,
        5
    )


if __name__ == "__main__":

    # prepare_monkeys_sample()
    prepare_monkeys_input()

    rounds = 20
    for _ in range(rounds):
        for monkey in Monkey.monkeys:
            monkey.turn()

    counts = sorted(list(map(lambda monkey: monkey.inspected_item_count, Monkey.monkeys)))
    print(counts, counts[-1] * counts[-2])
