import os


def solution():
    map = []
    moves = []
    robot = tuple([0, 0])

    with open("input.txt") as f:
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

    for x in range(len(map)):
        for y in range(len(map[0])):
            print(map[x][y], end="")
        print()

    # Collapse moves to single list
    moves = [move for sublist in moves for move in sublist]

    # Find start
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == "@":
                robot = tuple([x, y])
                break

    # Move robot
    for c, move in enumerate(moves):
        # Make copy of map and robot position
        revert_map = [row[:] for row in map]
        robot_before = robot

        # Make the move
        robot = do_move(map, robot[0], robot[1], move)

        # Search for broken boxes
        for x in range(len(map)):
            for y in range(len(map[0])):
                if map[x][y] == "[":
                    if map[x][y + 1] != "]":
                        # Revert map and robot position
                        robot = robot_before

                        for x in range(len(map)):
                            for y in range(len(map[0])):
                                map[x][y] = revert_map[x][y]

                        break

        os.system("clear")
        print(f"--- Move: {move} ({c}/{len(moves)})---")
        for x in range(len(map)):
            for y in range(len(map[0])):
                print(map[x][y], end="")
            print()
        input()

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

    # If moving a box
    if map[x + dx][y + dy] not in ["#", "."]:
        if map[x + dx][y + dy] == "[" and next_move in ["^", "v"]:
            do_move(map, x + dx, y + dy + 1, next_move)
            do_move(map, x + dx, y + dy, next_move)
        elif map[x + dx][y + dy] == "]" and next_move in ["^", "v"]:
            do_move(map, x + dx, y + dy, next_move)
            do_move(map, x + dx, y + dy - 1, next_move)
        else:
            do_move(map, x + dx, y + dy, next_move)

    if map[x + dx][y + dy] != ".":
        return (x, y)
    else:
        map[x + dx][y + dy] = map[x][y]
        map[x][y] = "."

        return (x + dx, y + dy)


if __name__ == "__main__":
    print(f"Solution: {solution()}")
