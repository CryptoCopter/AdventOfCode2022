#!/usr/bin/env python3

import sys


def load_input(path: str) -> list[tuple[int, int]]:
    moves: list[tuple[int, int]] = []

    with open(path, "r") as f:
        for line in f:
            direction, distance = line.strip().split(" ")
            if direction == "U":
                steps = [(0, 1)] * int(distance)
                moves += steps
            elif direction == "D":
                steps = [(0, -1)] * int(distance)
                moves += steps
            elif direction == "R":
                steps = [(1, 0)] * int(distance)
                moves += steps
            else:
                steps = [(-1, 0)] * int(distance)
                moves += steps

    return moves


def do_moves(moves: list[tuple[int, int]]) -> (int, int):
    head = (0, 0)
    tails = [(0, 0)] * 9
    first_visited: set[tuple[int, int]] = set()
    first_visited.add((0, 0))
    last_visited: set[tuple[int, int]] = set()
    last_visited.add((0, 0))

    for move in moves:
        # I thought Python would just let me add tuples... I was wrong
        head = (head[0] + move[0], head[1] + move[1])
        leader = head
        for i in range(len(tails)):
            tail = tails[i]
            x_diff = leader[0] - tail[0]
            y_diff = leader[1] - tail[1]

            if abs(x_diff) == 2 and abs(y_diff) == 2:
                tail = (tail[0] + int(x_diff / 2), tail[1] + int(y_diff / 2))
            elif abs(x_diff) == 2:
                tail = (tail[0] + int(x_diff / 2), tail[1] + y_diff)
            elif abs(y_diff) == 2:
                tail = (tail[0] + x_diff, tail[1] + int(y_diff / 2))

            leader = tail
            tails[i] = tail
        first_visited.add(tails[0])
        last_visited.add(tails[-1])

    return len(first_visited), len(last_visited)


if __name__ == "__main__":
    moves = load_input(sys.argv[1])
    part_1, part_2 = do_moves(moves)
    print(part_1)
    print(part_2)
