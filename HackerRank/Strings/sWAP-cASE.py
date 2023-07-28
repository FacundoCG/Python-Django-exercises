""" You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa. """

def swap_case(s:str)->str:
    string: str = ""
    abecederario_min: list = []
    abecedario_may: list = []
    
    for i in range(97,123):
        abecederario_min.append(chr(i))
    
    for j in range(65,91):
        abecedario_may.append(chr(j))
        
    for char in s:
        if char in abecederario_min or char in abecedario_may:
            if char.isupper():
                string += char.lower()
            else:
                string += char.upper()
        else:
            string += char
    
    return string

if __name__ == '__main__':
    s: str = input()
    result: str = swap_case(s)
    print(result)
