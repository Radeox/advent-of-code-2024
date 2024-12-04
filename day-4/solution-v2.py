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
            # If start found (A), search for the rest in all diagonals
            c = 0
            if matrix[i][j] == "A":
                if (
                    i - 1 >= 0
                    and j - 1 >= 0
                    and i + 1 < len(matrix)
                    and j + 1 < len(matrix[i])
                ):
                    if matrix[i - 1][j - 1] == "M" and matrix[i + 1][j + 1] == "S":
                        c += 1

                if (
                    i - 1 >= 0
                    and j - 1 >= 0
                    and i + 1 < len(matrix)
                    and j + 1 < len(matrix[i])
                ):
                    if matrix[i - 1][j - 1] == "S" and matrix[i + 1][j + 1] == "M":
                        c += 1

                if (
                    i + 1 < len(matrix)
                    and j - 1 >= 0
                    and i - 1 >= 0
                    and j + 1 < len(matrix[i])
                ):
                    if matrix[i + 1][j - 1] == "M" and matrix[i - 1][j + 1] == "S":
                        c += 1

                if (
                    i + 1 < len(matrix)
                    and j - 1 >= 0
                    and i - 1 >= 0
                    and j + 1 < len(matrix[i])
                ):
                    if matrix[i + 1][j - 1] == "S" and matrix[i - 1][j + 1] == "M":
                        c += 1

                if c == 2:
                    solution += 1

    return solution


if __name__ == "__main__":
    print(f"Solution: {solution()}")
