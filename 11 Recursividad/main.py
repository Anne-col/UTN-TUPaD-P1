
from funciones_recursivas_utils import factorial, fibonacci, potencia, decimal_a_binario, es_palindromo, suma_digitos, contar_bloques, contar_digito

# Ejercicio 1
n = int(input("Ingresá un número: "))
for i in range(1, n + 1):
    print(f"Factorial de {i} es {factorial(i)}")
  

# Ejercicio 2
pos = int(input("¿Hasta qué posición querés ver la serie Fibonacci?: "))
for i in range(pos):
    print(fibonacci(i), end=" ")
print()


# Ejercicio 3
base = int(input("Base: "))
expo = int(input("Exponente: "))
print(f"{base}^{expo} = {potencia(base, expo)}")

# Ejercicio 4
dec = int(input("Número decimal a convertir en binario: "))
print(f"Binario: {decimal_a_binario(dec) or '0'}")

# Ejercicio 5
palabra = input("Ingresá una palabra: ")
print("Es palíndromo" if es_palindromo(palabra) else "No es palíndromo")

# Ejercicio 6
n = int(input("Número para sumar sus dígitos: "))
print(f"Suma de dígitos: {suma_digitos(n)}")

# Ejercicio 7
niveles = int(input("Cantidad de bloques en el nivel más bajo: "))
print(f"Total de bloques: {contar_bloques(niveles)}")

# Ejercicio 8
numero = int(input("Número en el que contar dígitos: "))
dig = int(input("Dígito a contar: "))
print(f"Aparece {contar_digito(numero, dig)} veces")
