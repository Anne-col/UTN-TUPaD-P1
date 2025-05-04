# TP3 - CONDICIONALES
# Alumna: Rebeca

# EJERCICIO 1
# Solicita la edad del usuario y muestra si es mayor de edad
edad = int(input("Ejercicio 1 - ¿Cuántos años tenés? "))
if edad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")

# EJERCICIO 2
# Solicita una nota al usuario y muestra si está aprobado o desaprobado

nota = float(input("Ingresá tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# EJERCICIO 3
# Solicita un número y verifica si es par usando el operador módulo %

numero = int(input("Ingresá un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# EJERCICIO 4
# Clasifica al usuario según su edad

edad = int(input("Ingresá tu edad: "))

if edad < 12:
    print("Categoría: Niño/a")
elif edad < 18:
    print("Categoría: Adolescente")
elif edad < 30:
    print("Categoría: Adulto/a joven")
else:
    print("Categoría: Adulto/a")

# EJERCICIO 5
# Verifica si la longitud de una contraseña está entre 8 y 14 caracteres

contraseña = input("Ingresá una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# EJERCICIO 6
#Evaluar Media, Mediana y Moda
import random
from statistics import mean, median, mode

# Paso 1: Crear la lista
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Paso 2: Calcular los estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Paso 3: Determinar el sesgo
if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
elif media == mediana == moda:
    sesgo = "Sin sesgo"
else:
    sesgo = "No se puede determinar claramente el sesgo"

# Paso 4: Mostrar resultados
print("Lista de números:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Resultado:", sesgo)

# EJERCICIO 7
# Verifica si la frase termina en vocal y agrega un signo de exclamación si es así

frase = input("Ingresá una frase o palabra: ")

# Verificamos la última letra
ultima = frase[-1].lower()

if ultima in "aeiou":
    frase += "!"
    print("Resultado:", frase)
else:
    print("Resultado:", frase)

# EJERCICIO 8
# Transforma el nombre del usuario según la opción elegida

nombre = input("Ingresá tu nombre: ")

print("¿Cómo querés que se muestre tu nombre?")
print("1. Mayúsculas")
print("2. Minúsculas")
print("3. Primera letra en mayúscula")

opcion = input("Elegí una opción (1, 2 o 3): ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción inválida. Por favor, ingresá 1, 2 o 3.")

# EJERCICIO 9
# Clasifica la magnitud de un terremoto según la escala de Richter

magnitud = float(input("Ingresá la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# EJERCICIO 10
#Definir en que epoca del año esta el usuario
# Paso 1: Pedir datos
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿En qué mes estamos? (1-12): "))
dia = int(input("¿Qué día del mes es hoy? (1-31): "))

# Paso 2: Convertir fecha a número para comparar
fecha = mes * 100 + dia

# Paso 3: Determinar estación
if hemisferio == "N":
    if 1221 <= fecha <= 320:
        estacion = "Invierno"
    elif 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if 1221 <= fecha <= 320:
        estacion = "Verano"
    elif 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio inválido"

# Paso 4: Imprimir resultado
print("La estación del año es:", estacion)