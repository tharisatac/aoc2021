import collections
from util import read_input
from typing import Mapping, Tuple, List

def parse_line() -> Tuple[List[str], List[str]]:
    """ 
    Get entry and output values
    """
    entry = []
    op = []
    for line in read_input("day8.txt"):
        entry.append(line.split(" | ")[0])
        op.append(line.split(" | ")[1])
    
    return entry, op

def map_line_to_numbers(line:str, segments_to_number: Mapping[int, str], total_numbers: Mapping[str, int]) -> List[int]:
    """ 
    Take one line from entry or otuput and map it to numbers based on segments.
    """
    segments = line.split(" ")
    for segment in segments:
        try: 
            total_numbers[segments_to_number[len(segment)]] += 1
        except KeyError:
            pass
    return total_numbers
    
def sum_values(total_numbers: Mapping[str, int]):
    """ 
    Print the sum of values
    """
    print(sum(value for value in total_numbers.values()))

def main():
    # Number of segments to number
    segments_to_number = {2:'One', 4:'Four', 3:'Seven', 7:'Eight'}
    total_numbers = collections.defaultdict(int)
    entry, op = parse_line()
    
    for line in op:
        total_numbers = map_line_to_numbers(line, segments_to_number, total_numbers)
    sum_values(total_numbers)
    


if __name__ == '__main__':
    main()