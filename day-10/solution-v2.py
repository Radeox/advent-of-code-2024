def solution():
    solution = 0
    map = []

    with open("input.txt") as f:
        input = f.readlines()

    # Clean up
    for line in range(len(input)):
        map.append([int(i) for i in list(input[line].strip())])

    # Look for 0-height
    start_points = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 0:
                start_points.append((x, y))

    for sp in start_points:
        solution += look_for_trails(map, sp[0], sp[1])

    return solution


def look_for_trails(map, x, y):
    def dfs(map, x, y, prev_value):
        if (
            not (0 <= x < len(map) and 0 <= y < len(map[0]))
            or map[x][y] != prev_value + 1
        ):
            return 0

        if map[x][y] == 9:
            return 1

        current_value = map[x][y]
        return (
            dfs(map, x + 1, y, current_value)
            + dfs(map, x - 1, y, current_value)
            + dfs(map, x, y + 1, current_value)
            + dfs(map, x, y - 1, current_value)
        )

    return dfs(map, x, y, -1)


if __name__ == "__main__":
    print(f"Solution: {solution()}")
