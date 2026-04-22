"""
3) Generar una lista con 15 números enteros al azar entre 1 y 100.

• Crear una lista con los pares y otra con los impares.

• Mostrar cuántos números tiene cada lista.
"""

import random

lista = []

for i in range(15):
  lista.append(random.randint(1, 100))

print(lista)
