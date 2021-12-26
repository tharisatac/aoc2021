import collections
from util import read_input


class LanternFishGroup:
    """
    A group of lanternfish
    """

    def __init__(self):
        """
        The amount of fish per day
        """
        days = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.days = {key: value for key, value in zip(days, [0] * len(days))}

    def add_fish(self, day: int):
        self.days[day] += 1

    def countdown(self, countdown_days: int):
        """
        Reset fish with 0 days to 6 and creates a new lantern fish.
        """
        for _ in range(countdown_days):
            day0 = self.days[0]
            for day in [0, 1, 2, 3, 4, 5, 6, 7]:
                self.days[day] = self.days[day + 1]
            self.days[6] += day0
            self.days[8] = day0

    def print_num_fish(self):
        print("Number of fish:", sum(val for val in self.days.values()))


def get_days(line: str):
    """
    Split line into days
    """
    return map(int, line.split(","))


def main():
    fish_group = LanternFishGroup()
    all_days = get_days(read_input("day6.txt")[0])
    for days in all_days:
        fish_group.add_fish(days)

    fish_group.countdown(256)
    fish_group.print_num_fish()


if __name__ == "__main__":
    main()
