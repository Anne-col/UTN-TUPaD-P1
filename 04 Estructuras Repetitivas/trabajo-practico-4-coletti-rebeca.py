# TP4 - Estructuras Repetitivas
# Autor: Coletti Rebeca
# 1. Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
print("Ejercicio 1:")

# Usamos un bucle for para contar desde 0 hasta 100 (el 101 no se incluye)
for i in range(101):
    print(i)  # Mostramos el valor actual de 'i' en cada vuelta del bucle



# 2. Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 
print("Ejercicio 2:")

# Le pedimos al usuario un número entero
numero = int(input("Escribí un número entero: "))

# Si el número es negativo, lo pasamos a positivo para contar los dígitos igual
if numero < 0:
    numero = -numero

# Empezamos contando desde 0
cantidad_digitos = 0

# Si el número es 0, entonces tiene 1 solo dígito
if numero == 0:
    cantidad_digitos = 1
else:
    # Mientras el número sea mayor que 0
    while numero > 0:
        numero = numero // 10  # Le sacamos el último dígito
        cantidad_digitos += 1  # Sumamos 1 al contador

# Mostramos el resultado
print("La cantidad de dígitos es:", cantidad_digitos)

# 3.Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores. 
print("Ejercicio 3:")
# Pedimos al usuario dos números enteros
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

sumatoria = 0  # Inicializamos la suma

# Usamos range desde el menor +1 hasta el mayor (sin incluirlo)
for i in range(min(num1, num2) + 1, max(num1, num2)):
    sumatoria += i  # Sumamos cada número en el rango

print("La suma es:", sumatoria)

# 4.Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 
print("Ejercicio 4:")
# Pedimos el primer número
n = int(input("Ingrese un número (0 para finalizar): "))

total = 0  # Total acumulado

# Mientras el número no sea 0, seguimos sumando
while n != 0:
    total += n  # Lo sumamos al total
    n = int(input("Ingrese un número (0 para finalizar): "))  # Pedimos otro número

# Cuando se ingresa 0, salimos del bucle
print("Total acumulado:", total)

# 5. Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 
import random  # Esto permite generar números aleatorios

print("Ejercicio 5:")

numero_secreto = random.randint(0, 9)  # El programa elige un número al azar entre 0 y 9
cantidad_intentos = 0  # Empezamos con 0 intentos

adivinado = False  # Creamos una variable para controlar si adivinó o no

while not adivinado:  # Mientras no haya adivinado...
    numero_usuario = int(input("Adivine el número (0-9): "))  # Pedimos un número al usuario
    cantidad_intentos = cantidad_intentos + 1  # Sumamos 1 intento
    if numero_usuario == numero_secreto:
        adivinado = True  # Si acertó, cambiamos la variable a True

# Fuera del bucle mostramos cuántos intentos le llevó
print("¡Correcto! Número de intentos:", cantidad_intentos)

# 6.Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente. 

print("Ejercicio 6:")

# Usamos un bucle for para contar desde 100 hasta 0, bajando de a 1, sin incluir -1
for i in range(100, -1, -1):
    
    # Verificamos si el número es par (es divisible por 2)
    if i % 2 == 0:
        
        # Si es par, lo mostramos en pantalla
        print(i)

# 7. Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
print("Ejercicio 7:")

# Pedimos al usuario que ingrese un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Inicializamos la variable 'suma' en 0, donde vamos a ir acumulando los valores
sumatoria = 0

# Creamos un bucle que va desde 0 hasta n (inclusive), sumando todos esos números
for i in range(n + 1):
    sumatoria += i  # En cada vuelta, sumamos el valor actual de 'i' a la variable 'suma'

# Mostramos el resultado final de la suma
print("La suma es:", sumatoria)

# 8.Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
print("Ejercicio 8:")

# Empezamos todos los contadores en 0
pares = 0
impares = 0
positivos = 0
negativos = 0

# Repetimos el proceso 10 veces (podés cambiar a 100 si querés después)
# Usamos range(1, 11) para contar del 1 al 10
for i in range(1, 11):
    
    # Pedimos un número al usuario
    numero = int(input("Ingrese el número " + str(i) + ": "))

    # Verificamos si el número es par
    if numero % 2 == 0:
        pares = pares + 1  # sumamos 1 a los pares
    else:
        impares = impares + 1  # sumamos 1 a los impares

    # Verificamos si el número es positivo o negativo
    if numero >= 0:
        positivos = positivos + 1  # sumamos 1 a los positivos
    else:
        negativos = negativos + 1  # sumamos 1 a los negativos

# Mostramos los resultados
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# 9. Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor). 
print("Ejercicio 9:")

# Inicializamos la variable total, que va a acumular la suma de los números
total = 0

# Definimos cuántos números va a ingresar el usuario (se puede cambiar a 100 luego)
cantidad = 5

# Repetimos la carga de números la cantidad de veces que indicamos
for i in range(cantidad):

    # En cada vuelta pedimos un número y lo sumamos al total
    numero = int(input("Ingrese el número " + str(i + 1) + ": "))
    total = total + numero  # Acumulamos el número en la variable total

# Calculamos el promedio (media) dividiendo el total por la cantidad de números
media = total / cantidad

# Mostramos el resultado del promedio
print("La media es:", media)

# 10. Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
print("Ejercicio 10:")
# Pedimos al usuario que ingrese un número entero como texto
numero = input("Ingrese un número entero: ")

# Creamos una variable vacía donde vamos a ir guardando el número invertido
invertido = ""

# Recorremos cada carácter del número, pero empezando desde el final hacia el principio
for letra in numero:
    invertido = letra + invertido  # Vamos agregando cada letra al principio

# Mostramos el número invertido
print("Número invertido:", invertido)