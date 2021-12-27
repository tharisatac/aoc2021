def read_input(file):
    """ Read input file """
    with open("../inputs/"+file) as f:
        lines = f.read().splitlines()   
    return lines

def change_line_to_numbers(file):
    """
    Split line into days
    """
    with open("../inputs/"+file) as f:
        line = f.read().splitlines()   
    return list(map(int, line[0].split(",")))