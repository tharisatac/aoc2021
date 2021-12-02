from collections import defaultdict
from util import read_input
import re

def _read_input():
    lines = read_input("day2.txt")
    directions = defaultdict(int)
    for line in lines:
        direction, num = re.split('\s+', line)
        if 'up' in direction:
            directions['up'] += int(num)
        # Can also just minus from up but just in case
        elif 'down' in direction:
            directions['down'] += int(num)
        elif 'forward' in direction:
            directions['forward'] += int(num)
    
    return directions

def _read_input2():
    lines = read_input("day2.txt")
    directions = dict.fromkeys(['aim','forward_h', 'forward_d'],0)
    for line in lines:
        direction, num = re.split('\s+', line)
        if 'up' in direction:
            directions['aim'] -= int(num)
        elif 'down' in direction:
            directions['aim'] += int(num)
        elif 'forward' in direction:
            directions['forward_h'] += int(num)
            directions['forward_d'] += int(num)*directions['aim']
    return directions

def main():
    directions = _read_input()
    h = directions["forward"]
    v = directions["down"] - directions["up"]
    print(h*v)
    
    directions2 = _read_input2()
    h = directions2['forward_h']
    d = directions2['forward_d']
    print(d*h)
main()