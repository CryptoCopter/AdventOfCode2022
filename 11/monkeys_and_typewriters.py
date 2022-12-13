#!/usr/bin/env python3

import sys
from typing import Callable
from copy import deepcopy


MONKEYS: dict[int, "Monkey"] = {}
SUPER_MOD = 1


class Monkey:
    def __init__(self, id: int):
        self.id = id
        self.items: list[int] = []
        self.mod: int = 0
        self.target_true: int = 0
        self.target_false: int = 0
        self.operation: Callable[[int], int] = None
        self.inspections = 0

    def __str__(self) -> str:
        return f"Monkey {self.id}"

    def business(self, div: bool):
        for item in self.items:
            self.inspections += 1
            item = self.operation(item)

            item = item % SUPER_MOD
            if div:
                item = int(item / 3)

            if item % self.mod == 0:
                MONKEYS[self.target_true].items.append(item)
            else:
                MONKEYS[self.target_false].items.append(item)

        self.items = []


def load_input(path: str) -> None:
    monkey: Monkey | None = None

    with open(path, "r") as f:
        for line in f:
            match line.strip().split(" "):
                case ["Monkey", index]:
                    if monkey is not None:
                        MONKEYS[monkey.id] = monkey
                    monkey = Monkey(int(index[:-1]))
                case ["Starting", "items:", *items]:
                    monkey.items = [int(item) for item in "".join(items).split(",")]
                case ["Operation:", *operation]:
                    operation = "".join(operation[-3:])
                    monkey.operation = eval(f"lambda old: {operation}")
                case ["Test:", *mod]:
                    monkey.mod = int(mod[-1])
                case ["If", "true:", *target]:
                    monkey.target_true = int(target[-1])
                case ["If", "false:", *target]:
                    monkey.target_false = int(target[-1])

    MONKEYS[monkey.id] = monkey

    for monkey in MONKEYS.values():
        global SUPER_MOD
        SUPER_MOD *= monkey.mod


def business(rounds: int, div: bool) -> int:
    for i in range(rounds):
        for monkey in MONKEYS.values():
            monkey.business(div)

    business = sorted([monkey.inspections for monkey in MONKEYS.values()], reverse=True)

    return business[0] * business[1]


if __name__ == "__main__":
    load_input(sys.argv[1])
    monkeys = deepcopy(MONKEYS)
    print(business(20, True))
    MONKEYS = monkeys
    print(business(10000, False))
