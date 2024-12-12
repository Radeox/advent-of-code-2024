def solution():
    solution = 0
    garden = []
    plots = []
    memory = []

    with open("example.txt") as f:
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
    for i, plot in enumerate(plots):
        plant = garden[plot[0][0]][plot[0][1]]

        # Compute area
        area = len(plot)

        # Compute perimeter
        perimeter = 0

        x_walls = set()
        y_walls = set()

        for x, y in plot:
            if (
                x < len(garden) - 1
                and x + 1 not in x_walls
                and garden[x + 1][y] != plant
            ):
                x_walls.add(x + 1)

            if x > 0 and x - 1 not in x_walls and garden[x - 1][y] != plant:
                x_walls.add(x - 1)

            if (
                y < len(garden[0]) - 1
                and y + 1 not in y_walls
                and garden[x][y + 1] != plant
            ):
                y_walls.add(y + 1)

            if y > 0 and y - 1 not in y_walls and garden[x][y - 1] != plant:
                y_walls.add(y - 1)

            if x in x_walls and not y in y_walls:
                perimeter -= 1

            elif y in y_walls and x not in x_walls:
                perimeter -= 1

            else:
                perimeter += 3

        print(f"X Walls: {x_walls}")
        print(f"Y Walls: {y_walls}")

        # v_walls = set()
        # h_walls = set()
        #
        # for x, y in plot:
        #     print(f"Plot {plant}: {x},{y}")
        #     # Up
        #     if x > 0 and garden[x - 1][y] != plant and x - 1 not in v_walls:
        #         perimeter += 1
        #         v_walls.add(x - 1)
        #
        #     # Down
        #     if (
        #         x < len(garden) - 1
        #         and garden[x + 1][y] != plant
        #         and x + 1 not in v_walls
        #     ):
        #         perimeter += 1
        #         v_walls.add(x + 1)
        #
        #     # Left
        #     if y > 0 and garden[x][y - 1] != plant and y - 1 not in h_walls:
        #         perimeter += 1
        #         h_walls.add(y - 1)
        #
        #     # Right
        #     if (
        #         y < len(garden[x]) - 1
        #         and garden[x][y + 1] != plant
        #         and y + 1 not in h_walls
        #     ):
        #         perimeter += 1
        #         h_walls.add(y + 1)
        #
        #     # Edges
        #     if x == 0 or x == len(garden) - 1 and x not in v_walls:
        #         perimeter += 1
        #         v_walls.add(x)
        #
        #     if y == 0 or y == len(garden[x]) - 1 and y not in h_walls:
        #         perimeter += 1
        #         h_walls.add(y)
        #
        # print(f"Horizontal: {h_walls}")
        # print(f"Vertical: {v_walls}")

        # Discounts
        # if x > 0 and garden[x - 1][y] == plant:
        #     perimeter -= 1
        #
        # if x < len(garden) - 1 and garden[x + 1][y] == plant:
        #     perimeter -= 1
        #
        # if y > 0 and garden[x][y - 1] == plant:
        #     perimeter -= 1
        #
        # if y < len(garden[x]) - 1 and garden[x][y + 1] == plant:
        #     perimeter -= 1

        # Compute plot cost
        print(f"Plot {plant}: A:{area} P:{perimeter}")
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
