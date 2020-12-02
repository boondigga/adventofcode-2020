import os


main_dir = os.getcwd()


def product_of_sum_2020(file):
    with open(file, "r") as f:
        rows = [int(line.rstrip()) for line in f]
        for r in rows:
            for i in rows:
                for x in rows:
                    if r + i + x == 2020:
                        return r * i * x


if __name__ == "__main__":
    input_file = os.path.join(main_dir, "input.txt")
    result = product_of_sum_2020(input_file)
    print(result)
    # 286977330