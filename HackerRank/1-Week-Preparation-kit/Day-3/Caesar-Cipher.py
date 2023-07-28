""" Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. 

If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. 

In the case of a rotation by 3, w, x, y and z would map to z, a, b and c. """

import os

def caesarCipher(s: str, k: int)->str:
    string: str = ""
    abecederario_min: list = []
    abecedario_may: list = []
    
    for i in range(97,123):
        abecederario_min.append(chr(i))
    
    for j in range(65,91):
        abecedario_may.append(chr(j))
    
    for i in s:
        
        if i.isalpha() and i.islower(): 
            index = (abecederario_min.index(i)+k)%26
            string+= abecederario_min[index]
            
        elif i.isalpha() and i.isupper():
            index = (abecedario_may.index(i)+k)%26
            string+= abecedario_may[index]
            
        else:
            string += i
        
    return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n: int = int(input().strip())

    s: str = input()

    k: int = int(input().strip())

    result: str = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
