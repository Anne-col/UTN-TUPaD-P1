# -----------------------------------------
# Ejercicio 1: Agregar frutas al diccionario
# -----------------------------------------
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300



# -----------------------------------------
# Ejercicio 2: Actualizar precios
# -----------------------------------------

print("Antes de pasar al Ejercicio 2, mostramos como queda el Ejercicio 1:", precios_frutas)

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800


# -----------------------------------------
# Ejercicio 3: Lista de frutas (solo claves)
# -----------------------------------------

print("Antes de pasar al Ejercicio 2, mostramos como queda el Ejercicio 2:", precios_frutas)

frutas = list(precios_frutas.keys())
print("Se muestra el resultado del Ejercicio 3:", frutas)

# -----------------------------------------
# Ejercicio 4: Agenda de contactos
# -----------------------------------------
agenda = {}
for i in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input("Ingresá su número de teléfono: ")
    agenda[nombre] = numero

buscar = input("¿Qué contacto querés buscar? ")
if buscar in agenda:
    print(f"El número de {buscar} es: {agenda[buscar]}")
else:
    print("Ese contacto no está en la agenda.")

# -----------------------------------------
# Ejercicio 5: Palabras únicas y conteo
# -----------------------------------------
frase = input("Escribí una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("Conteo de palabras:", conteo)

# -----------------------------------------
# Ejercicio 6: Promedios de alumnos
# -----------------------------------------
notas_alumnos = {}
for i in range(3):
    nombre = input("Ingresá el nombre del alumno: ")
    print(f"Ingresá 3 notas para {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    notas_alumnos[nombre] = (nota1, nota2, nota3)

print("Promedios:")
for alumno, notas in notas_alumnos.items():
    promedio = sum(notas) / 3
    print(f"{alumno}: {promedio:.2f}")

# -----------------------------------------
# Ejercicio 7: Sets de estudiantes
# -----------------------------------------
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

print("Ambos parciales:", parcial1 & parcial2)
print("Solo uno de los dos:", parcial1 ^ parcial2)
print("Al menos uno:", parcial1 | parcial2)

# -----------------------------------------
# Ejercicio 8: Gestión de stock
# -----------------------------------------
stock = {"lapicera": 10, "cuaderno": 5, "goma": 8}
producto = input("Ingresá un producto: ")

if producto in stock:
    print(f"Stock actual: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto nuevo. Ingresá stock inicial: "))
    stock[producto] = nuevo_stock

print("Stock final:", stock)

# -----------------------------------------
# Ejercicio 9: Agenda con tuplas
# -----------------------------------------
agenda_eventos = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "14:00"): "Clase de Python",
    ("Miércoles", "09:00"): "Consulta médica"
}

for clave, evento in agenda_eventos.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

# -----------------------------------------
# Ejercicio 10: Invertir diccionario
# -----------------------------------------
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

capitales = {}
for pais, capital in paises.items():
    capitales[capital] = pais

print("Diccionario invertido (capital: país):", capitales)