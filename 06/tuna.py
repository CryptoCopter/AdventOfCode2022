#!/usr/bin/env python3

import sys


def sliding_window(data_stream: str) -> tuple[int, int]:
    i = 0
    packet_start = 0
    mesage_start = 0
    while i + 14 < len(data_stream):
        if not packet_start:
            window = set(data_stream[i : i + 4])
            if len(window) == 4:
                packet_start = i + 4
        if not mesage_start:
            window = set(data_stream[i : i + 14])
            if len(window) == 14:
                mesage_start = i + 14
        if packet_start and mesage_start:
            break
        i += 1
    return packet_start, mesage_start


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        data_stream = f.readline()

    part_1, part_2 = sliding_window(data_stream)
    print(part_1)
    print(part_2)
