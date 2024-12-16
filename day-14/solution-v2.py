import os

from PIL import Image


def solution():
    steps = 10000

    # Make map
    x = 103
    y = 101
    map = [[0 for _ in range(y)] for _ in range(x)]

    # Read robots position
    robots = []

    # Make output dir
    if not os.path.exists("output"):
        os.makedirs("output")

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
        print(c)
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

        # Create image
        image = Image.new("RGB", (len(map), len(map[0])), "black")
        pixels = image.load()

        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] > 0:
                    pixels[i, j] = (255, 255, 255)

        image.save(f"output/{c}.png")
        c += 1


if __name__ == "__main__":
    solution()
    print("Solution saved in output directory")
