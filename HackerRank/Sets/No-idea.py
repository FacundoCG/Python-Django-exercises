""" There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B.

Your initial happiness is 0. For each i integer in the array, if iϵA , you add 1 to your happiness. If iϵB, you add -1 to your happiness. 

Otherwise, your happiness does not change. Output your final happiness at the end. """

def convert_input(cadena:str)->list:
    lista: list = cadena.split()
    lista_enteros: list = list(map(int,lista))
    
    return lista_enteros

size_input: str = input("")
array_input: str = input("")
set_a_input: str = input("")
set_b_input: str = input("")

array: list = convert_input(array_input)
A: set = set(convert_input(set_a_input))
B: set = set(convert_input(set_b_input))

happiness: int = 0

for i in array:
    if i in A:
        happiness+=1
    elif i in B:
        happiness -=1
    else:
        continue

print(happiness)