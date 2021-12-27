from typing import Iterable
from util import change_line_to_numbers
import statistics

def find_total_fuel(median:int, ipt: Iterable[int])-> int:
    """ 
    Find the total fuel for all the crabs
    """
    return sum(map(lambda x: abs(x-median), ipt))

def main():
    # Minimum distance will be the median of all the points
    ipt = change_line_to_numbers("day7.txt")
    median = statistics.median(ipt)
    
    total_fuel = find_total_fuel(median, ipt)
    print(total_fuel)
    
if __name__ == '__main__':
    main()