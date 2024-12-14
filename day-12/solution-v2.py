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
        perimeter = 0

        for p in plot:
            x, y = p

            tl = (x - 1, y - 1)
            tr = (x - 1, y + 1)
            bl = (x + 1, y - 1)
            br = (x + 1, y + 1)

            left = (x, y - 1)
            right = (x, y + 1)
            top = (x - 1, y)
            bottom = (x + 1, y)

            # Outer corners
            ## Top left
            if top not in plot and left not in plot:
                perimeter += 1

            ## Top right
            if top not in plot and right not in plot:
                perimeter += 1

            ## Bottom left
            if bottom not in plot and left not in plot:
                perimeter += 1

            ## Bottom right
            if bottom not in plot and right not in plot:
                perimeter += 1

            # Inner corners
            ## Top left
            if top in plot and left in plot and tl not in plot:
                perimeter += 1

            ## Top right
            if top in plot and right in plot and tr not in plot:
                perimeter += 1

            ## Bottom left
            if bottom in plot and left in plot and bl not in plot:
                perimeter += 1

            ## Bottom right
            if bottom in plot and right in plot and br not in plot:
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
