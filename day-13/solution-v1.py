def solution():
    arcades = []
    cost_a = 3
    cost_b = 1
    solution = 0

    game = {"button_a": {}, "button_b": {}, "prize": {}}

    with open("input.txt") as f:
        for line in f:
            line = line.strip()

            if not line:
                arcades.append(game)
                game = {"button_a": {}, "button_b": {}, "prize": {}}
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

    for game in arcades:
        for a in range(0, 100):
            for b in range(0, 100):
                if (
                    game["button_a"]["X"] * a + game["button_b"]["X"] * b
                    == game["prize"]["X"]
                    and game["button_a"]["Y"] * a + game["button_b"]["Y"] * b
                    == game["prize"]["Y"]
                ):
                    solution += cost_a * a + cost_b * b
                    continue

    return solution


if __name__ == "__main__":
    print(f"Solution: {solution()}")
