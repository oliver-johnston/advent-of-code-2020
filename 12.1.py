import math

fp = open("input/12.txt")
instructions = [(x[0], int(x[1:])) for x in fp.read().splitlines()]

location = (0, 0, 0)

vectors = {
    "N": (0, 1, 0),
    "S": (0, -1, 0),
    "E": (1, 0, 0),
    "W": (-1, 0, 0),
    "L": (0, 0, 1),
    "R": (0, 0, -1)
}

for i in instructions:

    if i[0] in vectors:
        vector = vectors[i[0]]
        location = (location[0] + vector[0]*i[1], location[1] + vector[1]*i[1], location[2] + vector[2]*i[1])
    elif i[0] == "F":
        degrees = ((location[2] + 180) % 360) - 180
        radians = degrees * (math.pi / 180)
        x = math.cos(radians) * i[1]
        y = math.sin(radians) * i[1]
        location = (location[0] + x, location[1] + y, location[2])

manhattan = abs(location[0]) + abs(location[1])
print(manhattan)
