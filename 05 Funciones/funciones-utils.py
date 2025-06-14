# Funciones

import math #importamos el modulo, que nos servira mas adelante 

# 1. Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")



# 2. Función que saluda a un usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"



# 3. Función que imprime información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# 4. Área y perímetro de un círculo


def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


# 5. Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600


# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# 7. Operaciones básicas
def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "Indefinido")


# 8. Calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# 10. Calcular promedio de 3 números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

