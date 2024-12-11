def solution():
    blinks = 75
    memory = {}

    with open("input.txt") as f:
        stones = [int(c) for c in list(f.read().strip().split(" "))]

    # Memory initialization
    for stone in stones:
        if stone in memory:
            memory[stone] += 1
        else:
            memory[stone] = 1

    i = 0
    while i < blinks:
        snap = memory.copy()
        for s in snap:
            occurrences = snap[s]

            if occurrences <= 0:
                continue

            # Remove 1 stone from memory
            memory[s] -= occurrences

            if s == 0:
                if 1 in memory:
                    memory[1] += occurrences
                else:
                    memory[1] = occurrences
            elif len(str(s)) % 2 == 0:
                first_half = int(str(s)[: len(str(s)) // 2])
                second_half = int(str(s)[len(str(s)) // 2 :])

                if first_half in memory:
                    memory[first_half] += occurrences
                else:
                    memory[first_half] = occurrences

                if second_half in memory:
                    memory[second_half] += occurrences
                else:
                    memory[second_half] = occurrences
            else:
                x = s * 2024
                if x in memory:
                    memory[x] += occurrences
                else:
                    memory[x] = occurrences

        i += 1

        # Cleanup memory
        new_memory = memory.copy()
        for m in memory:
            if memory[m] <= 0:
                new_memory.pop(m)
        memory = new_memory

        stones = 0
        for d in memory:
            if memory[d] > 0:
                stones += memory[d]

    return sum(memory.values())


if __name__ == "__main__":
    print(f"Solution: {solution()}")
