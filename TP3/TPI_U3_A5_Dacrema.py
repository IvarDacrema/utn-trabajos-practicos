#Actividad 5 - Escape Room:"La Arena del Gladiador"
import random

nombreGladiador = ""
vidaGladiador = 100
vidaEnemigo = 100
pocionesDeVidaGladiador = 3
pocionesDeVidaEnemigo = 2
dañoBaseAtaquePesado = 15
dañoBaseEnemigo = 12
turnoGladiador = True

while True:
    nombreGladiador = input("Ingrese el nombre del gladiador, se permiten solo letras: ").title()
    if nombreGladiador.isalpha():
        print("Tu gladiador esta listo para el coliseo.")
        break
    else:
        print("El nombre ingresado tiene caracteres no permitidos, ingrese solo letras.")

while vidaGladiador > 0 and vidaEnemigo > 0:
    print(f"""
{nombreGladiador} - vida:{vidaGladiador} - pociones: {pocionesDeVidaGladiador}
Enemigo - vida: {vidaEnemigo} - pociones: {pocionesDeVidaEnemigo}

Elige tu ataque:
1- Ataque pesado
2- Rafaga de ataques
3- Curar
          """)
    while True:
        opcionElegida = input("Ingrese la opción que desea realizar: ")
        if opcionElegida.isdigit() and 1 <= int(opcionElegida) <= 3:
            match opcionElegida:
                case "1":
                    print("Ataque pesado")
                    if vidaEnemigo <= 20:
                        vidaEnemigo -= dañoBaseAtaquePesado*1.5
                        print(f"Atacaste al enemigo por {(dañoBaseAtaquePesado*1.5):.2f} puntos de daño.")
                        break
                    else:
                        vidaEnemigo -= dañoBaseAtaquePesado
                        print(f"Atacaste al enemigo por {dañoBaseAtaquePesado} puntos de daño.")
                        break

                case "2":
                    print("Rafaga de ataques")
                    for i in range(3):
                        vidaEnemigo -= 5
                        print("Golpe conectado con 5 de daño")
                    break
                case "3":
                    print("Curar")
                    if pocionesDeVidaGladiador >= 1:
                        vidaGladiador += 30
                        pocionesDeVidaGladiador -= 1
                        print("Recuperaste 30 puntos de vida.")
                    else:
                        print("No tienes pociones disponibles.")
                    break
        else:
            print("Elija una opción correcta.")
    #Ataque del enemigo
    if vidaGladiador <= 40:
        numeroAleatorioDeAtaque = random.randint(1, 4)
        if numeroAleatorioDeAtaque == 3:
            vidaGladiador -= dañoBaseEnemigo*1.5
            print(f"ATAQUE CRITICO por {(dañoBaseEnemigo*1.5):.2f} de daño del enemigo")
        else:
            vidaGladiador -= dañoBaseEnemigo
            print(f"¡El Enemigo te atacó por {dañoBaseEnemigo} puntos de daño!")
    else:
        vidaGladiador -= dañoBaseEnemigo
        print(f"¡El Enemigo te atacó por {dañoBaseEnemigo} puntos de daño!")
    if vidaEnemigo <= 30 and pocionesDeVidaEnemigo >= 1:
        vidaEnemigo += 30
        print("Enemigo a usado una poción de recuperación.")
        pocionesDeVidaEnemigo -= 1
    elif pocionesDeVidaEnemigo < 1:
        print("El enemigo no se puede curar, no tiene más pociones.")

print("")
if vidaEnemigo <= 0 and vidaGladiador <= 0:
    print("¡¡¡HAN MUERTO LOS 2 GLADIADORES!!!")
elif vidaEnemigo <= 0:
    print(f"¡¡¡FELICITACIONES {(nombreGladiador).upper()} ERES LIBRE!!!")
else:
    print("¡¡¡HAZ MUERTO!!!")
