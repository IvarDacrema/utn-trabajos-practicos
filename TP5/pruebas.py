puntajes = [450, 1200, 875, 990, 300, 1500, 640]
numeroMenor = puntajes[0]
numeroMayor = puntajes[0]

for i in puntajes:
    if numeroMayor <= i:
        numeroMayor = i
    elif numeroMenor >= i:
        numeroMenor = i
    if puntajes.index(i) == len(puntajes)-1:
      print(f"El puntaje más grande es: {numeroMayor}")
      print(f"El puntaje más chico es: {numeroMenor}")

listaOrdenada = sorted(puntajes, reverse = True)

for i in listaOrdenada:
  print(i, end= "-")

print("")
for i in listaOrdenada:
   if i == 990:
      print(f"La posición del puntaje 990 en el ranking es {listaOrdenada.index(i)+1}") #Tome la posición del ranking como comenzando en 1