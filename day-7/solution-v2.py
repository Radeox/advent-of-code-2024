from itertools import product


def solution():
    solution = 0
    equations = {}

    with open("input.txt") as f:
        lines = f.readlines()

    for line in lines:
        result = int(line.strip().split(": ")[0])
        equations[result] = [int(i) for i in line.strip().split(": ")[1].split(" ")]

    for eq in equations:
        # Get all possibile operations
        for ops in product(["+", "*", "||"], repeat=len(equations[eq]) - 1):
            # Make the equation
            result = equations[eq][0]
            for i, num in enumerate(equations[eq][1:]):
                if ops[i] == "||":
                    result = int(str(result) + str(num))
                else:
                    result = eval(f"{result} {ops[i]} {num}")

            if result == eq:
                solution += eq
                break

    return solution


if __name__ == "__main__":
    print(f"Solution: {solution()}")
