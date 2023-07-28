""" Read a given string, change the character at a given index and then print the modified string."""

def mutate_string(string: str, position: int, character: str)->str:
    string_list : list = list(string)
    string_list[position]: str = character
    
    word: str = "".join(string_list)
    
    return word

if __name__ == '__main__':
    s:str = input()
    i, c:str = input().split()
    s_new: str = mutate_string(s, int(i), c)
    print(s_new)
