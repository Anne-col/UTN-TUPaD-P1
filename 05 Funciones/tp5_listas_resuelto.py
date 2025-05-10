# Práctico 5: Listas
#alumna: Coletti Rebeca Anneris

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4
multiplo_4 = list(range(4, 101, 4)) #defino en que numero comienza, el numero que no incluira y el salto que debe hacer que en este caso es de 4 en 4
print("Ejercicio 1 - lista con los Múltiplos de 4 (del 1 al 100)):", multiplo_4)

# 2) Crear una lista con cinco elementos y mostrar el penúltimo
gustos = ["chocolate", "vainilla", "frutilla", "maracuya", "pistachos"] #defino la lista y los gustos dentro
print("Ejercicio 2 - lista que expresa el penultimo elemento:", gustos[-2])

# 3) Crear lista vacía y agregar tres palabras con append
lista_vacia = [] #creo la lista vacia
lista_vacia.append("sol") #agrego el primer elemento y luego los otros de la misma manera
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("Ejercicio 3 - Lista con elementos agregados:", lista_vacia)

# 4) Reemplazar segundo y último valor en lista de animales
animales = ["perro", "gato", "conejo", "pez"] #defino una lista inicial
animales[1] = "loro"  # cambio el segundo elemento
animales[-1] = "oso"  # cambio el último elemento
print("Ejercicio 4 - Lista con las modificaciones solicitadas:", animales)

# 5) Este ejercicio pide analizar un programa
print("Ejercicio 5 -se crea una lista con elementos, la funcion max reconoce ell valor mas grande, remove lo elimina de la lista y finalmente se imprimer la lista sin ese numero")

# 6) Crear una lista con números del 10 al 30 con saltos de 5 y mostrar los dos primeros
lista_saltos = list(range(10, 31, 5)) #defino que arranca con 10 y termina con 30 (ya que el 31 no se debe incluir), defino el salto de a 5
print("Ejercicio 6 - los dos primeros elementos de la lista son:", lista_saltos[:2])

# 7) Reemplazar los dos valores centrales de la lista autos
autos = ["sedan", "polo", "suran", "gol"] #defino la lista
autos[1:3] = ["camioneta", "convertible"] # defino que lementos quiero mostrar
print("Ejercicio 7 - los elemtos centrales de la lista autos son:", autos)

# 8) Crear lista dobles con el doble de 5, 10 y 15
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Ejercicio 8 - esta es la lista que contiene el doble de 5, 10 y 15:", dobles)

# 9) Modificar la lista de compras
#con la lista definida:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")
# b) Reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"
# c) Eliminar "pan"
compras[0].remove("pan")
print("Ejercicio 9 - la lista de compras modificadas es:", compras)

# 10) Crear lista anidada con valores específicos
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("Ejercicio 10 - la lista anidada es:", lista_anidada)
