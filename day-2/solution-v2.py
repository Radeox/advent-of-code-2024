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
        tmp = level.copy()

        if compute_safeness(tmp):
            solution += 1
        else:
            # Try brute forcing all levels excluding one element
            tmp_levels = []

            for i in range(len(level)):
                tmp = level.copy()
                tmp.pop(i)
                tmp_levels.append(tmp)

            valid = False
            for tmp in tmp_levels:
                if compute_safeness(tmp):
                    valid = True
                    break

            if valid:
                solution += 1

    return solution


def compute_safeness(level):
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
        return True
    else:
        return False


if __name__ == "__main__":
    print(f"Solution: {solution()}")
