"""day 3 - advent of code"""


def read_data(file_: str) -> list:
    with open(file_, "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
    return data


def calculate_gamma_number(data: list) -> int:
    # import pdb;pdb.set_trace()
    final_binary = []
    trace = []
    for j in range(0, 5):
        for i in data:
            track = int(i[j])
            trace.append(track)
            continue
        most_common = max(trace, key=trace.count)
        trace = []
        final_binary.append(most_common)
        gamma_rate = int("".join(str(i) for i in final_binary), 2)

    return gamma_rate


def calculate_epsilon_number(data: list) -> int:
    # import pdb;pdb.set_trace()
    final_binary = []
    trace = []
    for j in range(0, 5):
        for i in data:
            track = int(i[j])
            trace.append(track)
            continue
        min_common = min(trace, key=trace.count)
        trace = []
        final_binary.append(min_common)
        epsilon_rate = int("".join(str(i) for i in final_binary), 2)

    return epsilon_rate


def discard_data_based_on_most_common(data: list, common: int, j: iter) -> list:
    # import pdb;pdb.set_trace()
    new_list = []
    for line in data:
        if line[j] == str(common):
            new_list.append(line)
    return new_list


def calculate_oxygen_rate(data: list) -> int:
    trace = []
    for j in range(0, 12):
        for i in data:
            track = int(i[j])
            trace.append(track)
            continue
        most_common = max(trace, key=trace.count)
        least_common = min(trace, key=trace.count)
        if most_common == least_common:
            most_common = 1
        trace = []
        new_list = discard_data_based_on_most_common(data, most_common, j)
        data = new_list
    o2_gen_rating = int("".join(str(i) for i in data), 2)
    return o2_gen_rating


def calculate_co2_rate(data: list) -> int:
    trace = []
    for j in range(0, 12):
        for i in data:
            track = int(i[j])
            trace.append(track)
            continue
        most_common = max(set(trace), key=trace.count)
        least_common = min(set(trace), key=trace.count)

        if most_common == least_common:
            least_common = 0
        if len(trace) == 1:
            break
        trace = []
        new_list = discard_data_based_on_most_common(data, least_common, j)
        data = new_list
    CO2_scrub_rating = int("".join(str(i) for i in data), 2)
    return CO2_scrub_rating


def main():
    """solve the puzzle of decoding binary to decimal numbers"""
    data = read_data("input.txt")
    print(data)

    # part 1
    gamma_rate = calculate_gamma_number(data)
    epsilon_rate = calculate_epsilon_number(data)
    power_consumption = gamma_rate * epsilon_rate
    print(power_consumption)

    # part 2
    o2_gen_rating = calculate_oxygen_rate(data)
    CO2_scrub_rating = calculate_co2_rate(data)
    life_support = o2_gen_rating * CO2_scrub_rating
    print(life_support)


if __name__ == "__main__":
    main()
