def solution():
    solution = 0
    disk = []

    with open("example.txt") as f:
        disk_map = f.readline().strip()

    id = 0
    checking_free = False
    disk_usage = {}

    # Recosturct the disk
    for bit in disk_map:
        if not checking_free:
            for i in range(int(bit)):
                disk.append(id)

            # Keep track of each file size
            disk_usage[id] = int(bit)

            checking_free = True
            id += 1
        else:
            for _ in range(int(bit)):
                disk.append(".")
            checking_free = False

    for i in range(len(disk)):
        print(disk[i], end="")
    print()

    # Compact disk from right to left (prevent fragmentation)
    for i in range(len(disk)):
        # Skip
        if disk[i] != ".":
            continue
        else:
            index = i
            free_space = 0
            for i in range(i, len(disk)):
                if disk[i] == ".":
                    free_space += 1
                else:
                    break

            # Search for biggest file that can fit in the free space
            to_move = -1
            for file in range(len(disk_usage) - 1, -1, -1):
                if disk_usage[file] <= free_space:
                    to_move = file
                    break

            for j in range(len(disk) - 1, index, -1):
                if disk[j] == to_move:
                    disk[index] = to_move
                    disk[j] = "."
                    free_space -= 1
                    break

            # for j in range(len(disk) - 1, index, -1):
            #     if disk[j] != ".":
            #         if disk_usage[disk[j]] <= free_space:
            #             disk[index] = disk[j]
            #             disk[j] = "."
            #             free_space -= disk_usage[disk[index]]
            #             break

    for i in range(len(disk)):
        print(disk[i], end="")
    print()

    # Compute checksum
    id = 0
    for i in range(len(disk) - 1):
        if disk[i] != ".":
            solution += id * int(disk[i])
            id += 1

    return solution


if __name__ == "__main__":
    print(f"Solution: {solution()}")
