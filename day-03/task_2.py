import os
from math import ceil
from functools import reduce


main_dir = os.getcwd()


def count_trees(file, right, down):
    with open(file, "r") as f:
        rows = [line.rstrip() for line in f.readlines()]
        len_rows = len(rows)
        max_idx_right = ceil((len_rows * right)/len(rows[0]))
        rows = [row * max_idx_right for row in rows]
        start_right = 0
        start_down = 0
        count = 0
        while start_down < len_rows:
            if rows[start_down][start_right] == "#":
                count += 1
            start_right += right
            start_down += down
        return count


if __name__ == "__main__":
    input_file = os.path.join(main_dir, "input.txt")
    tree_counts = []
    for r, d in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2]):
        tree_counts.append(count_trees(input_file, r, d))    
    result = reduce((lambda x, y: x * y), tree_counts)
    print(result)
    # 1115775000