""" The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary. """

if __name__ == '__main__':
    a: int = int(input())
    b: int = int(input())
    
    integer_division: int = a//b
    float_division: float = a/b
    
    print(integer_division) 
    print(float_division)
