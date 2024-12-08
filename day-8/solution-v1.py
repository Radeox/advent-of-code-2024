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
                o, p = pair[0][0] - distance_x, pair[0][1] + distance_y
                k, l = pair[1][0] + distance_x, pair[1][1] - distance_y
            else:
                o, p = pair[0][0] - distance_x, pair[0][1] - distance_y
                k, l = pair[1][0] + distance_x, pair[1][1] + distance_y

            # If op is in bounds, mark it
            if 0 <= o < len(map) and 0 <= p < len(map[0]):
                map[o][p] = "#"

            # If kl is in bounds, mark it
            if 0 <= k < len(map) and 0 <= l < len(map[0]):
                map[k][l] = "#"

    # Print map
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == "#":
                solution += 1

    return solution


if __name__ == "__main__":
    print(f"Solution: {solution()}")
