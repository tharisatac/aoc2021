from collections import defaultdict
from typing import List
from util import read_input, yield_input
import time


class Info:
    """ 
    Class for extracting data from information
    """

    def __init__(self, lines: List[str]) -> None:
        self.total_lines = len(lines)
        self.lines = lines
        self.bit_dict = defaultdict(int)
        self.max_bit_dict = {}
        
        # Part 2
        
        self.oxygen_bits = {}
    
    def get_binary_strings(self):
        """ Interpret the lines and put them in a dictionary """
        for line in self.lines:
            for index, char in enumerate(line):
                self.bit_dict[index] += int(char) 
        
    def get_max_bits(self):
        string = ''
        for value in self.bit_dict.values():
            if (value/self.total_lines) > 0.5:
                string += '1'
            else:
                string += '0'

        return int(string, 2)

    def get_min_bits(self):
        string = ''
        for value in self.bit_dict.values():
            if (value/self.total_lines) > 0.5:
                string += '0'
            else:
                string += '1'
        return int(string, 2)

    def get_oxygen_rating(self):
        """ Get oxygen rating """
        tmp_lines = self.lines
        for idx in range(len(self.lines[0])):
            tmp_lines = self.check_lines(idx, tmp_lines)
            
            if len(tmp_lines) == 1:
                return int(tmp_lines[0],2) 
        return int(tmp_lines[0],2) 

    def get_co2_rating(self):
        """ Get co2 rating """
        tmp_lines = self.lines
        for idx in range(len(self.lines[0])):
            tmp_lines = self.check_lines(idx, tmp_lines, o2=False)
            if len(tmp_lines) == 1:
                return int(tmp_lines[0],2) 
        return int(tmp_lines[0],2) 
        

    def check_lines(self, idx, remaining_lines, o2 = True):
        """ Check the remaining lines """
        tmp_count = 0

        for line in range(len(remaining_lines)):
            for char in remaining_lines[line][idx]:
                tmp_count += int(char)
        print(f"temporary count:{tmp_count} at index {idx}")
        print("len of remaining lines:", len(remaining_lines))
        if tmp_count/len(remaining_lines) >= 0.5:
            if o2:
                return self.find_lines(idx, 1, remaining_lines)
            else:
                return self.find_lines(idx, 0, remaining_lines)
        else:
            if o2:
                return self.find_lines(idx, 0, remaining_lines)
            else:
                return self.find_lines(idx, 1, remaining_lines)


    def find_lines(self, idx: int, num:int , remaining_lines: List[str]):
        tmp_lines = []
        for line in remaining_lines:
            if line[idx] == str(num):
                tmp_lines.append(line)
        return tmp_lines
            
def main():
    t0 = time.time()
    lines = read_input("day3.txt")

    info = Info(lines)
    info.get_binary_strings()
    gamma_rate = info.get_max_bits()
    epsilon_rate = info.get_min_bits()

    t1 = time.time()
    print(t1-t0)
    print(gamma_rate*epsilon_rate)
    
    o2 = info.get_oxygen_rating()
    co2 = info.get_co2_rating()
    
    print(o2)
    print(co2)
    print(co2*o2)
if __name__ == "__main__":
    main()