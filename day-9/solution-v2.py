def solution():
    solution = 0
    disk = []

    with open("input.txt") as f:
        disk_map = f.readline().strip()

    id = 0
    checking_free = False
    disk_usage = {}
    disk_order = []
    disk_position = {}

    # Recosturct the disk
    for bit in disk_map:
        if not checking_free:
            for i in range(int(bit)):
                disk.append(id)

            # Keep track of each file size
            disk_usage[id] = int(bit)
            disk_order.append(id)
            disk_position[id] = len(disk) - int(bit)

            checking_free = True
            id += 1
        else:
            for _ in range(int(bit)):
                disk.append(".")
            checking_free = False

    # Compact disk from right to left (prevent fragmentation)
    disk_order.reverse()
    for file in disk_order:
        space_needed = disk_usage[file]

        for i in range(len(disk)):
            if disk[i] == ".":
                free_space = 0
                # Check how much free space is available
                for j in range(i, len(disk)):
                    if disk[j] == ".":
                        free_space += 1
                    else:
                        break

                # Find file in disk
                p = disk_position[file]

                if i > p:
                    break

                # Check if we have enough space to move the file
                if free_space >= space_needed:
                    # Move the file
                    for k in range(len(disk)):
                        if disk[k] == file:
                            disk[k] = "."

                    for j in range(i, i + space_needed):
                        disk[j] = file
                    break

    # Compute checksum
    pos = 0
    for i in range(len(disk) - 1):
        if disk[i] != ".":
            solution += pos * int(disk[i])
        pos += 1

    return solution


if __name__ == "__main__":
    print(f"Solution: {solution()}")
