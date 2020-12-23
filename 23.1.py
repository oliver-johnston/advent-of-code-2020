def play_round(cups):

    current_cup = cups.pop(0)
    pick_up = [cups.pop(0) for _ in range(3)]
    destination = current_cup - 1
    while destination not in cups:
        destination = (destination - 1) % 10

    index = cups.index(destination)

    for cup in reversed(pick_up):
        cups.insert(index+1, cup)

    cups.append(current_cup)


def get_result(cups):

    result = ""
    index = cups.index(1)
    for i in range(len(cups) - 1):
        result += str(cups[(index + i + 1) % len(cups)])

    return result


def main():

    cups = [int(x) for x in "962713854"]
    cups = cups

    for i in range(100):
        play_round(cups)

    print("Part 1: {}".format(get_result(cups)))


if __name__ == "__main__":
    main()
