#!/usr/bin/env python3

import sys


def load_input(path: str) -> list[int | None]:
    instructions: list[int | None] = []

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line == "noop":
                instructions.append(None)
            else:
                instructions.append(int(line.split(" ")[1]))

    return instructions


def at_least_its_not_intcode(instructions: list[int | None]) -> None:
    signal = 0
    register = 1
    checkpoints = (x for x in [20, 60, 100, 140, 180, 220])
    checkpoint = next(checkpoints)
    instructions = (x for x in instructions)
    instruction = next(instructions)

    part_1_finished = False
    processing = False
    display = ""

    for clock in range(240):
        if clock % 40 == 0:
            display += "\n"
        if register - 1 <= clock % 40 <= register + 1:
            display += "#"
        else:
            display += "."

        if not part_1_finished:
            if clock + 1 == checkpoint:
                signal += register * checkpoint
                checkpoint = next(checkpoints, None)
                if checkpoint is None:
                    part_1_finished = True

        if processing:
            register += instruction
            processing = False
            instruction = next(instructions, None)
        else:
            if instruction is None:
                instruction = next(instructions, None)

            else:
                processing = True

    print(signal)
    print(display[1:])


if __name__ == "__main__":
    instructions = load_input(sys.argv[1])
    at_least_its_not_intcode(instructions)
