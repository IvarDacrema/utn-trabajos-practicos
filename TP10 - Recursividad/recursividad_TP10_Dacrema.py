#Actividad 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

limite = int(input("Ingrese un número entero para calcular factoriales: "))
for i in range(1, limite + 1):
    print(f"El factorial de {i} es: {factorial(i)}")

# Ejercicio 2
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese la posición hasta donde desea ver la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")

# Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("\n\nIngrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base} elevado a la {exponente} es: {potencia(base, exponente)}")

# Ejercicio 4
def decimal_a_binario(n):
    if n <= 1:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)

numero = 10
print(f"El número {numero} en binario es: {decimal_a_binario(numero)}")

# Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

print(f"¿'radar' es palíndromo?: {es_palindromo('radar')}")
print(f"¿'python' es palíndromo?: {es_palindromo('python')}")

# Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

print(f"La suma de los dígitos de 1234 es: {suma_digitos(1234)}")

# Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

print(f"Bloques necesarios para nivel 4: {contar_bloques(4)}")

# Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    coincidencia = 1 if ultimo_digito == digito else 0
    
    return coincidencia + contar_digito(numero // 10, digito)

print(f"El número 2 en 12233421 aparece {contar_digito(12233421, 2)} veces")