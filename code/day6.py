from util import read_input

class LanternFish:
    """ 
    One Lanternfish object
    """
    def __init__(self, days: int):
        self.days = days
    
    def _reset_timer(self) -> None:
        self.days = 6
    
    def _countdown(self):
        self.days -= 1
    
    def _create_new_lanternfish(self):
        return LanternFish(days=8)

class LanternFishGroup:
    """ 
    A group of lanternfish
    """
    def __init__(self):
        self.fish: list[LanternFish] = []
    
    def add_fish(self, fish: LanternFish):
        self.fish.append(fish)
    
    def countdown(self, countdown_days: int):
        """ 
        Reset fish with 0 days to 6 and creates a new lantern fish.
        """
        for _ in range(countdown_days):
            new_fish = []
            for fish in self.fish:
                if fish.days != 0:
                    fish._countdown()
                else:
                    fish._reset_timer()
                    new_fish.append(fish._create_new_lanternfish())

            self.fish.extend(new_fish)
    
    def print_days(self):
        print("Number of fish:", len(self.fish))
        # for fish in self.fish:
        #     print(fish.days)


def get_days(line: str):
    """ 
    Split line into days
    """
    return map(int,line.split(","))

def main():
    fish_group = LanternFishGroup()
    all_days = get_days(read_input("day6.txt")[0])
    for days in all_days:
        fish_group.add_fish(LanternFish(days))

    fish_group.countdown(80)
    fish_group.print_days()
    
    
if __name__ == '__main__':
    main()