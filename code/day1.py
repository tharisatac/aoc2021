def read_input():
    """ Read input file """
    with open("inputs/day1.txt") as f:
        lines = f.read().splitlines()

    return [int(line) for line in lines]


def find_measurements_larger_than_prev(all_num: list):
    """ Find all measurements greater than previous measurements"""

    counter = -1
    prev = 0
    for num in all_num:
        # First prev is always less than num
        if prev < num:
            counter += 1
            prev = num
        else:
            prev = num
    return counter


def find_sum_of_windows(all_num: list):
    """ Find sum of three sliding windows """

    sum_of_windows = []
    for i in range(len(all_num)):
        try:
            sum_of_windows.append(all_num[i] + all_num[i + 1] + all_num[i + 2])
        except IndexError:
            return find_measurements_larger_than_prev(sum_of_windows)


def main():
    all_num = read_input()
    counter1 = find_measurements_larger_than_prev(all_num)
    counter2 = find_sum_of_windows(all_num)

    print(counter1)
    print(counter2)


main()
