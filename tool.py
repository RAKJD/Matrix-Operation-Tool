import numpy as np
import tkinter as tk
from tkinter import messagebox

# function to extract matrix value from user input.
def get_matrix_from_entries(entries, rows, cols):
    """
    Extracts value from input fields and converts to numpy array.
    Invalid inputs handled by displaying error message.
    """
    try:
        matrix = [[float(entries[r][c].get()) for c in range(cols)] for r in range(rows)]
        return np.array(matrix)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")
        return None

# function to perform selected matrix operations.
def perform_operation():
    """
    Retrieves matrix dimensions and user inputs.
    Performs the selected operation.
    Displayes result.
    Errors due to invalid operation selection is handled by displaying error msg.
    """
    try:
        rows_a = int(row_a_entry.get())
        cols_a = int(col_a_entry.get())
        rows_b = int(row_b_entry.get())
        cols_b = int(col_b_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid dimensions!")
        return
    
    # validate input for operation requiring two matrices.
    if operation.get() in ["Addition", "Subtraction", "Multiplication"]:
        if not (rows_a and cols_a and rows_b and cols_b):
            messagebox.showerror("Input Error", "Please enter valid dimensions for both matrices!")
            return
        matrix_a = get_matrix_from_entries(entries_a, rows_a, cols_a)
        matrix_b = get_matrix_from_entries(entries_b, rows_b, cols_b)
        if matrix_a is None or matrix_b is None:
            return
    # validate input for single matrix operations.
    else: 
        if not (rows_a and cols_a):
            messagebox.showerror("Input Error", "Please enter valid dimensions for Matrix A!")
            return
        matrix_a = get_matrix_from_entries(entries_a, rows_a, cols_a)
        if matrix_a is None:
            return

    try:
        # performs the selectex operation.
        # error is handled by displaying error message.
        if operation.get() == "Addition":
            if matrix_a.shape == matrix_b.shape:
                result = matrix_a + matrix_b
            else:
                raise ValueError("Matrix dimensions must match for addition!")
        elif operation.get() == "Subtraction":
            if matrix_a.shape == matrix_b.shape:
                result = matrix_a - matrix_b
            else:
                raise ValueError("Matrix dimensions must match for subtraction!")
        elif operation.get() == "Multiplication":
            if matrix_a.shape[1] == matrix_b.shape[0]:
                result = np.dot(matrix_a, matrix_b)
            else:
                raise ValueError("Invalid matrix dimensions for multiplication!")
        elif operation.get() == "Transpose":
            result = matrix_a.T
        elif operation.get() == "Determinant":
            if matrix_a.shape[0] == matrix_a.shape[1]:
                result = np.linalg.det(matrix_a)
            else:
                raise ValueError("Matrix must be square for determinant calculation!")
        messagebox.showinfo("Result", f"Result:\n{result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# function to create matrix input fields
def create_matrix_entries(root, rows, cols, frame):
    """
    Dynamically generates matrix input fields based on given rows and column counts.
    """
    entries = []
    for r in range(rows):
        row_entries = []
        for c in range(cols):
            entry = tk.Entry(frame, width=5)
            entry.grid(row=r, column=c)
            row_entries.append(entry)
        entries.append(row_entries)
    return entries

# funtion to dynamically generate matrix input fields based on input by user.
def generate_entries():
    """
    Reads user input mayrix dimensions and creates corresponding input fields.
    Clears previous entries before regenrating.
    """
    global entries_a, entries_b
    try:
        rows_a = int(row_a_entry.get())
        cols_a = int(col_a_entry.get())
        rows_b = int(row_b_entry.get())
        cols_b = int(col_b_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid dimensions!")
        return
    # clears previous matrix input fields.
    for widget in frame_a.winfo_children():
        widget.destroy()
    for widget in frame_b.winfo_children():
        widget.destroy()
    # creates new matrix input fields.
    entries_a = create_matrix_entries(root, rows_a, cols_a, frame_a)
    entries_b = create_matrix_entries(root, rows_b, cols_b, frame_b)

# function to set up GUI layout.
def setup_gui():
    global root, row_a_entry, col_a_entry, row_b_entry, col_b_entry, operation, frame_a, frame_b
    
    root = tk.Tk()
    root.title("Matrix Operations Tool")
    
    # Input fields for matrix dimensions.
    tk.Label(root, text="Matrix A Dimensions (Rows x Cols):").pack()
    row_a_entry = tk.Entry(root, width=5)
    col_a_entry = tk.Entry(root, width=5)
    row_a_entry.pack(side=tk.LEFT)
    col_a_entry.pack(side=tk.LEFT)
    
    tk.Label(root, text="Matrix B Dimensions (Rows x Cols):").pack()
    row_b_entry = tk.Entry(root, width=5)
    col_b_entry = tk.Entry(root, width=5)
    row_b_entry.pack(side=tk.LEFT)
    col_b_entry.pack(side=tk.LEFT)
    
    # button to generate matrix input fields.
    tk.Button(root, text="Generate Matrices", command=generate_entries).pack()
    
    # frames to hold matrix input fields.
    frame_a = tk.Frame(root)
    frame_a.pack()
    frame_b = tk.Frame(root)
    frame_b.pack()
    
    # dromdown menu for selecting matrix operations.
    operations = ["Addition", "Subtraction", "Multiplication", "Transpose", "Determinant"]
    operation = tk.StringVar(root)
    operation.set(operations[0])
    tk.OptionMenu(root, operation, *operations).pack()
    
    # button to perform selected operation.
    tk.Button(root, text="Calculate", command=perform_operation).pack()
    root.mainloop()

# initialise and run GUI.
setup_gui()