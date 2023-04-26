# Import the libraries

import numpy as np
import matplotlib.pyplot as plt

# Create a list

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
print(a)

# Convert list to Numpy Array
# Every element is the same type

A = np.array(a)
print(A)

# Show the numpy array dimensions

print(A.ndim)

# Show the numpy array shape

print(A.shape)

# Show the numpy array size

print(A.size)

# Access the element on the second row and third column

print(A[1, 2])

# Access the element on the second row and third column

print(A[1][2])

# Access the element on the first row and first column

print(A[0][0])

# Access the element on the first row and first and second columns

print(A[0][0:2])

# Create a numpy array X

X = np.array([[1, 0], [0, 1]])
print(X)

# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]])
print(Y)

# Add X and Y

Z = X + Y
print(Z)

# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]])

# Multiply Y with 2

Z = 2 * Y
print(Z)

# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]])

# Create a numpy array X

X = np.array([[1, 0], [0, 1]])

# Multiply X with Y

Z = X * Y

print(Z)



# Create a matrix A

A = np.array([[0, 1, 1], [1, 0, 1]])

# Create a matrix B

B = np.array([[1, 1], [1, 1], [-1, 1]])

# Calculate the dot product

Z = np.dot(A,B)
print(Z)

# Calculate the sine of Z

print(np.sin(Z))

# We use the numpy attribute <code>T</code> to calculate the transposed matrix

# Create a matrix C

C = np.array([[1,1],[2,2],[3,3]])

# Get the transposed of C

print(C.T)

