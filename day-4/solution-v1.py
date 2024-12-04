def solution():
    with open("input.txt") as f:
        matrix = f.readlines()

    # Clean up the matrix
    matrix = [line.strip() for line in matrix]

    return search_for_xmas(matrix)


def search_for_xmas(matrix):
    solution = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # If start found (X), search for the rest in all directions
            if matrix[i][j] == "X":
                letters = ["X", "M", "A", "S"]
                directions = [
                    "up",
                    "down",
                    "left",
                    "right",
                    "up-left",
                    "up-right",
                    "down-left",
                    "down-right",
                ]

                for direction in directions:
                    target = ["X"]
                    offset = 1

                    while look_for_next(matrix, i, j, direction, offset):
                        target.append(letters[offset])
                        offset += 1

                        if target == ["X", "M", "A", "S"]:
                            solution += 1
                            break

    return solution


def look_for_next(matrix, x, y, direction, offset):
    letters = ["X", "M", "A", "S"]
    look_for = letters[offset]

    if direction == "up":
        h = -1 * offset
        v = 0 * offset
    elif direction == "down":
        h = 1 * offset
        v = 0 * offset
    elif direction == "left":
        h = 0 * offset
        v = -1 * offset
    elif direction == "right":
        h = 0 * offset
        v = 1 * offset
    elif direction == "up-left":
        h = -1 * offset
        v = -1 * offset
    elif direction == "up-right":
        h = -1 * offset
        v = 1 * offset
    elif direction == "down-left":
        h = 1 * offset
        v = -1 * offset
    elif direction == "down-right":
        h = 1 * offset
        v = 1 * offset
    else:
        raise ValueError("Invalid direction")

    if x + h < 0 or x + h >= len(matrix):
        return False
    elif y + v < 0 or y + v >= len(matrix[x]):
        return False
    elif matrix[x + h][y + v] == look_for:
        return True
    else:
        return False


if __name__ == "__main__":
    print(f"Solution: {solution()}")
