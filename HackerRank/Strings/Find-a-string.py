""" In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 

String traversal will take place from left to right, not from right to left. """

def count_substring(string: str, sub_string: str)->int:
    n: int = len(string)
    m: int = len(sub_string)
    times: int = 0
    
    for i in range(n):
        if sub_string == string[i:i+m]:
            times+=1
    
    return times

if __name__ == '__main__':
    string: int = input().strip()
    sub_string: int = input().strip()
    
    count: int = count_substring(string, sub_string)
    print(count)