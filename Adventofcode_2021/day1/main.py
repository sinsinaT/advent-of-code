"""advent of code - day 1"""

from typing import TYPE_CHECKING


def load_data(file_: str) -> list:
    """read the data from text"""
    with open(file_, "r") as f:
        data = f.readlines()
        data = [int(line.strip()) for line in data]
    return data


def calculate_increase_step(data: list) -> int:
    """part1-calculate the step in increase"""

    counter = 0
    prev = data[0]
    for i in data[1:]:
        if i > prev:
            counter += 1
        prev = i
    return counter


def calculate_three_measurement_sum(data: list) -> int:
    """part 2 - compute the steps considering three measurements"""
    counter = 0
    prev = data[0]
    for i in range(
        3, len(data)
    ):  # sliding window: instread of summing all slides, we compare the first and the fourth element as the the 2 number are shared with each other
        if data[i] > prev:
            counter += 1
        prev = data[i - 2]
    return counter


def main():
    """the main body of function"""
    data = load_data("input.txt")
    # part 1
    count = calculate_increase_step(data)
    print(count)

    # part 2
    counter = calculate_three_measurement_sum(data)
    print(counter)


if __name__ == "__main__":
    main()
