
from typing import List
from util import read_input


class Board:
    """ A single Bingo Board """
    
    def __init__(self):
        self.rows = [[] for _ in range(5)]
        self.columns = [[] for _ in range(5)] 
        self.rows_print = [[] for _ in range(5)]
    def fill_board(self, lines: List[List[int]]):
        """ Fill the board with the numbers from input
        
        :param lines:
            A 5x5 list of strings.
        """
        for row in range(len(lines)):
            self.rows[row] = [int(num) for num in lines[row].split()]
            self.rows_print[row] = [int(num) for num in lines[row].split()]
            for col in range(len(self.rows)):
                self.columns[col].append(self.rows[row][col])

    def check_board(self, num: int):
        """Check for a specific number in each row/col and remove it from list"""
        
        for row in range(len(self.rows)):
            if num in self.rows[row]:
                self.rows[row].remove(num)
                for entry in range(len(self.rows_print)):
                    if num == self.rows_print[row][entry]:
                        self.rows_print[row][entry] = 'X'
                if len(self.rows[row]) == 0:
                    return True
                
        for col in range(len(self.columns)):
            if num in self.columns[col]:
                self.columns[col].remove(num)
                if len(self.columns[col]) == 0:
                    return True
        
        return False

    def sum_unmarked_nums(self):
        """ Sum the remaining numbers """
        return sum(sum(row) for row in self.rows)
    
    def print_board(self):
        """ Print board for visualisation """
        print("\n")
        for row in self.rows_print:
            print(row)
        print("\n")
            
        
class BingoCollections:
    """ A collection of Bingo Boards"""
    
    def __init__(self):
        self.nums: List[int] = []
        self.boards: List[Board] = []
        self.remaining_boards_idx: List[int] = []

    def fill_bingo_collection(self, lines: List[List[int]]):
        """ Wrapper to call both fill nums and fill collections """
        #self._fill_collection(lines)
        self.nums = [int(num) for num in lines[0].split(",")]
        line_counter = 1
        while line_counter < len(lines[2:]):
            # Bingo boards are separated by an empy list
            if not lines[line_counter]:
                board = Board()
                board.fill_board(lines[line_counter+1:line_counter+6])
                self.boards.append(board)
            line_counter += 1
            
        self.remaining_boards_idx = [i for i in range(len(self.boards))]

        
    def check_collection(self):
        """ Check the collectiion of boards as each number is drawn"""
        check = False
        
        for num in self.nums:
            for board in self.boards:
                check = board.check_board(num)
                if check:
                    return board.sum_unmarked_nums()*num
                
    def check_collection2(self):
        """ Check the collectin of boards as each number is drawn """
        for num in self.nums:
            board = self.check_remaining_boards(num)
            self.boards[25].print_board()
            if board:
                self.boards[board].print_board()
                return self.boards[board].sum_unmarked_nums()*num

    def check_remaining_boards(self, num):
        """ Check only the remaining boards! """
        for board_idx in self.remaining_boards_idx:
            self.boards[27].print_board()
            check = self.boards[board_idx].check_board(num)
            if len(self.remaining_boards_idx) == 1 and check:
                return int(self.remaining_boards_idx[0])
            elif check:
                self.remaining_boards_idx.remove(board_idx)

        
def main():
    """ Mainline """
    
    lines = read_input("day4.txt")
    
    all_boards = BingoCollections()
    all_boards.fill_bingo_collection(lines)

    print(all_boards.check_collection())
    
    all_boards2 = BingoCollections()
    all_boards2.fill_bingo_collection(lines)
    
    print(all_boards2.check_collection2())

if __name__ == '__main__':
    main()
