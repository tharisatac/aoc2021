from typing import Dict, Tuple
from util import read_input
import collections

def _parse_line(coor_dict: Dict[Tuple[int,int],int], line: str) -> Dict[Tuple[int,int],int]:
    """ 
    Parse one line at at ime and return all the numbers inbetween
    """
    
    [start_coor, end_coor] = [number.split(",") for number in line.split(" -> ")]
    x1, y1 = map(int, start_coor)
    x2, y2 = map(int, end_coor)

    # Horizontal line
    if x1 == x2:
        if y1 < y2:
            y_range = range(y1, y2+1)
        else:
            y_range = range(y2, y1+1)    
        
        for y in y_range:
            coor_dict[(x1,y)] += 1

    # Vertical line
    if y1 == y2:
        if x1 < x2:
            x_range = range(x1, x2+1)
        else:
            x_range = range(x2, x1+1) 
       
        for x in x_range:
            coor_dict[(x,y1)] += 1
    
    # Diagonal line
    if abs(y1-y2) == abs(x1-x2):
        if x1 < x2:
            x_range = range(x1, x2+1)
        else:
            x_range = range(x1, x2-1, -1) 
        
        if y1 < y2:
            y_range = range(y1, y2+1)
        else:
            y_range = range(y1, y2-1, -1)
        
        for x,y in zip(x_range,y_range):
            coor_dict[(x,y)] += 1

    return coor_dict
    
    
    

def main():
    coor_dict = collections.defaultdict(lambda:0)
    for line in read_input("day5.txt"):
        coor_dict = _parse_line(coor_dict, line)
    
    points = len([val for val in coor_dict.values() if val >= 2])
    print(points)
    # print(coor_dict)
    
    

if __name__ == '__main__':
    main()
