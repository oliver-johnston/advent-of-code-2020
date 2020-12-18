from pyparsing import nestedExpr


def solve_nested(parts):
    if len(parts) == 1:
        if type(parts[0]) is list:
            return solve_nested(parts[0])
        else:
            return int(parts[0])

    left = solve_nested(parts[0:-2])
    operator = parts[-2]
    right = solve_nested(parts[-1:])

    if operator == "+":
        return left + right
    elif operator == "*":
        return left * right


def solve(equation):
    parts = nestedExpr("(", ")").parseString("(" + equation + ")").asList()
    return solve_nested(parts)


def main():
    equations = open("input/18.txt").read().splitlines()
    print(sum([solve(e) for e in equations]))


if __name__ == "__main__":
    main()
