def solution():
    solution = 0
    garden = []
    plots = []
    memory = []

    with open("input.txt") as f:
        for line in f:
            garden.append(list(line.strip()))

    # Find all types of plants
    plants = set()
    for x in range(len(garden)):
        for y in range(len(garden[x])):
            plants.add(garden[x][y])

    # Search for plots
    for x in range(len(garden)):
        for y in range(len(garden[x])):
            plot = expand_plot(garden, x, y, garden[x][y], memory)
            if plot == []:
                continue

            plots.append(plot)

            for plant in plot:
                memory.append(plant)

    # Compute area and perimeter of each plot
    for plot in plots:
        plant = garden[plot[0][0]][plot[0][1]]

        # Compute area
        area = len(plot)

        # Compute perimeter
        perimeter = 0
        for x, y in plot:
            if x > 0 and garden[x - 1][y] != plant:
                perimeter += 1

            if x < len(garden) - 1 and garden[x + 1][y] != plant:
                perimeter += 1

            if y > 0 and garden[x][y - 1] != plant:
                perimeter += 1

            if y < len(garden[x]) - 1 and garden[x][y + 1] != plant:
                perimeter += 1

            # Edges
            if x == 0 or x == len(garden) - 1:
                perimeter += 1

            if y == 0 or y == len(garden[x]) - 1:
                perimeter += 1

        # Compute plot cost
        cost = area * perimeter
        solution += cost

    return solution


def expand_plot(map, x, y, kind, to_ignore):
    if (x, y) in to_ignore:
        return []

    plot = [(x, y)]

    if x > 0 and map[x - 1][y] == kind and (x - 1, y) not in to_ignore:
        plot += expand_plot(map, x - 1, y, kind, to_ignore + plot)
    if x < len(map) - 1 and map[x + 1][y] == kind and (x + 1, y) not in to_ignore:
        plot += expand_plot(map, x + 1, y, kind, to_ignore + plot)
    if y > 0 and map[x][y - 1] == kind and (x, y - 1) not in to_ignore:
        plot += expand_plot(map, x, y - 1, kind, to_ignore + plot)
    if y < len(map[x]) - 1 and map[x][y + 1] == kind and (x, y + 1) not in to_ignore:
        plot += expand_plot(map, x, y + 1, kind, to_ignore + plot)

    return plot


if __name__ == "__main__":
    print(f"Solution: {solution()}")
