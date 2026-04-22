#Ejercicio 4 — Escape Room: La Bóveda
import time

energia = 100
tiempo = 12
cerradurasAbiertas = 0
alarma = False
codigoParcial = ""
alarmaBloqueada = False
antiSpam = 0

while True:
    nombreAgente = input("Ingrese el nombre del agente, solo debe ingresar letras: ").title()
    if nombreAgente.isalpha():
        break
    else:
        print("Nombre del agente a ingresado caracteres erroneos, solo letras.")

while energia > 0 and tiempo > 0 and cerradurasAbiertas < 3 and not alarmaBloqueada: 
    if alarma and tiempo <= 3:
        print("Alarma bloqueada.")
        alarmaBloqueada = True
    else:    
        while True:
            print(f"Energia: {energia} - Tiempo: {int(tiempo)} - Alarma: {("Activada" if alarma else "Desactivada")} - Cerraduras abiertas: {cerradurasAbiertas}")
            opcionElegida = input("Ingrese el numero de la opción que desea realizar -> 1-Forzar cerradura 2-Hacker panel 3-Descansar: ")
            if opcionElegida.isdigit and 1 <= int(opcionElegida) <= 3:
                match opcionElegida:
                    case "1":
                        print("Forzar cerradura")
                        if antiSpam == 2:
                            print("Se trabo la cerradura - Alarma activada.")
                            alarma = True
                            tiempo -= 2
                            energia -= 20
                            break
                        else:
                            if energia <= 40:
                                while True:
                                    numeroRiesgoAlarma = input("Riesgo de alarma, ingrese un numero entre estas opciones: 1 - 2 - 3: ")
                                    if numeroRiesgoAlarma.isdigit() and 1 <= int(numeroRiesgoAlarma) <= 3:
                                        if numeroRiesgoAlarma == "3":
                                            tiempo -= 2
                                            energia -= 20
                                            print("Alarma activada.")
                                            alarma = True
                                            break
                                        else:
                                            tiempo -= 2
                                            energia -= 20
                                            print("Alarma no activada, 1 cerradura abierta.")
                                            cerradurasAbiertas += 1
                                            break
                                        break
                                    else:
                                        print("Los datos ingresados son incorrectos, un numero entero entre 1 y 3.")
                            else:
                                print("Cerradura abierta.")
                                cerradurasAbiertas += 1
                                tiempo -= 2
                                energia -= 20
                                antiSpam += 1
                                break
                    case "2":
                        print("Hackeo panel")
                        for i in range(4):
                            codigoParcial += "A"
                            print(codigoParcial)
                            time.sleep(1)
                            antiSpam = 0
                            energia -= 5
                            tiempo -= 0.75
                        if len(codigoParcial) >= 8:
                            cerradurasAbiertas += 1
                            codigoParcial = ""
                        break
                    case "3":
                        print("Descanso")
                        if alarma:
                            print("No pudiste descansar, el estres de la alarma te agota.")
                            tiempo -= 1
                            energia -= 10
                            break
                        elif energia <= 85:
                            energia += 15
                            tiempo -= 1
                            break
                        else:
                            energia = 100
                            tiempo -= 1
                            break
                    case _:
                        break
            else:
                print("El dato ingresado es incorrecto, debe ser uno de los numeros que estan en las opciones.")

if cerradurasAbiertas == 3:
    print(f"Felicitaciones {nombreAgente} haz abierto las 3 cerraduras.")
else:
    print(f"Haz perdido {nombreAgente}.")