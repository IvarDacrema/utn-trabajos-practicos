#Actividad 1
print("¡¡Hola Mundo!!")

#Actividad 2
nombre = input("¿Cuál es tu nombre? ")
print("¡Hola " + nombre + "!")

#Actividad 3
nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuál es tu edad? ")
localidad = input("¿En que pais vives? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y soy de {localidad}.")

#Actividad 4
print("Vamos a calcular el area y el perimetro de un circulo.")
radio = float(input("Ingrese el radio del circulo: "))
print(f"El area del circulo es: {3.14 * (radio ** 2)} y el perimetro es: {2 * 3.14 * radio}.")

#Actividad 5
print("Ingrese la cantidad de segundos que quiere que se pasen a horas.")
segundos = int(input("Ingrese la cantidad de segundos que quiere calcular: "))
print(f"La cantidad de segundo que ingresaste son {segundos//3600} horas.")

#Actividad 6
print("Imprimir tabla de multplicar del numero que elijas.")
numeroElegido = int(input("Ingrese en numero que desea saber la tabla de multiplicar del 1 al 10:  "))
print("Resultados:")
print(f"{numeroElegido} * 1 = {numeroElegido * 1}")
print(f"{numeroElegido} * 2 = {numeroElegido * 2}")
print(f"{numeroElegido} * 3 = {numeroElegido * 3}")
print(f"{numeroElegido} * 4 = {numeroElegido * 4}")
print(f"{numeroElegido} * 5 = {numeroElegido * 5}")
print(f"{numeroElegido} * 6 = {numeroElegido * 6}")
print(f"{numeroElegido} * 7 = {numeroElegido * 7}")
print(f"{numeroElegido} * 8 = {numeroElegido * 8}")
print(f"{numeroElegido} * 9 = {numeroElegido * 9}")
print(f"{numeroElegido} * 10 = {numeroElegido * 10}")

#Actividad 7
print("Ingrese 2 numero distintos de 0 (cero) para que realicemos distintas operaciones matematicas.")
numero1 = int(input("Ingrese el primero numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
print("Resultados:")
print(f"Suma: {numero1} + {numero2}: {numero1+numero2}")
print(f"Resta: {numero1} - {numero2}: {numero1-numero2}")
print(f"Division: {numero1} / {numero2}: {numero1/numero2}")
print(f"Division entera: {numero1} // {numero2}: {numero1//numero2}")
print(f"Modulo: {numero1} % {numero2}: {numero1%numero2}")
print(f"Multiplicación: {numero1} * {numero2}: {numero1*numero2}")
print(f"Potenciación: {numero1} ** {numero2}: {numero1**numero2}")

#Actividad 8
print("Calculamos el IMC")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su peso en metros: "))
print(f"Su indice de masa corporal es de: {peso/(altura**2)}")

#Actividad 9
print("Pasemos de Celsius a Farhrenheit.")
gradosCelsius = float(input("Ingrese los grados celcius que quiere transformar a farhrenheit: "))
print(f"Los {gradosCelsius} celsius son {9/5*gradosCelsius+32} farhrenheit.")

#Actividad 10
print("Ingrese 3 numeros para sacar su promedio.")
numero2 = float(input("Ingrese el primer numero: "))
numero3 = float(input("Ingrese el segundo numero: "))
numero1 = float(input("Ingrese el tercer numero: "))
print(f"El promedio de los 3 numeros es {(numero1+numero2+numero3)/3}")