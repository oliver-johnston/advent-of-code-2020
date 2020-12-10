import math


def binary_search(code, max, left_char):
    min = 0

    for c in code:
        if c == left_char:
            max = math.floor((min + max) / 2)
        else:
            min = math.ceil((min + max) / 2)

    return min


def get_id(code):
    row = binary_search(code[0:7], 127, "F")
    col = binary_search(code[-3:], 7, "L")

    return row * 8 + col


def get_missing(ids):
    ids.sort()
    expected = ids[0]
    for x in ids:
        if x != expected:
            return expected
        expected += 1


fp = open("input/5.txt")
data = fp.read().splitlines()

ids = [get_id(x) for x in data]

print("Part 1: {}".format(max(ids)))
print("Part 2: {}".format(get_missing(ids)))
