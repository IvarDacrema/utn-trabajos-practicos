"""
6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).
"""
import random

listaNumeros = []
lista2Numeros = [0, 0, 0, 0, 0, 0, 0]

for i in range(7):
  listaNumeros.append(random.randint(1, 100))

print(listaNumeros)
# iteramos la lista con enumerate para poder tener el valor con el indice al mismo tiempo
for i, valor in enumerate(listaNumeros):
  if i <= 5:
    lista2Numeros[i+1] = valor
  else:
    lista2Numeros[0] = valor

print(lista2Numeros)
