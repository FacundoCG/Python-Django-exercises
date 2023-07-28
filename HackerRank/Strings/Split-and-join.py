""" You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen. """

def split_and_join(line:str)->str:
    line: list = line.split()
    line: str = "-".join(line)
    
    return line

if __name__ == '__main__':
    line: str = input()
    result: str = split_and_join(line)
    print(result)