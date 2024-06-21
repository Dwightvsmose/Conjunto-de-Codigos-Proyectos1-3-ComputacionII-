import tkinter as tk
from tkinter import filedialog, messagebox
import random
import string

def generar_texto(num_lineas, palabras_por_linea):
    vocales = 'AEIOUaeiou'
    consonantes = ''.join(set(string.ascii_letters) - set(vocales))
    texto = []

    for _ in range(num_lineas):
        linea = []
        for _ in range(palabras_por_linea):
            if random.choice([True, False]):
                palabra = ''.join(random.choices(string.ascii_letters, k=random.randint(1, 9)))
            else:
                palabra = str(random.randint(1, 999999999))
            linea.append(palabra)
        texto.append(' '.join(linea))
    
    return '\n'.join(texto)

def guardar_archivo():
    num_lineas = int(entry_num_lineas.get())
    palabras_por_linea = int(entry_palabras_por_linea.get())
    
    texto_generado = generar_texto(num_lineas, palabras_por_linea)
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(texto_generado)
        messagebox.showinfo("Archivo guardado", f"Archivo guardado en: {file_path}")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Generador de Datos Aleatorios")

tk.Label(root, text="Número de líneas:").grid(row=0, column=0, padx=10, pady=10)
entry_num_lineas = tk.Entry(root)
entry_num_lineas.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Palabras por línea:").grid(row=1, column=0, padx=10, pady=10)
entry_palabras_por_linea = tk.Entry(root)
entry_palabras_por_linea.grid(row=1, column=1, padx=10, pady=10)

btn_guardar = tk.Button(root, text="Guardar como...", command=guardar_archivo)
btn_guardar.grid(row=2, columnspan=2, pady=20)

root.mainloop()
