# Christian Torres A.
# Analizador de Archivos de Texto y Números
# Solicitar el nombre del archivo al usuario
nombre_archivo = input("Introduce el nombre del archivo (incluye la extensión): ")

# Leer el contenido del archivo
with open(nombre_archivo, 'r') as archivo:
    lineas = archivo.readlines()

# Contar el número de líneas en el archivo
num_lineas = len(lineas)
print(f"El archivo '{nombre_archivo}' contiene {num_lineas} líneas.")

# Contar el número total de palabras y números
num_palabras = 0
num_numeros = 0
for linea in lineas:
    palabras = linea.split()
    for palabra in palabras:
        if palabra.isdigit():
            num_numeros += 1
        else:
            num_palabras += 1
print(f"Número total de palabras en el archivo: {num_palabras}")
print(f"Número total de números en el archivo: {num_numeros}")

# Contar palabras que comienzan con vocales y números específicos
vocales = 'AEIOUaeiou'
numeros = '123456789'
conteo_vocales = {v: 0 for v in vocales}
conteo_numeros = {n: 0 for n in numeros}

for linea in lineas:
    palabras = linea.split()
    for palabra in palabras:
        if palabra[0] in conteo_vocales:
            conteo_vocales[palabra[0]] += 1
        if palabra[0] in conteo_numeros:
            conteo_numeros[palabra[0]] += 1

for vocal in vocales:
    print(f"Palabras que comienzan con '{vocal}': {conteo_vocales[vocal]}")

for numero in numeros:
    print(f"Palabras que comienzan con '{numero}': {conteo_numeros[numero]}")

# Contar palabras y números por longitud
longitud_palabras = {n: 0 for n in range(1, 10)}
longitud_numeros = {n: 0 for n in range(1, 10)}

for linea in lineas:
    palabras = linea.split()
    for palabra in palabras:
        longitud = len(palabra)
        if palabra.isdigit():
            if 1 <= longitud <= 9:
                longitud_numeros[longitud] += 1
        else:
            if 1 <= longitud <= 9:
                longitud_palabras[longitud] += 1

print("Recuento de palabras por longitud:")
for longitud, conteo in longitud_palabras.items():
    print(f"Palabras de {longitud} letras: {conteo}")

print("Recuento de números por longitud:")
for longitud, conteo in longitud_numeros.items():
    print(f"Números de {longitud} cifras: {conteo}")

# Ordenar palabras alfabéticamente y en orden inverso, y números de mayor a menor
palabras_lista = []
numeros_lista = []

for linea in lineas:
    palabras = linea.split()
    for palabra in palabras:
        if palabra.isdigit():
            numeros_lista.append(int(palabra))
        else:
            palabras_lista.append(palabra)

palabras_ordenadas_az = sorted(palabras_lista)
palabras_ordenadas_za = sorted(palabras_lista, reverse=True)
numeros_ordenados_mayor = sorted(numeros_lista)
numeros_ordenados_menor = sorted(numeros_lista, reverse=True)

print("Palabras ordenadas alfabéticamente:")
print(palabras_ordenadas_az)

print("Palabras ordenadas en orden inverso:")
print(palabras_ordenadas_za)

print("Números ordenados de menor a mayor:")
print(numeros_ordenados_mayor)

print("Números ordenados de mayor a menor:")
print(numeros_ordenados_menor)

# Promedio de los números
total_numeros = sum(numeros_lista)
if len(numeros_lista) > 0:
    promedio_numeros = total_numeros / len(numeros_lista)
else:
    promedio_numeros = 0

print(f"El promedio de los números es: {promedio_numeros}")
