#!/usr/bin/env python3

import sys


def parse_symbol(symbol: str) -> int:
    if symbol == "A" or symbol == "X":
        return 0
    if symbol == "B" or symbol == "Y":
        return 1
    if symbol == "C" or symbol == "Z":
        return 2


def parse_symbol_part_2(opponent: int, result: str) -> int:
    if result == "X":
        return (opponent - 1) % 3
    elif result == "Y":
        return opponent
    elif result == "Z":
        return (opponent + 1) % 3


def load_input(path: str) -> list[tuple[str, str]]:
    strategy: list[tuple[str, str]] = []
    with open(path, "r") as f:
        for line in f:
            opponent, me = line.strip().split(" ")
            strategy.append((opponent, me))
    return strategy


def round_points(opponent: int, me: int) -> int:
    points = 0

    points += me + 1
    outcome = me - opponent
    if outcome == 0:
        points += 3
    elif (outcome > 0 and outcome != 2) or outcome == -2:
        points += 6

    return points


def part_1(strategy: list[tuple[str, str]]) -> int:
    total = 0

    for opponent, me in strategy:
        opponent = parse_symbol(opponent)
        me = parse_symbol(me)
        total += round_points(opponent, me)

    return total


def part_2(strategy: list[tuple[str, str]]) -> int:
    total = 0

    for opponent, me in strategy:
        opponent = parse_symbol(opponent)
        me = parse_symbol_part_2(opponent, me)
        total += round_points(opponent, me)

    return total


if __name__ == "__main__":
    strategy = load_input(sys.argv[1])
    print(part_1(strategy))
    print(part_2(strategy))
