#!/usr/bin/env python3


def load_input(path: str) -> list[list[int]]:
    everyone: list[list[int]] = []

    just_a_little_guy: list[int] = []
    with open(path, "r") as f:
        for line in f:
            if line == "\n":
                everyone.append(just_a_little_guy)
                just_a_little_guy = []
                continue
            line = line.strip()
            just_a_little_guy.append(int(line))
    everyone.append(just_a_little_guy)

    return everyone


def find_hungriest_boi(everyone: list[list[int]]) -> tuple[int, int]:
    calories: list[int] = [sum(boi) for boi in everyone]
    calories.sort(reverse=True)
    return calories[0], sum(calories[:3])


if __name__ == "__main__":
    everyone = load_input("input.txt")
    part_1, part_2 = find_hungriest_boi(everyone)
    print(part_1)
    print(part_2)
