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
        unique_points = []
        points = flatten_list(look_for_trails(map, sp[0], sp[1]))

        # Remove duplicates
        for p in points:
            if p not in unique_points and p is not None:
                unique_points.append(p)

        solution += len(unique_points)

    return solution


def look_for_trails(map, x, y):
    def dfs(map, x, y, prev_value):
        if (
            not (0 <= x < len(map) and 0 <= y < len(map[0]))
            or map[x][y] != prev_value + 1
        ):
            return

        if map[x][y] == 9:
            return (x, y)

        current_value = map[x][y]
        return [
            position
            for position in [
                dfs(map, x + 1, y, current_value),
                dfs(map, x - 1, y, current_value),
                dfs(map, x, y + 1, current_value),
                dfs(map, x, y - 1, current_value),
            ]
        ]

    return dfs(map, x, y, -1)


def flatten_list(nested_list):
    flattened = []
    for element in nested_list:
        if isinstance(element, list):
            flattened.extend(flatten_list(element))
        else:
            flattened.append(element)
    return flattened


if __name__ == "__main__":
    print(f"Solution: {solution()}")
