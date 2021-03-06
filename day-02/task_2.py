import os
import re


main_dir = os.getcwd()


def count_valid_pws(file):
    with open(file, "r") as f:
        count = 0
        rows = [re.split("-| |: | ", line.rstrip()) for line in f.readlines()]
        for row in rows:
            pos1, pos2 = [int(i) - 1 for i in row[:2]]
            char, pw = row[2:]
            count_chars = (pw[pos1] + pw[pos2]).count(char)
            if count_chars == 1:
                count += 1
            else:
                continue
        return count


if __name__ == "__main__":
    sum_valid_pws = count_valid_pws(os.path.join(main_dir, "input.txt"))
    print(f"Sum of valid passwords: {sum_valid_pws}")
    # 294