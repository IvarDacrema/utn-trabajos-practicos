#Actividad 1
def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    return n * factorial(n - 1)

# Uso del algoritmo general
limite = int(input("Ingrese un número entero para calcular factoriales: "))
for i in range(1, limite + 1):
    print(f"El factorial de {i} es: {factorial(i)}")