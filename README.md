# Task3
## Matrix Operations Tool

### Overview

The Matrix Operations Tool is a Python-based GUI application built using tkinter and numpy. It allows users to perform various matrix operations, such as:
-Addition
-Subtraction
-Multiplication
-Transpose
-Determinant

Users can input custom matrix dimensions and values, and the application will compute the results accordingly.

### Features:
-Dynamic Input Fields: Users specify matrix dimensions, and input fields are generated dynamically.
-Error Handling: Proper validation and error messages ensure valid inputs.
-Interactive GUI: Simple and intuitive interface using tkinter.
-Matrix Calculations: Supports common matrix operations with real-time feedback.


### Usage:

Step 1: Enter the number of rows and columns for Matrix A and Matrix B.

Step 2: Click Generate Matrices to create input fields.

Step 3: Enter values in the input fields.

Step 4: Choose an operation from the dropdown menu.

Step 5: Click Calculate to perform the operation and view results.

### Error Handling

If invalid inputs are provided, an error message is displayed.
Operations that require square matrices (like determinant) will prompt errors if dimensions are incorrect.
For addition and subtraction, matrix dimensions must match.
For multiplication, column count of Matrix A must match row count of Matrix B.
