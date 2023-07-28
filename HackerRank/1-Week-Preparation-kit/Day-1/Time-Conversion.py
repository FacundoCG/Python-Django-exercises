""" Given a time in 12-hour AM/PM format, convert it to military (24-hour) time. """


import math
import os
import random
import re
import sys

def timeConversion(s:str):
    new: list = list(s)
    
    if new[8]=="P":
        if int(new[0])==0:
            new[0] = str(int(new[0])+1)
            new[1] = str(int(new[1])+2) 
        elif int(new[0])==1 and int(new[1])==2:     
           pass
        else:
            new[0] = str(int(new[0])+1)
            new[1] = str(int(new[1])+2)  
    else:
        if int(new[0])>0:
            new[0] = str(int(new[0])-1)
            new[1] = str(int(new[1])-2)          
    
    new[8]=''
    new[9]=''
    
    s = ''.join(new)
    
    return s
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s: str = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
