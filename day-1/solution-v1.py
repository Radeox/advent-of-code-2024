import math


def solution():
    left = []
    right = []
    data = []

    with open("input.txt") as f:
        lines = f.readlines()

        # Add all lines the corresponding list
        c = len(lines)
        for line in lines:
            left.append(int(line.split()[0]))
            right.append(int(line.split()[1]))

        for _ in range(c):
            # Smallest element of each list (bigger than last time)
            left_smallest = min(left)
            right_smallest = min(right)

            # Make absolute difference between indexes
            data.append(abs(left_smallest - right_smallest))

            # Index of smallest element
            left_index = left.index(left_smallest)
            right_index = right.index(right_smallest)

            # Remove from in list
            left[left_index] = math.inf
            right[right_index] = math.inf

        return sum(data)


if __name__ == "__main__":
    print(f"Solution: {solution()}")
