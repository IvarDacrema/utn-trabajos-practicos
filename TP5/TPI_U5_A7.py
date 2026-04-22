"""
7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.

• Calcular el promedio de las mínimas y el de las máximas.

• Mostrar en qué día se registró la mayor amplitud térmica.
"""

listaAnidada = [[21, 32], [22, 34], [20, 33], [22, 33], [24, 39], [21, 31], [22, 33]]
sumatoriaMax = 0
sumatoriaMin = 0
#Calcular la media de las temperaturas minimas y maximas.
for dias in listaAnidada:
  for i, valor in enumerate(dias):
    if i == 0:
      sumatoriaMin += valor
    elif i == 1:
      sumatoriaMax += valor
sumatoriaMax = sumatoriaMax/len(listaAnidada)
sumatoriaMin = sumatoriaMin/len(listaAnidada)
print(f"""Promedio de las minimas: {sumatoriaMin: .2f}.
Promedio de las maximas: {sumatoriaMax: .2f}""")
#Mostrar mayor amplitud térmica.
amplitudes = []
for dias in listaAnidada:
  diferencias = dias[1]-dias[0]
  amplitudes.append(diferencias)
print(f"El dia con mayor amplitud termica es el {amplitudes.index(max(amplitudes))+1}")#Imprimimos el indice + 1 del mayor valor de la lista de amplitudes, utilizamos index para el indice sobre el valor max de esta lista.
