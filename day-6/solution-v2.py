def solution():
    solution = 0
    map = []

    with open("input.txt") as f:
        lines = f.readlines()

    # Create matrix map
    for line in lines:
        map.append(list(line.strip()))

    # Compute all possibile position where put the obstacle
    for x in range(len(map)):
        for y in range(len(map[x])):
            new_reality = [row[:] for row in map]
            new_reality[x][y] = "#"
            if check_new_reality(new_reality) == False:
                solution += 1

    # Count X on the map
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == "X":
                solution += 1

    return solution


def check_new_reality(map):
    max_moves = len(map) * len(map[0])

    # Search for the guard
    x, y = get_guard_position(map)

    map[x][y] = "X"
    directions = ["up", "right", "down", "left"]
    direction = directions[0]

    # Move the guard
    while True:
        if x <= 0 or y <= 0 or x >= len(map) - 1 or y >= len(map[0]) - 1:
            break

        # Get next position
        if direction == "up":
            next = map[x - 1][y]
        elif direction == "right":
            next = map[x][y + 1]
        elif direction == "down":
            next = map[x + 1][y]
        elif direction == "left":
            next = map[x][y - 1]
        else:
            break

        # Change direction at any obstacle
        if next == "#":
            i = directions.index(direction)
            direction = directions[(i + 1) % 4]
            max_moves -= 1
        else:
            map[x][y] = "X"

            if next == "X":
                max_moves -= 1
            else:
                max_moves += 1

            if direction == "up":
                x = x - 1
            elif direction == "right":
                y = y + 1
            elif direction == "down":
                x = x + 1
            elif direction == "left":
                y = y - 1
            else:
                break

        if max_moves == 0:
            return False

    return True


def get_guard_position(map):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == "^":
                return x, y
    return -1, -1


if __name__ == "__main__":
    print(f"Solution: {solution()}")
