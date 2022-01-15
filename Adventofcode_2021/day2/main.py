"""day 3 - advent of code"""


def read_data(file_: str) -> list:
    """read data from text file"""
    with open(file_, "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
    return data


def calculate_steps(data: list) -> int:
    """compute the horizantal and vertical movements"""
    count_h = 0
    count_v = 0
    for line in data:
        cmd, arg = line.split()
        arg = int(arg)
        if cmd == "up":
            count_v += arg
        elif cmd == "down":
            count_v -= arg
        else:
            count_h += arg
    return count_h, count_v


def calulcate_steps_with_aim(data: list) -> int:
    """here we modify the direction and add aim"""
    count_h = 0
    count_v = 0
    aim = 0
    for line in data:
        cmd, arg = line.split()
        arg = int(arg)
        if cmd == "down":
            aim += arg
        elif cmd == "up":
            aim -= arg
        else:
            count_h += arg
            count_v += arg * aim
    return count_h, count_v


def main():
    data = read_data("input.txt")

    # part 1
    count_h, count_v = calculate_steps(data)
    multi = count_h * count_v
    print(multi)

    # part 2
    count_h, count_v = calulcate_steps_with_aim(data)
    multi = count_h * count_v
    print(multi)


if __name__ == "__main__":
    main()
