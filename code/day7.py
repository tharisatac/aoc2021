from typing import Iterable
from util import change_line_to_numbers
import statistics
import math

def find_total_fuel_part_1(median:int, ipt: Iterable[int])-> int:
    """ 
    Find the total fuel for all crabs part 1.
    """
    return sum(map(lambda x: abs(x-median), ipt))

def find_total_fuel_part_2(mean: int, ipt: Iterable[int])->int:
    """ 
    Find the total fuel for all crabs part 2.
    """

    def _return_total_sum(diff: int, total_sum: int = 0):
        """ 
        Return total sum based on distance
        """
        
        while diff > 0:
            total_sum += diff
            diff -= 1

        return total_sum

    standardized_ipt = list(map(lambda x: abs(x-math.floor(mean)), ipt))

    return sum(map(_return_total_sum, standardized_ipt))
    

def main():
    # Minimum distance will be the median of all the points
    ipt = change_line_to_numbers("day7.txt")
    median = statistics.median(ipt)
    
    # Minimum distance is now the mean of all points
    mean = statistics.mean(ipt)
    
    total_fuel = find_total_fuel_part_1(median, ipt)
    print(total_fuel)
    
    total_fuel2 = find_total_fuel_part_2(mean, ipt)
    print(total_fuel2)

    
if __name__ == '__main__':
    main()