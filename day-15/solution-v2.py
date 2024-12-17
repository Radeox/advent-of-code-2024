def solution():
    map = []
    moves = []
    robot = tuple([0, 0])

    with open("example2.txt") as f:
        map_complete = False

        for line in f:
            line = line.strip()

            if line == "":
                map_complete = True
                continue

            if not map_complete:
                # Restructure map -> each element is wider
                line = line.replace("#", "##")
                line = line.replace("O", "[]")
                line = line.replace(".", "..")
                line = line.replace("@", "@.")

                map.append(list(line))
            else:
                moves.append(list(line))

    # Collapse moves to single list
    moves = [move for sublist in moves for move in sublist]

    # Find start
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == "@":
                robot = tuple([x, y])
                break

    # Move robot
    for move in moves:
        print(f"--- Move: {move} ---")
        for x in range(len(map)):
            for y in range(len(map[0])):
                print(map[x][y], end="")
            print()

        robot = do_move(map, robot[0], robot[1], move)

    # Compute solution
    solution = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == "[":
                # GPS equals distance from top left corner
                solution += 100 * x + y

    return solution


def do_move(map, x, y, next_move):
    dx = 0
    dy = 0

    match next_move:
        case "^":
            dx -= 1
            dy = 0
        case "v":
            dx += 1
            dy = 0
        case "<":
            dx = 0
            dy -= 1
        case ">":
            dx = 0
            dy += 1

    if map[x + dx][y + dy] not in ["#", "."]:
        do_move(map, x + dx, y + dy, next_move)

    if map[x + dx][y + dy] != ".":
        return (x, y)
    else:
        if map[x + dx][y + dy] == "[":
            map[x + dx][y + dy] = map[x][y]
            map[x][y] = "."

            map[x + dx][y + dy + 1] = map[x][y + 1]
            map[x][y + 1] = "."
        else:
            map[x + dx][y + dy] = map[x][y]
            map[x][y] = "."

            map[x + dx][y + dy - 1] = map[x][y - 1]
            map[x][y - 1] = "."

        return (x + dx, y + dy)


if __name__ == "__main__":
    print(f"Solution: {solution()}")
