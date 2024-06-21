# Analizador Avanzado de Datos Numéricos
# Christian Torres Aguayo

try:

    # Solicitar al usuario el nombre del archivo de datos
    archivo = input("Ingrese el nombre del archivo de datos: ")
    
    # Abrir el archivo en modo lectura y contar las líneas
    with open(archivo, 'r') as datos:
        lineas = datos.readlines()
        num_lineas = len(lineas)
        print(f"EL ARCHIVO '{archivo}' TIENE {num_lineas} LINEAS.")
    
    # Contar el número total de números en el archivo
    num_numeros = 0
    i = 0
    for renglon in lineas:
        numeros = renglon.split()
        num_numeros += len(numeros)
        i += 1
    
    print(f"EL NUMERO TOTAL DE NUMEROS EN EL ARCHIVO {archivo} ES: {num_numeros}")
    
    # Contar la cantidad de números que comienzan con cada dígito del 1 al 9
    numeros_con_1 = sum(1 for linea in lineas for numero in linea.split() if numero.startswith('1'))
    print(f"EL ARCHIVO '{archivo}' TIENE {numeros_con_1} NUMEROS QUE COMIENZAN CON UN '1'")
    
    numeros_con_2 = sum(1 for linea in lineas for numero in linea.split() if numero.startswith('2'))
    print(f"EL ARCHIVO '{archivo}' TIENE {numeros_con_2} NUMEROS QUE COMIENZAN CON UN '2'")
    
    numeros_con_3 = sum(1 for linea in lineas for numero in linea.split() if numero.startswith('3'))
    print(f"EL ARCHIVO '{archivo}' TIENE {numeros_con_3} NUMEROS QUE COMIENZAN CON UN '3'")
    
    numeros_con_4 = sum(1 for linea in lineas for numero in linea.split() if numero.startswith('4'))
    print(f"EL ARCHIVO '{archivo}' TIENE {numeros_con_4} NUMEROS QUE COMIENZAN CON UN '4'")
    
    numeros_con_5 = sum(1 for linea in lineas for numero in linea.split() if numero.startswith('5'))
    print(f"EL ARCHIVO '{archivo}' TIENE {numeros_con_5} NUMEROS QUE COMIENZAN CON UN '5'")
    
    numeros_con_6 = sum(1 for linea in lineas for numero in linea.split() if numero.startswith('6'))
    print(f"EL ARCHIVO '{archivo}' TIENE {numeros_con_6} NUMEROS QUE COMIENZAN CON UN '6'")
    
    numeros_con_7 = sum(1 for linea in lineas for numero in linea.split() if numero.startswith('7'))
    print(f"EL ARCHIVO '{archivo}' TIENE {numeros_con_7} NUMEROS QUE COMIENZAN CON UN '7'")
    
    numeros_con_8 = sum(1 for linea in lineas for numero in linea.split() if numero.startswith('8'))
    print(f"EL ARCHIVO '{archivo}' TIENE {numeros_con_8} NUMEROS QUE COMIENZAN CON UN '8'")
    
    numeros_con_9 = sum(1 for linea in lineas for numero in linea.split() if numero.startswith('9'))
    print(f"EL ARCHIVO '{archivo}' TIENE {numeros_con_9} NUMEROS QUE COMIENZAN CON UN '9'")
    
    # Contar la cantidad de números de una, dos, tres, cuatro, cinco y seis cifras
    una_cifra = dos_cifras = tres_cifras = cuatro_cifras = cinco_cifras = seis_cifras = 0

    for linea in lineas:
        numeros = linea.split()
        for numero in numeros:
            if len(numero) == 1:
                una_cifra += 1
            elif len(numero) == 2:
                dos_cifras += 1
            elif len(numero) == 3:
                tres_cifras += 1
            elif len(numero) == 4:
                cuatro_cifras += 1
            elif len(numero) == 5:
                cinco_cifras += 1
            elif len(numero) == 6:
                seis_cifras += 1

    # Imprimir el recuento de números según su longitud
    print("RECUENTO DE LAS CIFRAS:")
    print(f" EL ARCHIVO {archivo} TIENE {una_cifra} NUMEROS DE UNA CIFRA")
    print(f" el archivo {archivo} tiene {dos_cifras} numeros de dos cifras")
    print(f" el archivo {archivo} tiene {tres_cifras} numeros de tres cifras")
    print(f" el archivo {archivo} tiene {cuatro_cifras} numeros de cuatro cifras")
    print(f" el archivo {archivo} tiene {cinco_cifras} numeros de cinco cifras")
    print(f" el archivo {archivo} tiene {seis_cifras} numeros de seis cifras")
    
    # Ordenar todos los números de menor a mayor y de mayor a menor
    todos_los_numeros = [] 
    for linea in lineas:
        numeros = linea.split()
        todos_los_numeros.extend(numeros)

    todos_los_numeros_decimales = [float(numero) for numero in todos_los_numeros]

    todos_los_numeros_decimales.sort()
    uno_nueve = [numero for numero in todos_los_numeros_decimales]

    print(f"LOS NUMEROS ORDENADOS DE MENOR A MAYOR: {uno_nueve}")

    todos_los_numeros_decimales.sort(reverse=True)
    nueve_uno = [numero for numero in todos_los_numeros_decimales]

    print(f"LOS NUMEROS ORDENADOS DE MAYOR A MENOR: {nueve_uno}")
    
    # Calcular y mostrar el promedio de los números
    promedio = sum(todos_los_numeros_decimales) / len(todos_los_numeros_decimales)
    print(f"EL PROMEDIO ES {promedio}")
    
    # Función para comparar la distancia de un número al promedio
    def comparar_distancia(lugar):
        return abs(lugar - promedio)

    # Ordenar los números según su distancia al promedio
    todos_los_numeros_decimales.sort(key=comparar_distancia)

    print(f"Lista de números ordenados según la distancia al promedio = {promedio}")
    print(todos_los_numeros_decimales)

     # Mostrar la distancia de cada número al promedio
    i = 0
    while i < len(todos_los_numeros_decimales):
        print("El número en el espacio", i + 1, "de la lista es:", todos_los_numeros_decimales[i], "y su distancia al promedio es:", comparar_distancia(todos_los_numeros_decimales[i]))
        i += 1
except Exception as e:
   print("Se produjo un error:", e)
