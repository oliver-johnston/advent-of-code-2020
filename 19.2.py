import re


def get_rule(rules, number):
    if number == 8:
        return "({r42})+".format(r42=get_rule(rules, 42))

    if number == 11:
        r42 = get_rule(rules, 42)
        r31 = get_rule(rules, 31)
        r11 = ""
        for _ in range(100):
            r11 = "({r42}{r11}{r31})?".format(r42=r42, r31=r31, r11=r11)
        return "{r42}{r11}{r31}".format(r42=r42, r31=r31, r11=r11)

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

    print("Part 2: {}".format(len([m for m in messages if re.match(rule, m)])))


if __name__ == "__main__":
    main()
