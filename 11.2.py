def is_occupied(seats, i, j):
    return seats[i][j] == "#"


def is_seat(seats, i, j):
    return seats[i][j] == "#" or seats[i][j] == "L"


def count_occupied(seats, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                row_i = row+i
                col_j = col+j
                while 0 <= row_i < len(seats) and 0 <= col_j < len(seats[row_i]) and not is_seat(seats, row_i, col_j):
                    row_i += i
                    col_j += j
                count += 0 <= row_i < len(seats) and 0 <= col_j < len(seats[row_i]) and is_occupied(seats, row_i, col_j)
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
            elif cur == "#" and occupied >= 5:
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


print("Part 2: {}".format(sum([len([y for y in x if y == "#"]) for x in cur])))
