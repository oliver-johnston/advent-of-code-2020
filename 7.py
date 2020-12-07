import re


def parse_contains(x):
    if x == "no other bags":
        return None
    match = re.match("([0-9]+) (.+) bag(s?)", x)
    return match.group(2), int(match.group(1))


def parse_line(line):
    match = re.match("(.+) bags contain (.+).", line)
    color = match.group(1)
    contains = [parse_contains(x) for x in match.group(2).split(", ")]

    return color, contains


def can_hold(outerColor, innerColor, bags):
    contains = bags[outerColor]

    for x in [y for y in contains if y is not None]:
        if x[0] == innerColor or can_hold(x[0], innerColor, bags):
            return True

    return False


def count_sub_bags(color, bags):
    contains = bags[color]
    return sum([count_sub_bags(x[0], bags) * x[1] for x in contains if x is not None]) + 1


fp = open("input/7.txt")
data = fp.read().splitlines()

bags = dict([parse_line(x) for x in data])

print("Part 1: {}".format(len([x for x in bags if can_hold(x, "shiny gold", bags)])))
print("Part 2: {}".format(count_sub_bags("shiny gold", bags) - 1))
