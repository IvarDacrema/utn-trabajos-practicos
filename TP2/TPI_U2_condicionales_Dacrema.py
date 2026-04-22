from datetime import date

#Actividad 1
print("Actividad 1")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#Actividad 2
print()
print("Actividad 2")
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("desaprobado")

#Actividad 3
print()
print("Actividad 3")
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
  print("Ha ingresado un número par.")
else:
  print("Por favor, ingrese un número par.")

#ACtividad 4
print()
print("Actividad 4")
edad = int(input("Ingrese su edad: "))
if edad < 12 and edad > 0:
  print("Tu eres un/a niño/a.")
elif edad >= 12 and edad < 18:
  print("Tu eres un/a adolescente.")
elif edad >= 18 and edad < 30:
  print("Tu eres un adulto/a joven")
elif edad >= 30:
  print("Tu eres un adulto")
else:
  print("No es un edad posible.")

#Actividad 5
print()
print("Actividad 5")
password = input("Ingrese una contraseña entre 8 y 14 caracteres.")
if len(password) >= 8 and len(password) <= 14:
  print("Ha ingresado una contraseña correcta.")
else:
  print("Por favor, ingrese una contraseña entre 8 y 14 caracteres.")

#Actividad 6
print()
print("Actividad 6")
consumo = float(input("Ingrese su consumo mensual de energía eléctrica en kilovatios (KWh): "))
if consumo <= 0:
  print("Dato incorrecto.")
elif consumo < 150:
  print("Consumo bajo.")
elif consumo <= 300:
  print("Consumo medio.")
else:
  if consumo >= 500:
    print("Consumo demaciado alto, considere medidas de ahorro de energía.")
  else:
    print("Consumo alto.")  

#Actividad 7
print()
print("Actividad 7")
frase = input("Ingrese una frase: ")
letra = frase[-1]
if letra in "aeiouAEIOU":
  print(frase+"!")
else:
  print(frase)

#Acividad 8
print()
print("Actividad 8")
nombre = input("ingrese su nombre: ")
print("""1- Si quiere su nombre en mayúsculas.
2- Si quiere su nombre en minúsculas.
3- Si quiere su nombre con la primera letra mayúscula.""")
numero = int(input("Ingrese una opcion: "))
match numero:
  case 1:
    print(nombre.upper())
  case 2:
    print(nombre.lower())
  case 3:
    print(nombre.title())
  case _:
    print("No es una opción valida.")

#Actividad 9
print()
print("Actividad 9")
magnitud = int(float(input("Ingrese la magnitud del terremoto.")))
match magnitud:
  case 1 | 2:
    print("Muy leve.")
  case 3:
    print("Leve.")
  case 4:
    print("Moderado.")
  case 5:
    print("Fuerte")
  case 6:
    print("Muy Fuerte")
  case 7 | 8 | 9 | 10:
    print("Extremo")
  case _:
    print("No es un registro valido.")

#Actividad 10
print()
print("Actividad 10")
dia = int(input("Ingrese que día esta: "))
mes = input("Ingrese que mes del año es: ").lower()
hemisferio = input("""¿En que hemisferio estas?
Norte.
Sur
""").lower()

match mes:
  case "enero":
    mes = 1
  case "febrero":
    mes = 2
  case "marzo":
    mes = 3
  case "abril":
    mes = 4
  case "mayo":
    mes = 5
  case "junio":
    mes = 6
  case "julio":
    mes = 7
  case "agosto":
    mes = 8
  case "septiembre" | "setiembre":
    mes = 9
  case "octubre":
    mes = 10
  case "noviembre":
    mes = 11
  case "diciembre":
    mes = 12
  case _:
    print("No es un valor valido.")

fechaUsuario = date(2026, mes, dia)

if hemisferio == "norte":
  if fechaUsuario > date(2026, 3, 21) and fechaUsuario <= date(2026, 6, 20):
    print("Primavera.")
  elif fechaUsuario > date(2026, 6, 21) and fechaUsuario <= date(2026, 9, 20):
    print("Verano.")
  elif fechaUsuario > date(2026, 9, 21) and fechaUsuario <= date(2026, 12, 20):
    print("Otoño.")
  else:
    print("invierno.")
elif hemisferio == "sur":
  if fechaUsuario > date(2026, 3, 21) and fechaUsuario <= date(2026, 6, 20):
    print("Otoño.")
  elif fechaUsuario > date(2026, 6, 21) and fechaUsuario <= date(2026, 9, 20):
    print("Invierno.")
  elif fechaUsuario > date(2026, 9, 21) and fechaUsuario <= date(2026, 12, 20):
    print("Primavera.")
  else:
    print("Verano.")
else:
  print("Algún dato no se pudo cargar.")
  pass