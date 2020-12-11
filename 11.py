def is_occupied(seats, i, j):
    if i < 0 or i >= len(seats):
        return False

    row = seats[i]
    if j < 0 or j >= len(row):
        return False

    return row[j] == "#"


def count_occupied(seats, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                count += is_occupied(seats, i+row, j+col)
    return count


def get_next_state(seats):
    new_seats = []
    for i in range(0, len(seats)):
        row = seats[i]
        new_row = []
        new_seats.append(new_row)

        for j in range(0, len(row)):
            cur = row[j]
            occupied = count_occupied(seats, i, j)
            next = cur
            if cur == "L" and occupied == 0:
                next = "#"
            elif cur == "#" and occupied >= 4:
                next = "L"
            new_row.append(next)
    return new_seats


def equals(seats1, seats2):
    for i in range(0, len(seats1)):
        row1 = seats1[i]
        row2 = seats2[i]
        for j in range(0, len(row1)):
            if row1[j] != row2[j]:
                return False
    return True


fp = open("input/11.txt")
data = fp.read().splitlines()

cur = data
next = get_next_state(cur)
while not equals(cur, next):
    cur = next
    next = get_next_state(cur)


print("Part 1: {}".format(sum([len([y for y in x if y == "#"]) for x in cur])))
