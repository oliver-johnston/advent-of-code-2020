def part_1(data_set):
    for i in data_set:
        match = 2020 - i
        if match in data_set:
            return match * i


def part_2(data_set):
    for i in data_set:
        for j in data_set:
            match = 2020 - i - j
            if match in data_set:
                return i * j * match


fp = open("input/1.txt")
data = fp.read().splitlines()

set = set([int(i) for i in data])

print("Part 1: {}".format(part_1(set)))
print("Part 2: {}".format(part_2(set)))
