"""
11) Crear una lista con los nombres de 10 estudiantes.

- Solicitar al usuario que ingrese un nombre a
buscar.

- Indicar si el nombre se encuentra en la lista.

- Mostrar la posición en la que aparece.

- Si no se encuentra, informar que no está en la lista.
"""
listaAlumnos = ["Araceli", "Sofia", "Maxi", "Ludmila", "Marcela", "Alfredo", "Fabian", "Sandra"]
nombreBusqueda = input("Ingrese el nombre que desea buscar en la lista de alumnos: ").title()
if nombreBusqueda in listaAlumnos:
  print(f"{nombreBusqueda} esta en la lista, posicion {listaAlumnos.index(nombreBusqueda)}")
else:
  print(f"{nombreBusqueda} no esta en la lista.")