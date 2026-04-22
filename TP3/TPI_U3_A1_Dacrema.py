#Ejercicio 1 - Caja del kiosco
print("Caja del Kiosco")
nombre = ""
cantidadDeProductos = 0
total = 0
totalConDescuento = 0
ahorro = 0

while True:
    nombre = input("Ingrese el nombre del cliente: ")
    if nombre.isalpha():
        nombre = nombre.title()
        break
    else:
        print("Error: El nombre solo debe contener letras.")

while True:
    cantidadDeProductos = input("Ingrese la cantidad de productos: ")
    if cantidadDeProductos.isdigit() and int(cantidadDeProductos) > 0:
        break
    else:
        print("A ingresado un valor no valido, debe ser un numero entero y positivo.")

for i in range(int(cantidadDeProductos)):
    precio = ""
    descuento = ""
    while True:
        precio = input(f"Ingrese el precio del producto {i+1}: ")
        if precio.isdigit() and float(precio) > 0:
            break
        else:
            print("Ingreso el precio de forma incorrecta, debe ser un numero mayor a 0.")
    while True:
        descuento = input(f"¿El producto {i+1} tiene descuento? Si o NO: ").lower()
        if descuento == "si":
            totalConDescuento += (float(precio)*0.9)
            total += float(precio)
            ahorro += (float(precio)*0.1)
            break
        elif descuento == "no":
            totalConDescuento += float(precio)
            total += float(precio)
            break
        else:
            print("Ingrese un valor valido, si para cuando tiene descuento o no cuando no tiene descuento.")
    print(f"Producto {i+1} - Precio: {float(precio):.2f} - Descuento (S/N): {descuento}")

print(f"Total sin descuento: ${float(total):.2f}")
print(f"Total con descuento: ${float(totalConDescuento):.2f}")
print(f"Ahorro: ${float(ahorro):.2f}")
print(f"Promedio por producto: ${(float(totalConDescuento)/float(cantidadDeProductos)):.2f}")
