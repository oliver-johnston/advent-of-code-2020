import re


def get_rule(rules, number):
    parts = rules[number]

    rule = ""
    for part in parts:
        if part == "|":
            rule += "|"
        elif re.match("\"[a-z]\"", part):
            rule += part[1]
        else:
            rule += get_rule(rules, int(part))

    if "|" in rule:
        rule = "(" + rule + ")"

    return rule


def main():
    data = open("input/19.txt").read().split("\n\n")

    rules = data[0].splitlines()
    unparsed = dict()
    for r in rules:
        split = r.split(": ")
        unparsed[int(split[0])] = split[1].split(" ")

    rule = "^" + get_rule(unparsed, 0) + "$"
    print(rule)

    messages = data[1].splitlines()

    print("Part 1: {}".format(len([m for m in messages if re.match(rule, m)])))


if __name__ == "__main__":
    main()
