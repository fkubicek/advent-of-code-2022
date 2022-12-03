from enum import Enum

SCORE_DRAW = 3
SCORE_VICTORY = 6


class Hand(Enum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2


def hand_value(hand):
    return hand.value + 1


def how_to_beat(other_hand):
    return Hand((other_hand.value + 1) % 3)


def how_to_lose(other_hand):
    return Hand((other_hand.value - 1) % 3)


def symbol_to_hand(symbol):
    match symbol:
        case "A" | "X": return Hand.ROCK
        case "B" | "Y": return Hand.PAPER
        case "C" | "Z": return Hand.SCISSOR


file = open("02/input.txt", "r")

score = 0

for line in file.readlines():
    opponent, outcome = line.split()
    opponent = symbol_to_hand(opponent)

    match outcome:
        case "X":
            # I need to lose
            me = how_to_lose(opponent)
            score += hand_value(me)
        case "Y":
            # we need to draw
            me = opponent
            score += SCORE_DRAW + hand_value(me)
        case "Z":
            # I need to win
            me = how_to_beat(opponent)
            score += SCORE_VICTORY + hand_value(me)


print(score)
