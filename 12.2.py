fp = open("input/12.txt")
instructions = [(x[0], int(x[1:])) for x in fp.read().splitlines()]


def rotate_left(pos, angle):
    for i in range(0, int(angle / 90)):
        pos = (-pos[1], pos[0])
    return pos


def rotate_right(pos, angle):
    for i in range(0, int(angle / 90)):
        pos = (pos[1], -pos[0])
    return pos


ship = (0, 0)
waypoint = (10, 1)

waypoint_vectors = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0)
}

for i in instructions:

    if i[0] in waypoint_vectors:
        vector = waypoint_vectors[i[0]]
        waypoint = (waypoint[0] + vector[0]*i[1], waypoint[1] + vector[1]*i[1])
    elif i[0] == "L":
        waypoint = rotate_left(waypoint, i[1])
    elif i[0] == "R":
        waypoint = rotate_right(waypoint, i[1])
    elif i[0] == "F":
        x = waypoint[0] * i[1]
        y = waypoint[1] * i[1]
        ship = (ship[0] + x, ship[1] + y)

print(ship)
manhattan = abs(ship[0]) + abs(ship[1])
print(manhattan)
