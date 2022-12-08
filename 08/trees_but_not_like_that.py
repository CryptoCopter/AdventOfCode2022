#!/usr/bin/env python3

import sys


def load_input(path: str) -> list[list[int]]:
    trees: list[list[int]] = []

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            row: list[int] = []
            for digit in line:
                row.append(int(digit))
            trees.append(row)

    return trees


def part_1(trees: list[list[int]]) -> int:
    visibility: list[list[int]] = [[0] * len(trees[0]) for _ in range(len(trees))]

    # horizontal
    for y in range(0, len(trees)):
        visibility[y][0] = 1
        visibility[y][-1] = 1
        left_done = False
        right_done = False
        max_left = trees[y][0]
        max_right = trees[y][-1]
        for x in range(1, len(trees[0]) - 1):
            if max_left == 9:
                left_done = True
            if max_right == 9:
                right_done = True

            if left_done and right_done:
                break

            if not left_done:
                if trees[y][x] > max_left:
                    visibility[y][x] = 1
                    max_left = trees[y][x]

            if not right_done:
                if trees[y][-(x + 1)] > max_right:
                    visibility[y][-(x + 1)] = 1
                    max_right = trees[y][-(x + 1)]

    # vertical
    # you could also do this more elegantly with a function, but you would have to re-arrange the list
    # which would probably take wayyy longer
    for x in range(0, len(trees[0])):
        visibility[0][x] = 1
        visibility[-1][x] = 1
        top_done = False
        bottom_done = False
        max_top = trees[0][x]
        max_bottom = trees[-1][x]
        for y in range(1, len(trees) - 1):
            if max_top == 9:
                top_done = True
            if max_bottom == 9:
                bottom_done = True

            if top_done and bottom_done:
                break

            if not top_done:
                if trees[y][x] > max_top:
                    visibility[y][x] = 1
                    max_top = trees[y][x]

            if not bottom_done:
                if trees[-(y + 1)][x] > max_bottom:
                    visibility[-(y + 1)][x] = 1
                    max_bottom = trees[-(y + 1)][x]

    return sum([sum(row) for row in visibility])


def part_2(trees: list[list[int]]) -> int:
    best = 0
    forest_width = len(trees[0])
    forest_height = len(trees)
    for y in range(forest_height):
        for x in range(forest_width):
            height = trees[y][x]

            # horizontal
            left_done = False
            left_view = 0
            right_done = False
            right_view = 0
            for i in range(1, forest_width):
                if x - i < 0:
                    left_done = True
                if x + i >= forest_width:
                    right_done = True

                if left_done and right_done:
                    break

                if not left_done:
                    left_view += 1
                    if trees[y][x - i] >= height:
                        left_done = True

                if not right_done:
                    right_view += 1
                    if trees[y][x + i] >= height:
                        right_done = True

            # vertical
            up_done = False
            up_view = 0
            down_done = False
            down_view = 0
            for j in range(1, forest_height):
                if y - j < 0:
                    up_done = True
                if y + j >= forest_height:
                    down_done = True

                if up_done and down_done:
                    break

                if not up_done:
                    up_view += 1
                    if trees[y - j][x] >= height:
                        up_done = True

                if not down_done:
                    down_view += 1
                    if trees[y + j][x] >= height:
                        down_done = True

            scenicity = up_view * down_view * left_view * right_view
            if scenicity > best:
                best = scenicity

    return best


if __name__ == "__main__":
    trees = load_input(sys.argv[1])
    print(part_1(trees))
    print(part_2(trees))
