"""
8) Crear una matriz con las notas de 5 estudiantes en 3 materias.

• Mostrar el promedio de cada estudiante.

• Mostrar el promedio de cada materia.
"""

listaAlumnos = [["alum", "f", "l", "a"], ["sofi", 9, 9, 10], ["ara", 10, 9, 10], ["maxi", 7, 8, 6], ["lud", 9, 8, 10], ["feli", 9, 7, 10]]

print("""
alumn: Alumnos.
f: Física.
l: Lengua.
a: Arte.
""")

for alumnos in listaAlumnos:
  for notas in alumnos:
    print(notas, end=" ")
  print()
print()
#Calculamos el promedio de notas de cada alumno.
nombre = ""
promedio = 0
for alumno in listaAlumnos:
  if listaAlumnos.index(alumno) != 0:
    promedio = 0
    for notas in alumno:
      if alumno.index(notas) != 0:
        promedio += notas
    promedio = promedio/(len(alumno)-1)
    print(f"El promedio de {alumno[0]} es de {promedio: .2f}")
#Calculamos el promedio de notas de cada materia.
promedioFisica = 0
promedioLengua = 0
promedioArte = 0
for alumno in listaAlumnos[1:]:
  promedioFisica += alumno[1]
  promedioLengua += alumno[2]
  promedioArte += alumno[3]

promedioFisica = promedioFisica / (len(listaAlumnos)-1)
promedioLengua = promedioLengua / (len(listaAlumnos)-1)
promedioArte = promedioArte / (len(listaAlumnos)-1)

print(f"""
Promedio de Fisica: {promedioFisica}
Promedio de Lengua: {promedioLengua}
Promedio de Arte: {promedioArte}""")