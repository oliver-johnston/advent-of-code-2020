import re


def is_valid_part_1(min, max, char, password):
    chars = [c for c in password if c == char]
    return min <= len(chars) <= max


def is_valid_part_2(i1, i2, char, password):
    return (password[i1 - 1] == char) != (password[i2 - 1] == char)


fp = open("input/2.txt")
data = fp.read().splitlines()

valid_part_1 = 0
valid_part_2 = 0


for line in data:
    match = re.match("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", line)
    min = int(match.group(1))
    max = int(match.group(2))
    char = match.group(3)
    password = match.group(4)

    if is_valid_part_1(min, max, char, password):
        valid_part_1 += 1

    if is_valid_part_2(min, max, char, password):
        valid_part_2 += 1

print("Part 1: {}".format(valid_part_1))
print("Part 2: {}".format(valid_part_2))
