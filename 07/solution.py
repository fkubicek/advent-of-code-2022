from typing import Self

from aoc22_util.input import *

class Directory:

    def __init__(self, parent):
        self.items = {}
        self.parent = parent
    
    def get_subdir(self, subdir) -> Self:
        return self.items.setdefault(subdir, Directory(self))
    
    def add_file(self, file, size):
        self.items[file] = size

    def all_dir_sizes(self):
        res = []
        total = 0
        for item in self.items.values():
            if isinstance(item, Directory):
                res.extend(item.all_dir_sizes())
                total += res[-1]
            else:
                total += item
        res.append(total)
        return res

    def __str__(self, level=0):
        res = []
        indent = " " * level * 2
        for name, item in self.items.items():
            if isinstance(item, Directory):
                res.append(f"{indent}- {name} (dir)")
                res.append(item.__str__(level + 1))
            else:
                res.append(f"{indent}- {name} ({item})")
        return "\n".join(res)


if __name__ == "__main__":
    root = Directory(None)

    for line in file_readlines_stripped("07/input.txt"):

        match line.split():
            case ["$", "cd", "/"]:
                current = root
            case ["$", "cd", ".."]:
                current = current.parent
            case ["$", "cd", subdir]:
                current = current.get_subdir(subdir)
            case ["$", "ls"]:
                pass
            case ["dir", name]:
                pass
            case [size, name]:
                current.add_file(name, int(size))
            case _:
                raise Exception(f"Unknown command: {line}")

    print(root)
    all_dir_sizes = root.all_dir_sizes()

    print("part one:", sum(filter(lambda x: x<=100000, all_dir_sizes)))

    filesystem = 70000000
    needed = 30000000
    free = filesystem - all_dir_sizes[-1]
    to_delete = needed - free

    print("part two:", min(filter(lambda x: x>=to_delete, all_dir_sizes)))
