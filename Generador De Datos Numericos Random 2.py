import random
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def generate_random_data(num_rows, num_columns, min_value, max_value):
    """
    Generate random numerical data.

    Parameters:
    num_rows (int): Number of rows of data.
    num_columns (int): Number of columns of data.
    min_value (int): Minimum value of the random data.
    max_value (int): Maximum value of the random data.

    Returns:
    str: Random numerical data as a string.
    """
    data = []
    for _ in range(num_rows):
        row = [str(random.randint(min_value, max_value)) for _ in range(num_columns)]
        data.append('\t'.join(row))  # Use tab as delimiter to avoid comma issues
    return '\n'.join(data)

def save_file(data):
    """
    Save the generated data to a text file.

    Parameters:
    data (str): The data to be saved.
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(data)
        messagebox.showinfo("Save File", f"Data saved to {file_path}")

def on_generate():
    try:
        num_columns = int(columns_entry.get())
        num_rows = total_numbers // num_columns
        data = generate_random_data(num_rows, num_columns, min_value=0, max_value=999)
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, data)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of columns")

def on_save():
    data = data_display.get(1.0, tk.END).strip()
    if data:
        save_file(data)
    else:
        messagebox.showerror("No Data", "No data to save. Please generate data first.")

# Create the main window
root = tk.Tk()
root.title("Random Data Generator")

# Create and place the widgets
tk.Label(root, text="Enter the number of columns:").grid(row=0, column=0, padx=10, pady=5)
columns_entry = tk.Entry(root)
columns_entry.grid(row=0, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate", command=on_generate)
generate_button.grid(row=0, column=2, padx=10, pady=5)

data_display = scrolledtext.ScrolledText(root, width=50, height=20)
data_display.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

save_button = tk.Button(root, text="Save As", command=on_save)
save_button.grid(row=2, column=1, pady=10)

# Define total numbers
total_numbers = 5000

# Run the application
root.mainloop()
