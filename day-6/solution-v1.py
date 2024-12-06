def solution():
    solution = 0
    map = []

    with open("example.txt") as f:
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
            i = x
            j = y + 1
        elif direction == "right":
            i = x + 1
            j = y
        elif direction == "down":
            i = x
            j = y - 1
        elif direction == "left":
            i = x - 1
            j = y
        else:
            i = x
            j = y

        next = map[i][j]

        # If out of bounds, break
        if i < 0 or i > len(map) - 1 or j < 0 or j > len(map[x]) - 1:
            break
        print(f"Position: {x}, {y}")

        # Change direction at any obstacle
        if next == "#":
            i = directions.index(direction)
            direction = directions[(i + 1) % 4]
        else:
            if direction == "up":
                x -= 1
                map[x][y] = "X"
            elif direction == "right":
                y += 1
                map[x][y] = "X"
            elif direction == "down":
                x += 1
                map[x][y] = "X"
            elif direction == "left":
                y -= 1
                map[x][y] = "X"

    # Count X on the map
    for x in range(len(map)):
        for y in range(len(map[x])):
            print(map[x][y], end="")
            if map[x][y] == "X":
                solution += 1
        print()

    return solution


def get_guard_position(map):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == "^":
                return x, y
    return -1, -1


if __name__ == "__main__":
    print(f"Solution: {solution()}")
