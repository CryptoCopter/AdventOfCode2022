#!/usr/bin/env python3

import sys


def load_input(path: str) -> tuple[list[list[int]], tuple[int, int], tuple[int, int]]:
    area: list[list[int]] = []
    y = 0
    start = (0, 0)
    end = (0, 0)

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            x = 0
            row: list[int] = []
            for height in line:
                if height == "S":
                    row.append(0)
                    start = (y, x)
                elif height == "E":
                    row.append(25)
                    end = (y, x)
                else:
                    row.append(ord(height) - 97)
                x += 1
            area.append(row)
            y += 1

    return area, start, end


def do_the_dijkstra(
    area: list[list[int]], start: tuple[int, int], end: tuple[int, int]
) -> int:
    area_height = len(area)
    area_width = len(area[0])
    distances = [[9999999] * area_width for _ in area]
    distances[start[0]][start[1]] = 0
    unvisited: set[tuple[int, int]] = set()
    unvisited.add(start)
    visited: set[tuple[int, int]] = set()

    while True:
        if not unvisited:
            return 9999999

        y, x = sorted(list(unvisited), key=lambda x: distances[x[0]][x[1]])[0]
        if (y, x) == end:
            return distances[y][x]

        if y > 0 and area[y - 1][x] <= area[y][x] + 1:
            distances[y - 1][x] = min([distances[y][x] + 1, distances[y - 1][x]])
            if (y - 1, x) not in visited:
                unvisited.add((y - 1, x))
        if x < area_width - 1 and area[y][x + 1] <= area[y][x] + 1:
            distances[y][x + 1] = min([distances[y][x] + 1, distances[y][x + 1]])
            if (y, x + 1) not in visited:
                unvisited.add((y, x + 1))
        if y < area_height - 1 and area[y + 1][x] <= area[y][x] + 1:
            distances[y + 1][x] = min([distances[y][x] + 1, distances[y + 1][x]])
            if (y + 1, x) not in visited:
                unvisited.add((y + 1, x))
        if x > 0 and area[y][x - 1] <= area[y][x] + 1:
            distances[y][x - 1] = min([distances[y][x] + 1, distances[y][x - 1]])
            if (y, x - 1) not in visited:
                unvisited.add((y, x - 1))

        visited.add((y, x))
        unvisited.remove((y, x))


def trail_mix(
    area: list[list[int]], start: tuple[int, int], end: tuple[int, int]
) -> tuple[int, int]:
    area_height = len(area)
    area_width = len(area[0])
    possible_starts = [
        (y, x)
        for y in range(area_height)
        for x in range(area_width)
        if (y, x) != start and area[y][x] == 0
    ]
    distances = [do_the_dijkstra(area, start, end)]
    distances += [do_the_dijkstra(area, start, end) for start in possible_starts]
    return distances[0], min(distances)


if __name__ == "__main__":
    area, start, end = load_input(sys.argv[1])
    part_1, part_2 = trail_mix(area, start, end)
    print(part_1)
    print(part_2)
