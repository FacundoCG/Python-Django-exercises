""" You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters. """

if __name__ == '__main__':
    s: str = input()
    
    has_alphanumeric: bool = any([char.isalnum() for char in s])
    has_alphabetical: bool = any([char.isalpha() for char in s])
    has_digit: bool = any([char.isdigit() for char in s])
    has_lowercases: bool = any([char.islower() for char in s])
    has_uppercases: bool = any([char.isupper() for char in s])
    
    print(has_alphanumeric)
    print(has_alphabetical)
    print(has_digit)
    print(has_lowercases)
    print(has_uppercases)
