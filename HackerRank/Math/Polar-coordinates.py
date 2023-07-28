""" You are given a complex z. Your task is to convert it to polar coordinates."""

import cmath

z: complex = complex(input())

modulo: float = abs(complex(z))
angulo: float = cmath.phase(z)

print(round(modulo,3))
print(round(angulo,3))
