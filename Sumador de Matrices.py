# Sumador de Matrices
# Christian Torres Aguayo

# Solicitar al usuario las dimensiones de la matriz A
print("Ingrese las dimensiones de la matriz A:")
filas_A = int(input("Número de filas de A: "))
columnas_A = int(input("Número de columnas de A: "))

# Solicitar al usuario las dimensiones de la matriz B
print("\nIngrese las dimensiones de la matriz B:")
filas_B = int(input("Número de filas de B: "))
columnas_B = int(input("Número de columnas de B: "))

# Verificar si las dimensiones son compatibles
if filas_A == filas_B and columnas_A == columnas_B:
    # Ingresar los elementos de la matriz A
    print("\nIngrese los elementos de la matriz A:")
    matriz_A = []
    for i in range(filas_A):
        filaA = []
        for j in range(columnas_A):
            elemento = float(input(f"Ingrese el elemento ({i+1},{j+1}) de A: "))
            filaA.append(elemento)
        matriz_A.append(filaA)

    # Ingresar los elementos de la matriz B
    print("\nIngrese los elementos de la matriz B:")
    matriz_B = []
    for i in range(filas_B):
        filaB = []
        for j in range(columnas_B):
            elemento = float(input(f"Ingrese el elemento ({i+1},{j+1}) de B: "))
            filaB.append(elemento)
        matriz_B.append(filaB)

    # Sumar las matrices
    suma = []
    for i in range(filas_A):
        fila_suma = []
        for j in range(columnas_A):
            fila_suma.append(matriz_A[i][j] + matriz_B[i][j])
        suma.append(fila_suma)

    # Mostrar la suma de las matrices
    print("\nLa suma de las matrices A y B es:")
    
    for entrada in suma:
        print(entrada)
else:
    print("Las matrices no tienen dimensiones compatibles para la suma.")
