def get_answers(group, combine):
    answers = group.split("\n")
    result = set(answers[0])
    for a in answers[1:]:
        result = combine(result, set(a))
    return result


def count_part_1(group):
    return len(get_answers(group, lambda a, b: a.union(b)))


def count_part_2(group):
    return len(get_answers(group, lambda a, b: a.intersection(b)))


fp = open("input/6.txt")
data = fp.read()

groups = data.split("\n\n")

print("Part 1: {}".format(sum([count_part_1(x) for x in groups])))
print("Part 2: {}".format(sum([count_part_2(x) for x in groups])))
