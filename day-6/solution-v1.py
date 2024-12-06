def solution():
    solution = 0
    map = []

    with open("input.txt") as f:
        lines = f.readlines()

    # Create matrix map
    for line in lines:
        map.append(list(line.strip()))

    # Search for the guard
    x, y = get_guard_position(map)
    map[x][y] = "X"
    directions = ["up", "right", "down", "left"]
    direction = directions[0]

    # Move the guard
    while True:
        # Get next position
        if direction == "up":
            x = x - 1
            map[x][y] = "X"

            if x <= 0:
                break
            else:
                next = map[x - 1][y]
        elif direction == "right":
            y = y + 1
            map[x][y] = "X"

            if y >= len(map) - 1:
                break
            else:
                next = map[x][y + 1]
        elif direction == "down":
            x = x + 1
            map[x][y] = "X"

            if x >= len(map[0]) - 1:
                break
            else:
                next = map[x + 1][y]

        elif direction == "left":
            y = y - 1
            map[x][y] = "X"

            if y <= 0:
                break
            else:
                next = map[x][y - 1]
        else:
            break

        # Change direction at any obstacle
        if next == "#":
            i = directions.index(direction)
            direction = directions[(i + 1) % 4]
        else:
            map[x][y] = "X"

    # Count X on the map
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == "X":
                solution += 1

    return solution


def get_guard_position(map):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == "^":
                return x, y
    return -1, -1


if __name__ == "__main__":
    print(f"Solution: {solution()}")
