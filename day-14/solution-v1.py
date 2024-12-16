def solution():
    steps = 100

    # Make map
    x = 103
    y = 101
    map = [[0 for _ in range(y)] for _ in range(x)]

    # Read robots position
    robots = []

    with open("input.txt") as f:
        for line in f:
            robot = {"position": {"x": -1, "y": -1}, "velocity": {"x": 0, "y": 0}}
            p, v = line.split(" ")

            # Parse data (x and y are inverted))
            x = int(p.replace("p=", "").split(",")[1])
            y = int(p.replace("p=", "").split(",")[0])
            vx = int(v.replace("v=", "").split(",")[1])
            vy = int(v.replace("v=", "").split(",")[0])

            # Get position
            robot["position"]["x"] = x
            robot["position"]["y"] = y

            # Get velocity
            robot["velocity"]["x"] = vx
            robot["velocity"]["y"] = vy

            # Add robot to map
            map[x][y] += 1

            robots.append(robot)

    # Run simulation
    c = 0
    while c < steps:
        for robot in robots:
            x = robot["position"]["x"]
            y = robot["position"]["y"]

            # Move robot
            map[x][y] -= 1

            # Compute new position
            x = (x + robot["velocity"]["x"]) % len(map)
            y = (y + robot["velocity"]["y"]) % len(map[0])

            # Save new position
            robot["position"]["x"] = x
            robot["position"]["y"] = y

            # Add robot to map
            map[x][y] += 1

        c += 1

    # Count robots in each quadrant (robots in the middle can be ignored)
    hh = int(len(map) // 2)
    hw = int(len(map[0]) // 2)

    solution = sum([map[x][y] for x in range(hh) for y in range(hw)])
    solution *= sum([map[x][y] for x in range(hh) for y in range(hw + 1, len(map[0]))])
    solution *= sum(
        [map[x][y] for x in range(hh + 1, len(map)) for y in range(hw + 1, len(map[0]))]
    )
    solution *= sum([map[x][y] for x in range(hh + 1, len(map)) for y in range(hw)])

    return solution


if __name__ == "__main__":
    print(f"Solution: {solution()}")
