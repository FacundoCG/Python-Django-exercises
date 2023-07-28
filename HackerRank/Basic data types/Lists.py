""" Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 

Iterate through each command in order and perform the corresponding operation on your list. """

if __name__ == '__main__':
    lista: list = []
    N: int = int(input())
    
    for i in range(N):
        command: list = input().split()
        
        if "insert" == command[0]:
            lista.insert(int(command[1]),int(command[2]))
        elif "print" == command[0]:
            print(lista)
        elif "remove" == command[0]:
            lista.remove(int(command[1]))
        elif "append" == command[0]:
            lista.append(int(command[1]))
        elif "sort" == command[0]:
            lista.sort()
        elif "pop" == command[0]:
            lista.pop()
        else:
            lista.reverse()
