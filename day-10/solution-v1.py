def solution():
    solution = 0
    input = []
    map = []
    scores = {}

    with open("example.txt") as f:
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
        path = look_for_trails(map, sp[0], sp[1], 0)
        print(path)
        step = 0

        for x in range(len(map)):
            for y in range(len(map[x])):
                if (x, y) in path and map[x][y] > step:
                    step = map[x][y]

        if step == 9:
            if sp in scores:
                scores[sp] += 1
            else:
                scores[sp] = 1

    print(scores)

    return solution


def look_for_trails(map, x, y, value):
    paths = []

    if value == 9:
        return paths

    # Left
    if x > 0 and map[x - 1][y] == value + 1:
        paths.append(look_for_trails(map, x - 1, y, value + 1))

    # Up
    if y > 0 and map[x][y - 1] == value + 1:
        paths.append(look_for_trails(map, x, y - 1, value + 1))

    # Right
    if x < len(map[0]) - 1 and map[x + 1][y] == value + 1:
        paths.append(look_for_trails(map, x + 1, y, value + 1))

    # Down
    if y < len(map) - 1 and map[x][y + 1] == value + 1:
        paths.append(look_for_trails(map, x, y + 1, value + 1))

    return (x, y)


if __name__ == "__main__":
    print(f"Solution: {solution()}")
