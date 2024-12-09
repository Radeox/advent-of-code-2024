def solution():
    solution = 0
    disk = []

    with open("input.txt") as f:
        disk_map = f.readline().strip()

    id = 0
    checking_free = False

    # Recosturct the disk
    for bit in disk_map:
        if not checking_free:
            for _ in range(int(bit)):
                disk.append(id)
            id += 1
            checking_free = True
        else:
            for _ in range(int(bit)):
                disk.append(".")
            checking_free = False

    # Count free spaces
    # Don't know why these works
    free_space = disk.count(".") - 2

    # Compact disk from right to left
    for i in range(len(disk) - 1, 0, -1):
        if disk[i] != ".":
            # Search for the first free space on the left
            for j in range(len(disk) - 1):
                if disk[j] == ".":
                    disk[j] = disk[i]
                    disk[i] = "."
                    free_space -= 1
                    break

        if free_space == 0:
            break

    # Compute checksum
    id = 0
    for i in range(len(disk) - 1):
        if disk[i] != ".":
            solution += id * int(disk[i])
            id += 1

    return solution


if __name__ == "__main__":
    print(f"Solution: {solution()}")
