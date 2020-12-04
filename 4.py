import re

required_fields = {
    "byr": lambda x: re.match("^[0-9]{4}$", x) and 1920 <= int(x) <= 2002,
    "iyr": lambda x: re.match("^[0-9]{4}$", x) and 2010 <= int(x) <= 2020,
    "eyr": lambda x: re.match("^[0-9]{4}$", x) and 2020 <= int(x) <= 2030,
    "hgt": lambda x: is_height_valid(x),
    "hcl": lambda x: re.match("^#[0-9a-f]{6}$", x),
    "ecl": lambda x: re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", x),
    "pid": lambda x: re.match("^[0-9]{9}$", x)
}


def is_valid_part_1(passport):
    fields = re.split("\n| ", passport)
    keys = set([x.split(":")[0] for x in fields])
    is_valid = all([r in keys for r in required_fields])
    return is_valid


def is_height_valid(height):

    cms = re.match("^([0-9]+)cm$", height)
    ins = re.match("^([0-9]+)in$", height)

    return (cms and 150 <= int(cms.group(1)) <= 193) or (ins and 59 <= int(ins.group(1)) <= 76)


def is_valid_part_2(passport):
    if not is_valid_part_1(passport):
        return False

    fields = re.split("\n| ", passport)
    key_values = set([(x.split(":")[0], x.split(":")[1]) for x in fields])

    for kv in key_values:
        if kv[0] in required_fields and not (required_fields[kv[0]](kv[1])):
            return False

    return True


fp = open("input/4.txt")
data = fp.read()

passports = data.split("\n\n")

print("Part 1: {}".format(len([p for p in passports if is_valid_part_1(p)])))
print("Part 2: {}".format(len([p for p in passports if is_valid_part_2(p)])))
