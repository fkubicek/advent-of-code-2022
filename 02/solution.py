from enum import Enum

SCORE_DRAW = 3
SCORE_VICTORY = 6


class Hand(Enum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2


def hand_value(hand):
    return hand.value + 1


def first_has_won(first, second):
    return (first.value - 1) % 3 == second.value


def get_my_score(opponent, me):
    if opponent == me:
        return SCORE_DRAW + hand_value(me)

    if first_has_won(opponent, me):
        return hand_value(me)

    return (SCORE_VICTORY + hand_value(me))


def symbol_to_hand(symbol):
    match symbol:
        case "A" | "X": return Hand.ROCK
        case "B" | "Y": return Hand.PAPER
        case "C" | "Z": return Hand.SCISSOR


file = open("02/input.txt", "r")

score = 0

for line in file.readlines():
    opponent, me = map(symbol_to_hand, line.split())

    print(opponent, me, get_my_score(opponent, me))
    score += get_my_score(opponent, me)

print(score)
