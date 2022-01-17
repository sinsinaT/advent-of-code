"""day 6 - advent of code"""

import collections


def read_data(file_: str) -> list:
    file = open(file_)
    data = file.read()
    data = data.split(",")
    return data


def counting_the_fish(data: list) -> int:
    """we count how many fish generated after 80 days"""
    # import pdb;
    # pdb.set_trace()
    new_data = []
    counts = len(data)
    days = 0
    while days < 80:
        for idx, num in enumerate(data):
            if num == 0:
                counts += 1
                num = 6
                data[idx] = num
                new_data.append(8)
            else:
                num = int(num) - 1
                data[idx] = num

        data.extend(new_data)
        new_data = []
        days += 1
    return counts


def counting_forever(data: list) -> int:
    """counting the fishes forever"""
    numbers = collections.Counter(int(s) for s in data)
    print(numbers)

    for _ in range(256):
        numbers2 = collections.Counter({6: numbers[0], 8: numbers[0]})
        for key, value in numbers.items():
            if key > 0:
                numbers2[key - 1] += value
        numbers = numbers2
        print(numbers)

        # numbers2.update({k - 1: v for k, v in numbers.items() if k > 0})
        # numbers = numbers2
    return sum(numbers.values())


def main():
    # part 1
    data = read_data("input.txt")
    counts = counting_the_fish(data)
    print(counts)

    # part 2
    counts2 = counting_forever(data)
    print(counts2)


if __name__ == "__main__":
    main()
