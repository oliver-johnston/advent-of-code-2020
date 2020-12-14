import re


def build_or_mask(text):
    mask = 0
    for c in text:
        mask = mask << 1
        if c == '1':
            mask += 1
    return mask


def build_and_mask(text):
    mask = 0
    for c in text:
        mask = mask << 1
        if c != '0':
            mask += 1
    return mask


fp = open("input/14.txt")
data = fp.read().splitlines()

memory = {}

for instruction in data:

    if instruction.startswith("mask"):
        match = re.match("mask = (.*)", instruction)
        or_mask = build_or_mask(match.group(1))
        and_mask = build_and_mask(match.group(1))
    else:
        match = re.match("mem\[([0-9]+)\] = ([0-9]+)", instruction)
        address = int(match.group(1))
        value = int(match.group(2))

        memory[address] = value & and_mask | or_mask

print("Part 1: {}".format(sum(memory.values())))
