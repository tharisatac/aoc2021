def read_input(file):
    """ Read input file """
    with open("../inputs/"+file) as f:
        lines = f.read().splitlines()   
    return lines

def read_input_as_int(file):
    """ Read input file """
    with open("../inputs/"+file) as f:
        lines = f.read().splitlines()   
    return [int(line) for line in lines]
