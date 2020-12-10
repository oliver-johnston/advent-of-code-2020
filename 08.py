class Instruction:
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand


def execute_program(program):
    accumulator = 0
    i = 0
    visited = set()

    while i not in visited and i < len(program):
        visited.add(i)

        instruction = program[i]

        if instruction.operator == "acc":
            accumulator += instruction.operand
            i += 1
        elif instruction.operator == "jmp":
            i += instruction.operand
        elif instruction.operator == "nop":
            i += 1
        else:
            raise ValueError("Unknown operator: {}".format(instruction.operator))

    success = i >= len(program)
    return accumulator, success


def fix_program(program):

    for i in range(0, len(program)):

        instruction = program[i]

        program_copy = program.copy()
        if instruction.operator == "nop":
            program_copy[i] = Instruction("jmp", instruction.operand)
        elif instruction.operator == "jmp":
            program_copy[i] = Instruction("nop", instruction.operand)

        if execute_program(program_copy)[1]:
            return program_copy


fp = open("input/8.txt")
program = [Instruction(line[:3], int(line[3:])) for line in fp.read().splitlines()]

print("Part 1: {}".format(execute_program(program)))

program = fix_program(program)
print("Part 2: {}".format(execute_program(program)))
