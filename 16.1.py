from functools import reduce

def get_fields(input):
    fields = {}
    for line in input.split("\n"):
        split = line.split(": ")
        name = split[0]
        ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in split[1].split(" or ")]
        fields[name] = ranges
    return fields


def get_tickets(input):
    return [[int(y) for y in x.split(",")] for x in input.split("\n")[1:]]


def is_within_range(value, ranges):
    return any(r[0] <= value <= r[1] for r in ranges)


def get_invalid_values(ticket, fields):
    return [value for value in ticket if not any(is_within_range(value, ranges) for ranges in fields.values())]


def main():
    fp = open("input/16.txt")
    data = fp.read().split("\n\n")

    fields = get_fields(data[0])
    my_ticket = get_tickets(data[1])[0]
    other_tickets = get_tickets(data[2])

    invalid_values = reduce(list.__add__, [get_invalid_values(ticket, fields) for ticket in other_tickets])

    print(sum(invalid_values))


if __name__ == "__main__":
    main()
