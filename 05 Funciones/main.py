#aplicacion de las funciones

import funciones
print("\n=== hola mundo ===")
funciones.imprimir_hola_mundo()

print("\n=== saludar ===")
nombre = input("¿Cuál es tu nombre?, por favor ingresar: ")
print(funciones.saludar_usuario(nombre))

print("\n=== informacion personal ===")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
funciones.informacion_personal(nombre, apellido, edad, residencia)

print("\n=== ejercicio de circulo ===")
radio = float(input("Ingrese el radio del círculo: "))
print("Área:", funciones.calcular_area_circulo(radio))
print("Perímetro:", funciones.calcular_perimetro_circulo(radio))

print("\n=== conversion de segundos a horas===")
segundos = int(input("Ingrese la cantidad de segundos: "))
print("Horas equivalentes:", funciones.segundos_a_horas(segundos))

print("\n=== tabla de multiplicar ===")
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
funciones.tabla_multiplicar(numero)

print("\n=== operaciones matematicas ===")
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
suma, resta, multiplicacion, division = funciones.operaciones_basicas(a, b)
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

print("\n=== calculo del IMC ===")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = funciones.calcular_imc(peso, altura)
print("IMC:", round(imc, 2))

print("\n=== de celsius a fahrenheit ===")
celsius = float(input("Temperatura en Celsius: "))
print("Temperatura en Fahrenheit:", funciones.celsius_a_fahrenheit(celsius))

print("\n=== calculo de promedio ===")
a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))
print("Promedio:", funciones.calcular_promedio(a, b, c))
