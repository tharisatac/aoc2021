def read_input(file):
    """ Read input file """
    with open("../inputs/"+file) as f:
        lines = f.read().splitlines()   
    return lines
