import re


def solution():
    solution = 0

    with open("input.txt") as f:
        lines = f.readlines()

    # Make it one long string
    memory = "".join(lines)

    # Extract all modifiers using and safe the position in the string
    mod_do = [m.start() for m in re.finditer("do\(\)", memory)]
    mod_dont = [m.start() for m in re.finditer("don't\(\)", memory)]

    # Make map of what should be done and what should be ignored
    do_map = [True] * len(memory)

    status = True
    for i in range(len(do_map)):
        if i in mod_do:
            do_map[i] = True
            status = True
        elif i in mod_dont:
            do_map[i] = False
            status = False
        else:
            do_map[i] = status

    # Extract all mul operatations using regex
    # Example mul(X,Y)
    entries = re.findall(r"mul\((\d+),(\d+)\)", memory)
    entries_position = [m.start() for m in re.finditer(r"mul\(\d+,\d+\)", memory)]
    for i, entry in enumerate(entries):
        if do_map[entries_position[i]] is False:
            continue
        else:
            x, y = map(int, entry)
            solution += x * y

    return solution


if __name__ == "__main__":
    print(f"Solution: {solution()}")
