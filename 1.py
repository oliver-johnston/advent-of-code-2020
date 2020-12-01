fp = open("1.txt")
data = fp.read().splitlines()

set = set([int(i) for i in data])

for i in set:
    match = 2020 - i;
    if match in set:
        print(i * match)

