"""
9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).

• Inicializarlo con guiones "-" representando casillas vacías.

• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".

• Mostrar el tablero después de cada jugada.
"""

tablero = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]

print("""Jugamos al Ta-Te-Ti, 2 jugadores que eligen entre X o O
 Para jugar deben colocar fila y columna donde quieren poner tu ficha.

 Tablero""")
for filas in tablero:
  for columnas in filas:
    print(columnas, end=" ")
  print()

#Ingreso de X y O
fila = 0
columna = 0
jugadorUno = input("Introduzca el nombre del jugador 1: ").lower()
jugadorDos = input("Introduzca el nombre del jugador 2: ").lower()
jugadorGanador = ""
jugador = 1
oportunidades = 0

while jugadorGanador != jugadorUno and jugadorGanador != jugadorDos:
  if jugador == 1:
    print()
    print(f"Elija posicion {jugadorUno}.")

    fila = int(input("Ingrese en numero de fila: "))-1
    columna = int(input("Ingrese en numero de columna: "))-1
    tablero[fila][columna]="X"
    for filas in tablero:
      for columnas in filas:
        print(columnas, end=" ")
      print()
    jugador = 2
    oportunidades += 1
  else:
    print()
    print(f"Elija posición {jugadorDos}")
    fila = int(input("Ingrese en numero de fila: "))-1
    columna = int(input("Ingrese en numero de columna: "))-1
    tablero[fila][columna]="O"
    for filas in tablero:
      for columnas in filas:
        print(columnas, end=" ")
      print()
    jugador = 1
    oportunidades += 1

  if oportunidades >= 5:
    jugadorGanador = input("""¿Hay ganador?. Colocar el nombre del ganador de ser esto así, si no dejar el espacio vacio.""").lower()

print()
print(f"El GANADOR de este juego es {jugadorGanador.upper()}")