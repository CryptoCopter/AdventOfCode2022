#!/usr/bin/env python3

import sys
from typing import TextIO
from copy import deepcopy


def parse_stacks(f: TextIO) -> list[list[str]]:
    tmp = ""
    n = 0
    for line in f:
        if "1" in line:
            n = int(line.strip().split(" ")[-1])
            break
        else:
            tmp += line

    stacks: list[list[str]] = [[] for _ in range(n)]

    for line in tmp.split("\n"):
        i = 0
        while i * 4 < len(line):
            crate = line[i * 4 : (i * 4) + 3]
            if crate != "   ":
                stacks[i].append(crate[1])
            i += 1

    return [stack[::-1] for stack in stacks]


def parse_moves(f: TextIO) -> list[tuple[int, int, int]]:
    moves: list[tuple[int, int, int]] = []

    for line in f:
        if line == "\n":
            continue

        parts = line.strip().split(" ")
        moves.append((int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1))

    return moves


def load_input(path: str) -> tuple[list[list[str]], list[tuple[int, int, int]]]:
    with open(path, "r") as f:
        stacks = parse_stacks(f)
        moves = parse_moves(f)

    return stacks, moves


def do_moves(
    stacks: list[list[str]], moves: list[tuple[int, int, int]]
) -> tuple[str, str]:
    cargo_update = deepcopy(stacks)

    for n, from_stack, to_stack in moves:
        stacks[to_stack] += stacks[from_stack][: -(n + 1) : -1]
        stacks[from_stack] = stacks[from_stack][:-n]

        cargo_update[to_stack] += cargo_update[from_stack][-n:]
        cargo_update[from_stack] = cargo_update[from_stack][:-n]

    return "".join([stack[-1] for stack in stacks]), "".join(
        [stack[-1] for stack in cargo_update]
    )


if __name__ == "__main__":
    stacks, moves = load_input(sys.argv[1])
    part_1, part_2 = do_moves(stacks, moves)
    print(part_1)
    print(part_2)
