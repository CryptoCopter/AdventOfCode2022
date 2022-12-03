#!/usr/bin/env python3

import sys


def item_priority(item: str) -> int:
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38


def load_input(path: str) -> list[tuple[str, str]]:
    rucksäcke: list[tuple[str, str]] = []

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            length = int(len(line) / 2)
            left = line[:length]
            right = line[length:]

            rucksäcke.append((left, right))

    return rucksäcke


def duplicates(rucksäcke: list[tuple[str, str]]) -> int:
    total = 0

    for left, right in rucksäcke:
        both = set(left) & set(right)
        for item in both:
            total += item_priority(item)

    return total


def badgesbadgesbadgesbadgesbadgesbadgesbadgesbadgesbadges_mushroom_mushroom(
    rucksäcke: list[tuple[str, str]]
) -> int:
    total = 0
    i = 0

    while i < len(rucksäcke):
        badge = (
            set(rucksäcke[i][0] + rucksäcke[i][1])
            & set(rucksäcke[i + 1][0] + rucksäcke[i + 1][1])
            & set(rucksäcke[i + 2][0] + rucksäcke[i + 2][1])
        )
        for item in badge:
            total += item_priority(item)
        i += 3

    return total


if __name__ == "__main__":
    rucksäcke = load_input(sys.argv[1])
    print(duplicates(rucksäcke))
    print(
        badgesbadgesbadgesbadgesbadgesbadgesbadgesbadgesbadges_mushroom_mushroom(
            rucksäcke
        )
    )
