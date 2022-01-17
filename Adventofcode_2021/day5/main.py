"""day 4 - advent of code"""
import collections
from collections import Counter
from typing import Tuple


def load_data_calculate_output(file_: str) -> int:
    "load the data, extract the coorinates and then calucalte output"
    # points: Counter[Tuple[int, int]] = collections.Counter()
    points = Counter()
    data = open(file_, "r").readlines()
    for line in data:
        line = line.strip()
        start, end = line.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[(x, y1)] += 1
    count = 0
    for i in points.most_common():
        dic, num = i
        if num > 1:
            count += 1
        else:
            break
    return count


def load_data_calculate_output2(file_: str) -> int:
    "load the data, extract the coorinates and then calucalte output"
    # points: Counter[Tuple[int, int]] = collections.Counter()
    points = Counter()
    data = open(file_, "r").readlines()
    for line in data:
        line = line.strip()
        start, end = line.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[(x, y1)] += 1
        else:
            if x1 < x2:
                x_d = 1
            else:
                x_d = -1
            if y1 < y2:
                y_d = 1
            else:
                y_d = -1
            x, y = x1, y1
            while (x, y) != (x2 + x_d, y2 + y_d):
                points[(x, y)] += 1
                x, y = x + x_d, y + y_d

    count2 = 0
    for i in points.most_common():
        dic, num = i
        if num > 1:
            count2 += 1
        else:
            break
    return count2


def main():
    # part 1
    count = load_data_calculate_output("input.txt")
    print(count)

    # part 2
    count2 = load_data_calculate_output2("input.txt")
    print(count2)


if __name__ == "__main__":
    main()
