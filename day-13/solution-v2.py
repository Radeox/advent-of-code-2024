def solution():
    arcades = []
    cost_a = 3
    solution = 0

    game = {"button_a": {}, "button_b": {}, "prize": {}}

    with open("input.txt") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            text = line.split(": ")[0]
            data = line.split(": ")[1]

            if text == "Button A":
                game["button_a"]["X"] = int(data.split(", ")[0].replace("X+", ""))
                game["button_a"]["Y"] = int(data.split(", ")[1].replace("Y+", ""))
            elif text == "Button B":
                game["button_b"]["X"] = int(data.split(", ")[0].replace("X+", ""))
                game["button_b"]["Y"] = int(data.split(", ")[1].replace("Y+", ""))
            elif text == "Prize":
                game["prize"]["X"] = int(data.split(", ")[0].replace("X=", ""))
                game["prize"]["Y"] = int(data.split(", ")[1].replace("Y=", ""))

                # Add 10000000000000 to each coordinate due to conversion error
                game["prize"]["X"] += 10000000000000
                game["prize"]["Y"] += 10000000000000

                arcades.append(game)
                game = {"button_a": {}, "button_b": {}, "prize": {}}

    for game in arcades:
        ax = game["button_a"]["X"]
        ay = game["button_a"]["Y"]

        bx = game["button_b"]["X"]
        by = game["button_b"]["Y"]

        px = game["prize"]["X"]
        py = game["prize"]["Y"]

        b = (ay * px - ax * py) / (ay * bx - ax * by)
        a = (px - bx * b) / ax

        if not a.is_integer() or not b.is_integer():
            continue

        if a * ax + b * bx != px or a * ay + b * by != py:
            continue

        solution += int(a * cost_a + b)

    return solution


if __name__ == "__main__":
    print(f"Solution: {solution()}")
