def count_trees(data, move_cols, move_rows):
    width = len(data[0])
    tree_count = 0
    row = 0
    col = 0

    while row < len(data):
        char = data[row][col % width]
        if char == "#":
            tree_count += 1

        row += move_rows
        col += move_cols

    return tree_count


fp = open("input/3.txt")
data = fp.read().splitlines()
print("Part 1: {}".format(count_trees(data, 3, 1)))


part_2 = count_trees(data, 1, 1)\
         * count_trees(data, 3, 1)\
         * count_trees(data, 5, 1)\
         * count_trees(data, 7, 1)\
         * count_trees(data, 1, 2)
print("Part 2: {}".format(part_2))

