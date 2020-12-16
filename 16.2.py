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


def is_within_field_range(value, ranges):
    return any(r[0] <= value <= r[1] for r in ranges)


def is_valid_for_any_field(value, fields):
    return any(is_within_field_range(value, fields[f]) for f in fields)


def is_valid(ticket, fields):
    return all(is_valid_for_any_field(value, fields) for value in ticket)


def get_field_indices(fields, tickets):
    indices = {}

    all_indices = range(len(fields))
    for f in fields:
        indices[f] = [i for i in all_indices if all(is_within_field_range(ticket[i], fields[f]) for ticket in tickets)]

    while any(len(x) > 1 for x in indices.values()):
        exact_matches = set([i[0] for i in list(indices.values()) if len(i) == 1])

        for f in fields:
            if len(indices[f]) > 1:
                indices[f] = list(set(indices[f]) - exact_matches)

    return dict((f, indices[f][0]) for f in fields)


def main():
    fp = open("input/16.txt")
    data = fp.read().split("\n\n")

    fields = get_fields(data[0])
    my_ticket = get_tickets(data[1])[0]
    valid_tickets = [ticket for ticket in get_tickets(data[2]) if is_valid(ticket, fields)]

    field_indices = get_field_indices(fields, valid_tickets)
    print(field_indices)

    departure_fields = [k for k in fields.keys() if k.startswith("departure")]
    departure_values = [my_ticket[field_indices[field]] for field in departure_fields]

    print(departure_values)
    print(reduce(lambda x, y: x * y, departure_values, 1))


if __name__ == "__main__":
    main()
