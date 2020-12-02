import os


main_dir = os.getcwd()


def product_of_sum_2020(file):
    with open(file, "r") as f:
        rows = [int(line.rstrip()) for line in f]
        for r in rows:
            for i in rows:
                if r + i == 2020:
                    print(r, i)
                    return r * i


if __name__ == "__main__":
    input_file = os.path.join(main_dir, "input.txt")
    result = product_of_sum_2020(input_file)
    print(result)
    # 1020036