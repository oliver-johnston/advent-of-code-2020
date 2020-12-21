import re
from functools import reduce


def parse_line(line):
    match = re.match("(.*) \(contains (.*)\)", line)
    ingredients = match.group(1).split(" ")
    allergens = match.group(2).split(", ")
    return ingredients, allergens


def main():
    data = open("input/21.txt").read().split("\n")

    lines = [parse_line(x) for x in data]

    all_allergens = set(reduce(list.__add__, [x[1] for x in lines]))
    all_ingredients = set(reduce(list.__add__, [x[0] for x in lines]))

    allergens = {}

    while any(all_allergens):
        for allergen in list(all_allergens):
            ingredients = [x[0] for x in lines if allergen in x[1]]
            possibilities = set(ingredients[0])
            for x in ingredients[1:]:
                possibilities = possibilities.intersection(x)

            if len(possibilities) == 1:
                ingredient = possibilities.pop()
                allergens[allergen] = ingredient
                all_allergens.remove(allergen)
                for x in lines:
                    if ingredient in x[0]:
                        x[0].remove(ingredient)

    for i in allergens.values():
        all_ingredients.remove(i)

    count = len(reduce(list.__add__, [x[0] for x in lines]))

    print("Part 1: {}".format(count))

    print(",".join([allergens[a] for a in sorted(allergens.keys())]))


if __name__ == "__main__":
    main()
