import os
from math import ceil


main_dir = os.getcwd()


def count_trees(file):
    with open(file, "r") as f:
        rows = [line.rstrip() for line in f.readlines()]
        len_rows = len(rows)
        max_idx_right = ceil((len_rows * 3)/len(rows[0]))
        rows = [row * max_idx_right for row in rows]
        right = 0
        down = 0
        count = 0
        while down < len_rows:
            if rows[down][right] == "#":
                count += 1
            right += 3
            down += 1
        return count

if __name__ == "__main__":
    input_file = os.path.join(main_dir, "input.txt")
    result = count_trees(input_file)
    print(result)
    # 225