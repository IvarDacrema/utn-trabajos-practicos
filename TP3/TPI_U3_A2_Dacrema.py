#Ejercicio 2 - Acceso al Campus y Menú Seguro
usuarioCorrecto = "alumno"
claveCorrecto = "python123"
maxError = 3
contadorDeErrores = 0
opcionesElegidas = "0"

while contadorDeErrores < maxError:
    usuario = input("Ingrese su usuario: ")
    if usuarioCorrecto == usuario:
        clave = input("Ingrese su contraseña: ")
        if clave == claveCorrecto:
            while opcionesElegidas < "4":
                opcionesElegidas = input("""                Menu
                Ingrese el numero de la opcion a la cual desea ingresar:
                1- Ver estado de inscripcion.
                2- Cambiar clave.
                3- Mostrar mensaje motivacional.
                4- Salir.
                Eliga la opción deseada: """)

                if opcionesElegidas.isdigit() and int(opcionesElegidas) >= 1 and int(opcionesElegidas) <= 4:
                    match opcionesElegidas:
                        case "1":
                            print("Inscripto.\n")
                        case "2":
                            while True:
                                claveNueva = input("Ingrese nueva clave: ")
                                confirmacionClave = input("Ingrese nuevamente la nueva clave: ")
                                if claveNueva == confirmacionClave and len(claveNueva) >= 6:
                                    claveCorrecto = claveNueva
                                    print(f"Contraseña actualizada, su contrasela nueva es: {claveCorrecto}")
                                    break
                                elif len(claveNueva) < 6:
                                    print("La contraseña debe ser minimo de 6 caracteres.")
                                else:
                                    print("La contraseñas no coinciden.")
                        case "3":
                            print("¡¡¡La mejor manera de predecir el futuro es crearlo!!!\n")
                        case "4":
                            contadorDeErrores = 10
                            break
                else:
                    print("Opción no valida, vuelva a intentarlo.")
                    opcionesElegidas = "0"
        else:
            contadorDeErrores += 1
            print(f"Error n° {contadorDeErrores}, quedan {maxError-contadorDeErrores} intentos.")
            print("Clave incorrecta.")
    else:
        contadorDeErrores += 1
        print(f"Error n° {contadorDeErrores}, quedan {maxError-contadorDeErrores} intentos.")
        print("Usuario incorrecto.")

if contadorDeErrores == maxError:
    print("Usuario bloqueado, se realizaron 3 intentos incorrectos.")
elif contadorDeErrores == 10:
    print("Gracias por usar nuestro sistema.")
