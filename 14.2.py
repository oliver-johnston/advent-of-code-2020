import re


def get_addresses(address, mask):
    addresses = [0]
    for i in range(0, len(mask)):
        c = mask[len(mask) - i - 1]
        bit = address & 1
        address = address >> 1
        if c == '0':
            addresses = [(bit << i) + a for a in addresses]
        elif c == '1':
            addresses = [(1 << i) + a for a in addresses]
        elif c == 'X':
            addresses = [(1 << i) + a for a in addresses] + [a for a in addresses]

    return addresses


fp = open("input/14.txt")
data = fp.read().splitlines()

memory = {}

for instruction in data:

    if instruction.startswith("mask"):
        mask = instruction.split(" = ")[-1]
    else:
        match = re.match("mem\[([0-9]+)\] = ([0-9]+)", instruction)
        address = int(match.group(1))
        value = int(match.group(2))

        addresses = get_addresses(address, mask)

        for a in addresses:
            memory[a] = value

print("Part 1: {}".format(sum(memory.values())))
