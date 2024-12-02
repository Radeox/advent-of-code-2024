def solution():
    levels = {}
    solution = 0

    # Read input
    with open("input.txt") as f:
        lines = f.readlines()

    # Create levels structure
    i = 0
    for line in lines:
        for n in line.split(" "):
            if i not in levels:
                levels[i] = []

            levels[i].append(int(n))
        i += 1

    # Compute solution
    for level in levels.values():
        # Increasing
        if level[0] < level[1]:
            trend = 1
        # Decreasing
        elif level[0] > level[1]:
            trend = -1
        # Unsafe
        else:
            trend = 0

        prev_value = level.pop(0)
        while level:
            value = level.pop(0)

            # Check if trend is broken
            if prev_value < value and trend == 1:
                pass
            elif prev_value > value and trend == -1:
                pass
            else:
                trend = 0

            # Check if value changed too much
            if abs(value - prev_value) > 3 or value == prev_value:
                trend = 0

            # Prepare for next iteration
            prev_value = value

        if trend == 1 or trend == -1:
            solution += 1

    return solution


if __name__ == "__main__":
    print(f"Solution: {solution()}")
