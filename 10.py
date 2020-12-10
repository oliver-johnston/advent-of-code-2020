from collections import defaultdict

fp = open("input/10.txt")
adapters = [int(x) for x in fp.read().splitlines()]

laptop = max(adapters)+3
adapters.append(laptop)
adapters.append(0)

adapters.sort()

diffs = defaultdict(lambda: 0)
for i in range(0, len(adapters)-1):
    diff = adapters[i+1] - adapters[i]
    diffs[diff] += 1

print("Part 1: {}".format(diffs[1] * diffs[3]))

# contains the number of ways to get to each adapter
combinations = defaultdict(lambda: 0)
# there is only one way to start with the socket
combinations[0] = 1

for current_adapter in adapters[1:]:
    for previous_adapter in list(combinations.keys()):

        diff = current_adapter - previous_adapter

        # If the difference between adapters is less than or equal to 3 then it is possible to plug the
        # previous adapter into the current adapter. This means that every combination that allowed us
        # to get us to the previous adapter will also allow us to get us to the current adapter.
        if diff <= 3:
            combinations[current_adapter] += combinations[previous_adapter]

        # If the difference between the adapters is more than 3 then it is not possible to plug the
        # previous adapter into the current adapter. This means it is not possible to use that path
        # to get to the end so we discard it.
        if diff > 3:
            combinations.pop(previous_adapter)

print("Part 2: {}".format(combinations[laptop]))

