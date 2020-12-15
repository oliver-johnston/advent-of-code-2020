def get_last_in_sequence(data, iterations):
    last = {}

    for i in range(0, len(data) - 1):
        last[data[i]] = i

    for i in range(len(data), iterations):
        prev = data[-1]
        if prev in last:
            data.append(i - 1 - last[prev])
        else:
            data.append(0)
        last[prev] = i - 1

    return data[-1]


fp = open("input/15.txt")
data = [int(x) for x in fp.read().split(",")]

print("Part 1: ", get_last_in_sequence(data, 2020))
print("Part 2: ", get_last_in_sequence(data, 30000000))
