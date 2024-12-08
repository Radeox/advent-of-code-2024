import itertools


def solution():
    solution = 0
    map = []
    antennas = {}

    with open("input.txt") as f:
        lines = f.readlines()

    # Make map
    for line in lines:
        map.append(list(line.strip()))

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] != ".":
                if map[x][y] not in antennas:
                    antennas[map[x][y]] = []

                antennas[map[x][y]].append((x, y))

    for freq in antennas:
        # Compute all possible pairs of antennas
        for pair in itertools.combinations(antennas[freq], 2):
            distance_x = abs(pair[0][0] - pair[1][0])
            distance_y = abs(pair[0][1] - pair[1][1])

            # Compute distance between antennas
            if pair[0][1] > pair[1][1]:
                o, p = pair[0][0], pair[0][1]
                k, l = pair[1][0], pair[1][1]

                while True:
                    if 0 <= o < len(map) and 0 <= p < len(map[0]):
                        map[o][p] = "#"
                        o -= distance_x
                        p += distance_y
                    else:
                        break

                while True:
                    if 0 <= k < len(map) and 0 <= l < len(map[0]):
                        map[k][l] = "#"
                        k += distance_x
                        l -= distance_y
                    else:
                        break

            else:
                o, p = pair[0][0], pair[0][1]
                k, l = pair[1][0], pair[1][1]

                while True:
                    if 0 <= o < len(map) and 0 <= p < len(map[0]):
                        map[o][p] = "#"
                        o -= distance_x
                        p -= distance_y
                    else:
                        break

                while True:
                    if 0 <= k < len(map) and 0 <= l < len(map[0]):
                        map[k][l] = "#"
                        k += distance_x
                        l += distance_y
                    else:
                        break

    # Print map
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == "#":
                solution += 1

    return solution


if __name__ == "__main__":
    print(f"Solution: {solution()}")
