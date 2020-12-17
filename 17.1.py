from functools import reduce


def parse(input):
    active = set()
    for i in range(len(input)):
        row = input[i]
        for j in range(len(row)):
            if row[j] == '#':
                active.add((0, i, j))

    return active


def get_neighbours(cell):
    neighbours = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if not (x == 0 and y == 0 and z == 0):
                    neighbours.append((cell[0] + x, cell[1] + y, cell[2] + z))
    return neighbours


def is_active(cell, active):
    neighbours = set(get_neighbours(cell))
    active_neighbours = neighbours.intersection(active)

    if cell in active:
        return 2 <= len(active_neighbours) <= 3
    else:
        return len(active_neighbours) == 3


def get_active(active):
    all_cells = set(reduce(list.__add__, [get_neighbours(c) for c in active]))
    return set([c for c in all_cells if is_active(c, active)])


def run(active, iterations):
    for _ in range(iterations):
        active = get_active(active)
    return active


def main():
    active = parse(open("input/17.txt").read().splitlines())
    print(len(run(active, 6)))


if __name__ == "__main__":
    main()
