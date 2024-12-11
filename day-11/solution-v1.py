def solution():
    stones = []
    blinks = 25

    with open("input.txt") as f:
        stones = [int(c) for c in list(f.read().strip().split(" "))]

    for _ in range(blinks):
        new_stones = []

        for stone in stones:
            stone_str = str(stone)

            # If stone equals 0 turns into 1
            if stone == 0:
                new_stones.append(1)
            # If stone have even number of digits split it into two stones
            elif len(stone_str) % 2 == 0:
                first_half = int(stone_str[: len(stone_str) // 2])
                second_half = int(stone_str[len(stone_str) // 2 :])

                new_stones.append(first_half)
                new_stones.append(second_half)
            # Else it get multiplied by 2024
            else:
                new_stones.append(stone * 2024)

        stones = new_stones

    return len(stones)


if __name__ == "__main__":
    print(f"Solution: {solution()}")
