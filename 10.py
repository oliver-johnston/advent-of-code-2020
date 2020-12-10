from collections import defaultdict

fp = open("input/10.txt")
data = [int(x) for x in fp.read().splitlines()]

data.append(max(data)+3)
data.append(0)

data.sort()


diffs = defaultdict(lambda: 0)
for i in range(0, len(data)-1):
    diff = data[i+1] - data[i]
    diffs[diff] += 1

print("Part 1: {}".format(diffs[1] * diffs[3]))

seqs = defaultdict(lambda: 0)

for x in data:

    if len(seqs) == 0:
        seqs[x] = 1
    else:
        for y in list(seqs.keys()):
            diff = x - y
            if diff <= 3:
                seqs[x] += seqs[y]
            if diff >= 3:
                seqs.pop(y)

print("Part 2: {}".format(sum(seqs.values())))

