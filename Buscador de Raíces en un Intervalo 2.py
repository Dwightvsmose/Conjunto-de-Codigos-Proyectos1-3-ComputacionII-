# Buscador de Raíces en un Intervalo
# Christian Torres Aguayo

import numpy as np
from scipy.optimize import brentq

def funcion(x):
    # Define aquí la función cuyas raíces quieres encontrar
    return x**3 - 2*x - 5

def encontrar_raices(func, limite_inferior, limite_superior):
    raices = []
    try:
        raiz = brentq(func, limite_inferior, limite_superior)
        raices.append(raiz)
    except ValueError:
        pass
    return raices

def main():
    # Solicitar al usuario el intervalo
    print("Buscador de Raíces en un Intervalo")
    limite_inferior = float(input("Ingrese el límite inferior del intervalo: "))
    limite_superior = float(input("Ingrese el límite superior del intervalo: "))

    # Encontrar las raíces dentro del intervalo utilizando el método de Brent
    raices = encontrar_raices(funcion, limite_inferior, limite_superior)

    # Mostrar las raíces encontradas
    if raices:
        print("Se encontraron las siguientes raíces en el intervalo dado:")
        for i, raiz in enumerate(raices):
            print(f"Raíz {i+1}: {raiz}")
    else:
        print("No se encontraron raíces en el intervalo dado.")

if __name__ == "__main__":
    main()
