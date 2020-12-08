def execute_program(program):
    accumulator = 0
    i = 0
    visited = set()

    while True:
        if i in visited:
            return accumulator, False

        if i >= len(program):
            return accumulator, True

        visited.add(i)

        instruction = program[i].split(" ")
        operator = instruction[0]
        operand = int(instruction[1])

        if operator == "acc":
            accumulator += operand
            i += 1
        elif operator == "jmp":
            i += operand
        elif operator == "nop":
            i += 1
        else:
            raise ValueError("Unknown operator: {}".format(operator))


def flip_instruction(instruction):
    if instruction.startswith("nop"):
        return instruction.replace("nop", "jmp")
    else:
        return instruction.replace("jmp", "nop")


def fix_program(program):
    for i in range(0, len(program)):
        if program[i].startswith("nop") or program[i].startswith("jmp"):
            program[i] = flip_instruction(program[i])
            if execute_program(program)[1]:
                return program
            program[i] = flip_instruction(program[i])


fp = open("input/8.txt")
program = fp.read().splitlines()

print("Part 1: {}".format(execute_program(program)))

program = fix_program(program)
print("Part 2: {}".format(execute_program(program)))
