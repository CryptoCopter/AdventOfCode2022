#!/usr/bin/env python3

import sys


def load_input(path: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    sections: list[tuple[tuple[int, int], tuple[int, int]]] = []

    with open(path, "r") as f:
        for line in f:
            left, right = line.strip().split(",")
            l_start, l_stop = left.split("-")
            r_start, r_stop = right.split("-")
            sections.append(((int(l_start), int(l_stop)), (int(r_start), int(r_stop))))

    return sections


def overlap(sections: list[tuple[tuple[int, int], tuple[int, int]]]) -> tuple[int, int]:
    total = 0
    partial = 0

    for (l_start, l_stop), (r_start, r_stop) in sections:
        if (l_start <= r_start and l_stop >= r_stop) or (
            l_start >= r_start and l_stop <= r_stop
        ):
            total += 1
            partial += 1
            continue
        if (
            l_start <= r_start <= l_stop
            or l_start <= r_stop <= l_stop
            or r_start <= l_start <= r_stop
            or r_start <= l_stop <= r_stop
        ):
            partial += 1

    return total, partial


if __name__ == "__main__":
    sections = load_input(sys.argv[1])
    part_1, part_2 = overlap(sections)
    print(part_1)
    print(part_2)
