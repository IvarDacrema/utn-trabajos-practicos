"""
2) Pedir al usuario que cargue 5 productos en una lista.

• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().

• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
"""

productos = []

print("Ingrese 5 productos.")

for i in range(5):
  producto = input(f"Ingrese el producto {i+1}: ")
  productos.append(producto.lower())
print(sorted(productos))

while producto != "salir":
  producto = input("Ingrese un producto que desea eliminar: ")
  if producto in productos:
    productos.remove(producto)
    print(productos)
  else:
    print("El producto no esta en la lista.")
