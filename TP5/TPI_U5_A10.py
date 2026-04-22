"""
10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.

• Mostrar el total vendido por cada producto.

• Mostrar el día con mayores ventas totales.

• Indicar cuál fue el producto más vendido en la semana.
"""
listaProductos = [
    ["productos", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"],
    ["huevo", 100, 120, 110, 130, 150, 200, 80],
    ["harina", 50, 45, 60, 55, 70, 85, 20],
    ["manteca", 20, 25, 18, 30, 35, 40, 12],
    ["leche", 80, 85, 90, 100, 110, 120, 33]] #lista de productos

for filas in listaProductos:
  for columnas in filas:
    print(columnas, end=" - ")
  print() #muestra la lista

print() #espacio para mejor presentación

#mostrar total vendido
masVentaProducto = 0
masVentaProductoNombre = ""
for producto in listaProductos[1:]: #itera listaProductos desde la posición 1
  nombre = producto[0]
  sumatoria = 0
  for cantidad in producto[1:]: #itera para realizar la suma de las cantidades a cada producto
    sumatoria += cantidad
  if masVentaProducto < sumatoria: #pregunta si la sumatoria es mayor que un valor creado, esto va a guardar el producto con más ventas
    masVentaProducto = sumatoria
    masVentaProductoNombre = nombre
  print(f"{nombre} vendio {sumatoria} unidades.")

#mostra día con más ventas
listaVentas = [] #se crea otra lista para guardar los datos de la semana.
masVentas = 0

for cantidad in listaProductos[1:]:
    contadorDia = 1
    contadorVentas = 0
    for valor in cantidad[1:]:
      #esta variable guarda el nombre que esta en la posición 0 de listaProductos (días de la semana), 0 es la posición de esa lista y el contador modifica el segundo indice para que no siempre se guarde el item numero 1
      nombre = listaProductos[0][contadorDia]
      if listaProductos.index(cantidad) == 1: #cuando el indice de cantidad es 1 crea rellena la lista con los primeros datos.
        listaVentas.append([nombre, valor]) #Los datos son los nombres de los días y el valor del primer producto.
      else:
        listaVentas[contadorVentas][1] += valor #cuando el índice no es el primero lo que hace es sumar el numero que esta tomando la variable valor y la suma.
      contadorDia += 1 #cuenta para que se modifica el día que se guarda en la listaVentas.
      contadorVentas += 1 #cuenta para que se suma en el lugar correcto modificando el primer índice.
for cantidades in listaVentas: #idem al de el producto más vendido pero con el día con más ventas.
  if masVentas < cantidades[1]:
    masVentas = cantidades[1]
    nombreMasVentas = cantidades[0]
print()
print(f"El dia con más ventas fue el {nombreMasVentas} con {masVentas} de unidades.")
print()
print(f"El producto que más se vendio fue {masVentaProductoNombre} con {masVentaProducto} unidades.")