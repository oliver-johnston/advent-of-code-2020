fp = open("1.txt")
data = fp.read().splitlines()

set = set([int(i) for i in data])

# part 1
for i in set:
    match = 2020 - i;
    if match in set:
        print(i * match)

# part 2
for i in set:
    for j in set:
        match = 2020 - i - j;
        if match in set:
            print(i * j * match)