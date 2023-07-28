""" Given 2 sets of integers, M and N, print their symmetric difference in ascending order.

The term symmetric difference indicates those values that exist in either M or N but do not exist in both. """

n: str = input("")
a: str = input("")
lista_a: list = a.split()
lista_enteros_a: list = list(map(int,lista_a))
A: set = set(lista_enteros_a)

m: str = input("")
b: str = input("")
lista_b: list = b.split()
lista_enteros_b: list = list(map(int,lista_b))
B: set = set(lista_enteros_b)

C: set = A.symmetric_difference(B)
lista_c: list = list(C)

lista_c.sort()

for x in lista_c:
    print(x)
