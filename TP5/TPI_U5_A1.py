"""
1) Crear una lista con las notas de 10 estudiantes.

•Mostrar la lista completa.

•Calcular y mostrar el promedio.

•Indicar la nota más alta y la más baja.
"""

notas = []
sumatoria = 0
promedio = 0
notaAlta  = 0
notaBaja = 0

print("Ingrese 10 notas de alumnos.")
#Se modifican los valores de la lista con las notas.
for i in range(10):
  nota = int(input("Ingrese la nota: "))
  notas.append(nota)
#Se hace la suma de todas las notas y se saca la media.
for i in range(len(notas)):
  sumatoria += notas[i]
promedio = sumatoria/len(notas)
#Se busca la nota más alta y baja.
notaAlta = max(notas)
notaBaja = min(notas)
#Se imprimen los resultados.
print(f"""
El promedio de las notas del curso es: {promedio}
La nota más alta es: {notaAlta}.
La nota más baja es: {notaBaja}""")
