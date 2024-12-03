import re


def solution():
    solution = 0

    with open("input.txt") as f:
        lines = f.readlines()

    # Make it one long string
    memory = "".join(lines)

    # Extract all mul operatations using regex
    # Example mul(X,Y)
    entries = re.findall(r"mul\((\d+),(\d+)\)", memory)
    for entry in entries:
        x, y = map(int, entry)
        solution += x * y

    return solution


if __name__ == "__main__":
    print(f"Solution: {solution()}")
