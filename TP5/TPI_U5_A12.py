"""
12) Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
- Mostrar la lista original.
- Mostrar la lista ordenada de menor a mayor.
- Mostrar la lista ordenada de mayor a menor.
- Investigar el uso de sorted() y del parámetro reverse.
"""

listaDeNumeros = []
listaOrdenada = []


while len(listaDeNumeros) < 8:
  numeroIngresado = int(input("Ingrese el numero entero positivos que desea meter en la lista: "))
  if str(numeroIngresado).isdigit() and len(listaDeNumeros) < 8:
    listaDeNumeros.append(numeroIngresado)
    print(f"Ingresaste {len(listaDeNumeros)} numero.")
  else:
    print("No es un valor valido, debes ingresar numeros enteros positivos.")

print("Lista ingresada por el usuario:")
for i in listaDeNumeros:
  print(i, end = "-")
print("")
print("Lista ordenada de menor a mayor:")
listaOrdenada = sorted(listaDeNumeros)
for i in listaOrdenada:
  print(i, end = "-")
print("")
print("Lista ordenada de mayor a menor:")
listaOrdenada.reverse()
for i in listaOrdenada:
  print(i, end = "-")
print("")

#print(f"Lista ingresada por el usuario: {listaDeNumeros}")
#print(f"Lista ordenada de mayor a menor: {sorted(listaDeNumeros, reverse=True)}")
#print(f"Lista ordenada de menor a mayor: {sorted(listaDeNumeros)}")