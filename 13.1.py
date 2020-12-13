fp = open("input/13.txt")
data = fp.read().splitlines()

time = int(data[0])
buses = [int(x) for x in data[1].split(',') if x != 'x']

next_bus = [(bus, (int(time / bus) * bus) + bus) for bus in buses]
next_bus.sort(key=lambda x: x[1])

first_bus = next_bus[0]
print("Part 1: {}".format(first_bus[0] * (first_bus[1] - time)))