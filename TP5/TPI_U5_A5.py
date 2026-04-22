"""
5) Crear una lista con los nombres de 8 estudiantes presentes en clase.

• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.

•Mostrar la lista final actualizada.
"""

listaAlumnos = ["araceli", "maxi", "ludmila", "sofia", "marcela", "alfredo", "sandra", "fabian"]
nombre = ""

print("""El programa busca un nombre en una lista realiza una de las siguientes acciones.
Agregar
Eliminar

Si desea salir del programa coloque finalizar""")

while nombre != "finalizar":
  nombre = input("""
  ELija una opcion: """).lower()

  if nombre == "eliminar":
    print(f"""
    Lista de alumnos

    {listaAlumnos}""")
    nombre = input("""
    Que nombre quiere eliminar:

    """)
    if  nombre in listaAlumnos:
      listaAlumnos.remove(nombre)
    else:
      print("El nombre no esta en la lista.")

  elif nombre == "agregar":
    print(f"""
    Lista de alumnos

    {listaAlumnos}""")
    nombre = input("""
    Que nombre quiere agregar:

    """)
    if  nombre not in listaAlumnos:
      listaAlumnos.append(nombre)
    else:
      print("El nombre ya esta en la lista.")

print(f"""
La lista de alumnos quedo de la siguiente forma:

{listaAlumnos}""")