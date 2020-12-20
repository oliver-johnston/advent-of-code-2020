import re
from functools import reduce


class Tile:
    def __init__(self, id, grid):
        self.id = id
        self.grid = grid

    def get_top(self):
        return self.grid[0]

    def get_bottom(self):
        return self.grid[-1]

    def get_left(self):
        return [x[0] for x in self.grid]

    def get_right(self):
        return [x[-1] for x in self.grid]

    def get_edges(self):
        return [self.get_top(), self.get_bottom(), self.get_left(), self.get_right()]


def parse_tile(input):
    lines = input.splitlines()
    id = int(re.match("Tile ([0-9]+):", lines[0]).group(1))
    data = [[c == "#" for c in l] for l in lines[1:]]
    return Tile(id, data)


def is_match(edge1, edge2):
    return edge1 == edge2 or list(reversed(edge1)) == edge2


def is_neighbour(tile1, tile2):
    return tile1.id != tile2.id and any([e1 for e1 in tile1.get_edges() if any([e2 for e2 in tile2.get_edges() if is_match(e1, e2)])])


def get_neighbours(t, tiles):
    return [n for n in tiles if is_neighbour(n, t)]


def main():
    data = open("input/20.txt").read().split("\n\n")

    tiles = [parse_tile(x) for x in data]

    corners = [t for t in tiles if len(get_neighbours(t, tiles)) == 2]
    print("Part 1: {}".format(reduce(lambda acc, tile: acc * tile.id, corners, 1)))


if __name__ == "__main__":
    main()
