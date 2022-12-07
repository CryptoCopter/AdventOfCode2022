#!/usr/bin/env python3

import sys


FILE_SYSTEM_SIZE = 70000000
UPDATE_REQUIRES = 30000000


class Directory:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent: Directory | None = parent
        self.sub_dirs: dict[str, Directory] = {}
        self.files: dict[str, int] = {}
        self.size = 0

    def __str__(self) -> str:
        if self.name == "/":
            return "/"

        return f"{self.parent.name}{self.name}/"

    def enlarge(self, size: int) -> None:
        self.size += size
        if self.parent:
            self.parent.enlarge(size)


def load_input(path: str) -> Directory:
    root = Directory(name="/")
    work_dir = root

    command_mode = True
    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(" ")
            if parts[0] == "$":
                command_mode = True

            if command_mode:
                if parts[1] == "ls":
                    command_mode = False
                elif parts[1] == "cd":
                    if parts[2] == "/":
                        work_dir = root
                    elif parts[2] == "..":
                        work_dir = work_dir.parent
                    else:
                        work_dir = work_dir.sub_dirs[parts[2]]
            else:
                if parts[0] == "dir" and parts[1] not in work_dir.sub_dirs:
                    child = Directory(name=parts[1], parent=work_dir)
                    work_dir.sub_dirs[parts[1]] = child
                else:
                    if parts[1] not in work_dir.files:
                        file_size = int(parts[0])
                        work_dir.files[parts[1]] = file_size
                        work_dir.enlarge(file_size)

    return root


def tree_traversal(
    work_dir: Directory,
    part_2_required: int,
    part_1: int = 0,
    part_2: int | None = None,
) -> (int, int):
    if work_dir.size <= 100000:
        part_1 += work_dir.size

    if work_dir.size >= part_2_required:
        if not part_2 or work_dir.size < part_2:
            part_2 = work_dir.size

    for subdir in work_dir.sub_dirs.values():
        part_1, part_2 = tree_traversal(subdir, part_2_required, part_1, part_2)

    return part_1, part_2


if __name__ == "__main__":
    root_dir = load_input(sys.argv[1])
    free_space = FILE_SYSTEM_SIZE - root_dir.size
    free_required = UPDATE_REQUIRES - free_space
    part_1, part_2 = tree_traversal(root_dir, free_required)
    print(part_1)
    print(part_2)
