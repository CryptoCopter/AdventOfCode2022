#!/usr/bin/env python3

import sys
from functools import cmp_to_key
from copy import deepcopy


def load_input(path: str) -> list[tuple[list, list]]:
    packets: list[tuple[list, list]] = []

    with open(path, "r") as f:
        input = f.read()

    for pairs in input.strip().split("\n\n"):
        left, right = pairs.split("\n")
        packets.append((eval(left), eval(right)))

    return packets


def check_order(left: int | list | None, right: int | list | None) -> int | None:
    match left, right:
        case int(), int():
            if left < right:
                return -1
            elif left > right:
                return 1
            else:
                return 0

        case list(), list():
            len_diff = len(left) - len(right)
            if len_diff > 0:
                right_padded = right + [None] * abs(len_diff)
                left_padded = deepcopy(left)
            elif len_diff < 0:
                right_padded = deepcopy(right)
                left_padded = left + [None] * abs(len_diff)
            else:
                right_padded = deepcopy(right)
                left_padded = deepcopy(left)

            for left_elem, right_elem in zip(left_padded, right_padded):
                order = check_order(left_elem, right_elem)
                if order:
                    return order
            return 0

        case None, int():
            return -1

        case None, list():
            return -1

        case int(), None:
            return 1

        case list(), None:
            return 1

        case int(), list():
            return check_order([left], right)

        case list(), int():
            return check_order(left, [right])


def check_orders(data: list[tuple[list, list]]) -> int:
    index_sum = 0

    for i in range(len(data)):
        if check_order(data[i][0], data[i][1]) < 0:
            index_sum += i + 1

    return index_sum


def order_packets(data: list[tuple[list, list]]) -> int:
    dividers = [[[2]], [[6]]]
    all_packets: list[list] = []

    for left, right in data:
        all_packets.append(left)
        all_packets.append(right)

    all_packets += dividers

    in_order = sorted(all_packets, key=cmp_to_key(check_order))

    return (in_order.index(dividers[0]) + 1) * (in_order.index(dividers[1]) + 1)


if __name__ == "__main__":
    data = load_input(sys.argv[1])
    print(check_orders(data))
    print(order_packets(data))
