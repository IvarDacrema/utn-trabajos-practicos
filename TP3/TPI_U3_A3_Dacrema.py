#Actividad 3 - Agenda de Turnos con Nombres (sin listas)

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

nombreOperador = input("Ingrese el nombre del operador: ")

opcionIngresada = 0

while True:
    opcionIngresada = input("""Ingrese la opcion deseada: 
                            1-Reservar Turno. 
                            2-Cancelar turno (con nombre). 
                            3-Ver agenda del día. 
                            4-Ver resumen general. 
                            5- Salir.\n""")
    match opcionIngresada:
        case "1":
            print("Reservar turno")
            while True:
                elegirDia = input("Ingrese el dia que quiere el turno Lunes o Martes: ").lower()
                if elegirDia == "martes" or elegirDia == "lunes":
                    nombrePaciente = input("Ingrese el nombre del paciente: ").lower()
                    if elegirDia == "lunes":
                        if lunes1 == nombrePaciente:
                            print("Tienes el primer turno del lunes.\n")
                        elif lunes2 == nombrePaciente:
                            print("Tienes el segundo turno del lunes.\n")
                        elif lunes3 == nombrePaciente:
                            print("Tienes el tercer turno del lunes.\n")
                        elif lunes4 == nombrePaciente:
                            print("Tienes el cuarto turno del lunes.\n")
                        elif lunes1 == "":
                            lunes1 = nombrePaciente
                            print("Se le otorga el primer turno del dia lunes.\n")
                        elif lunes2 == "":
                            lunes2 = nombrePaciente
                            print("Se le otorga el segundo turno del dia lunes.\n")
                        elif lunes3 == "":
                            lunes3 = nombrePaciente
                            print("Se le otorga el tercer turno del dia lunes.\n")
                        elif lunes4 == "":
                            lunes4 = nombrePaciente
                            print("Se le otorga el cuarto turno del dia lunes.\n")
                        elif lunes1 != "" and lunes2 != "" and lunes3 != "" and lunes4 != "":
                            print("El lunes esta lleno.\n")
                        break
                    elif elegirDia == "martes":
                        if martes1 == nombrePaciente:
                            print("Tienes el primer turno del martes.\n")
                        elif martes2 == nombrePaciente:
                            print("Tienes el segundo turno del martes.\n")
                        elif martes3 == nombrePaciente:
                            print("Tienes el tercer turno del martes.\n")
                        elif martes1 == "":
                            martes1 = nombrePaciente
                            print("Se le otorga el primer turno del dia martes.\n")
                        elif martes2 == "":
                            martes2 = nombrePaciente
                            print("Se le otorga el segundo turno del dia martes.\n")
                        elif martes3 == "":
                            martes3 = nombrePaciente
                            print("Se le otorga el tercer turno del dia martes.\n")
                        elif martes1 != "" and martes2 != "" and martes3 != "":
                            print("El martes esta lleno.\n")
                        
                        break
                else:
                    print("Elija una de las opciones posibles.\n")
        case "2":
            print("Cancelar turno")
            while True:
                elegirDia = input("Ingrese el dia que quiere cancelar su turno Lunes o Martes: ").lower()
                if elegirDia == "martes" or elegirDia == "lunes":
                    nombrePaciente = input("Ingrese el nombre del paciente: ").lower()
                    if elegirDia == "lunes":
                        if lunes1 == nombrePaciente:
                            lunes1 = ""
                            print("Se elimino su turno.\n")
                        elif lunes2 == nombrePaciente:
                            lunes2 = ""
                            print("Se elimino su turno.\n")
                        elif lunes3 == nombrePaciente:
                            lunes3 = ""
                            print("Se elimino su turno.\n")
                        elif lunes4 == nombrePaciente:
                            lunes4 = ""
                            print("Se elimino su turno.\n")
                        elif lunes1 != "" and lunes2 != "" and lunes3 != "" and lunes4 != "":
                            print("No hay turnos registrados el lunes.\n")
                        elif lunes1 != nombrePaciente and lunes2 != nombrePaciente and lunes3 != nombrePaciente and lunes4 != nombrePaciente:
                            print("No hay turnos registrados a tu nombre el día lunes.\n")
                        break
                    elif elegirDia == "martes":
                        if martes1 == nombrePaciente:
                            martes1 = ""
                            print("Se elimino su turno.\n")
                        elif martes2 == nombrePaciente:
                            martes2 = ""
                            print("Se elimino su turno.\n")
                        elif martes3 == nombrePaciente:
                            martes3 = ""
                            print("Se elimino su turno.\n")
                        elif martes1 != "" and martes2 != "" and martes3 != "":
                            print("No tiene turnos a su nombre el día martes.\n")
                        elif martes1 != nombrePaciente and martes2 != nombrePaciente and martes3 != nombrePaciente:
                            print("No hay turnos registrados a tu nombre el día lunes.\n")
                        break
        case "3":
            print("Agenda")
            print("Lunes:")
            print(f"Primer turno: {lunes1}" if lunes1 != "" else "Primer turno: Vacio.")
            print(f"Segundo turno: {lunes2}" if lunes2 != "" else "Segundo turno: Vacio.")
            print(f"Tercer turno: {lunes3}" if lunes3 != "" else "Tercer turno: Vacio.")
            print(f"Cuarto turno: {lunes4}" if lunes4 != "" else "Cuarto turno: Vacio.")
            print("Martes:")
            print(f"Primer turno: {martes1}" if martes1 != "" else "Primer turno: Vacio.")
            print(f"Segundo turno: {martes2}" if martes2 != "" else "Segundo turno: Vacio.")
            print(f"Tercer turno: {martes3}" if martes3 != "" else "Tercer turno: Vacio.")
        case "4":
            print("Ver resumen general")
            diasLunesTurnosVacios = 0
            diasLunesTurnos = 0
            diasMartesTurnosVacios = 0
            diasMartesTurnos = 0
            if lunes1 == "":
                diasLunesTurnosVacios += 1
            if lunes2 == "":
                diasLunesTurnosVacios += 1
            if lunes3 == "":
                diasLunesTurnosVacios += 1
            if lunes4 == "":
                diasLunesTurnosVacios += 1
            if martes1 == "":
                diasMartesTurnosVacios += 1
            if martes2 == "":
                diasMartesTurnosVacios += 1
            if martes3 == "":
                diasMartesTurnosVacios += 1
            if lunes1 != "":
                diasLunesTurnos += 1
            if lunes2 != "":
                diasLunesTurnos += 1
            if lunes3 != "":
                diasLunesTurnos += 1
            if lunes4 != "":
                diasLunesTurnos += 1
            if martes1 != "":
                diasMartesTurnos += 1
            if martes2 != "":
                diasMartesTurnos += 1
            if martes3 != "":
                diasMartesTurnos += 1    
            print(f"El lunes tiene {diasLunesTurnos} turnos dados y {diasLunesTurnosVacios} turnos disponibles.")
            print(f"El martes tiene {diasMartesTurnos} turnos dados y {diasMartesTurnosVacios} turnos disponibles.")
            if diasLunesTurnos == diasMartesTurnos:
                print(f"Los días lunes y martes tienen la misma cantidad de turnos dados con {diasLunesTurnos}.")
            elif diasLunesTurnos < diasMartesTurnos:
                print(f"El día martes tiene más turnos dados que el lunes con {diasMartesTurnos}.")
            else:
                print(f"El día lunes tiene más turnos dados que el martes con {diasLunesTurnos}.")
        case "5":
            print("Gracias por usar nuestro sistema.")
            break