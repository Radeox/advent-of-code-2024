def solution():
    solution = 0
    rules = {}
    updates = []

    with open("input.txt") as f:
        lines = f.readlines()

    # Parse the input
    rule_processing = True
    while lines:
        line = lines.pop(0).strip()

        if line == "":
            rule_processing = False
            continue

        if rule_processing:
            page1, page2 = line.split("|")
            page1 = int(page1)
            page2 = int(page2)

            if not page1 in rules:
                rules[page1] = []
            rules[page1].append(page2)
        else:
            u = [int(n) for n in line.split(",")]
            updates.append(u)

    # Validate updates
    valid_updates = []
    invalid_updates = []

    while updates:
        update = updates.pop(0)
        valid, u = validate_update(update, rules)

        if valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(u)

    valid_updates = []
    while invalid_updates:
        update = invalid_updates.pop(0)
        valid, u = validate_update(update, rules)

        if valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(u)

    # Add middle page for each valid update
    for update in valid_updates:
        solution += update[len(update) // 2]

    return solution


def validate_update(update, rules):
    valid = True

    for i, page in enumerate(update):
        # Check pages before the current page
        for j in range(i, -1, -1):
            if page not in rules:
                continue

            if update[j] in rules[page]:
                valid = False

                # Swap the pages and reinsert the update
                update[j], update[i] = update[i], update[j]
                break

        if not valid:
            return False, update

    return valid, update


if __name__ == "__main__":
    print(f"Solution: {solution()}")
