# import numpy library

import numpy as np

# Create a python list

a = ["0", 1, "two", "3", 4]

# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])

print(a)

# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Version Check

print(np.__version__)

# Check the type of the array

print(type(a))

# Check the type of the values stored in numpy array

print(a.dtype)

# Create numpy array

c = np.array([20, 1, 2, 3, 4])

# Assign the first element to 100

c[0] = 100

print(c)

# Assign the 5th element to 0

c[4] = 0

print(c)

# Slicing the numpy array

d = c[1:4]

print(d)

# Set the fourth element and fifth element to 300 and 400

c[3:5] = 300, 400

print(c)

# We can also define the steps in slicing, like this: [start:end:step].

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

# if we don't pass the end it considered 0

print(arr[:4])

# If we don't pass end it considers till the length of array.

print(arr[4:])

# If we don't pass step its considered 1

print(arr[1:5:])


# Similarly, we can use a list to select more than one specific index.
# The list `select` contains several values:
# Create the index list

select = [0, 2, 3, 4]
print(select)

# Use List to select elements

d = c[select]
print(d)

# Assign the specified elements to new value

c[select] = 100000
print(c)

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])

# Get the size of numpy array

print(a.size)

# Get the number of dimensions of numpy array

print(a.ndim)

# Get the shape/size of numpy array

print(a.shape)

# Numpy Statistical Functions

# Create a numpy array

a = np.array([1, -1, 1, -1])

mean = a.mean()
print(mean)

# Get the standard deviation of numpy array

standard_deviation=a.std()
print(standard_deviation)

# Create a numpy array

b = np.array([-1, 2, 3, 4, 5])
# Get the biggest value in the numpy array

max_b = b.max()
print(max_b)

# Get the smallest value in the numpy array

min_b = b.min()
print(min_b)

# Numpy Array Operations

u = np.array([1, 0])
v = np.array([0, 1])

# Numpy Array Addition

z = np.add(u, v)
print(z)

# Plotting functions


import time
import sys
import numpy as np

import matplotlib.pyplot as plt
# %matplotlib inline


def Plotvec1(u, z, v):
    ax = plt.axes()  # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r',
             head_length=0.1)  # Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')  # Adds the text u to the Axes

    ax.arrow(0, 0, *v, head_width=0.05, color='b',
             head_length=0.1)  # Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')  # Adds the text v to the Axes

    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')  # Adds the text z to the Axes
    plt.ylim(-2, 2)  # set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)  # set the xlim to left(-2), right(2)
    plt.show()

# Plot numpy arrays

# Plotvec1(u, z, v)

# Numpy Array Subtraction

a = np.array([10, 20, 30])
b = np.array([5, 10, 15])
c = np.subtract(a, b)

print(c)

# Array Multiplication

# Create a numpy array

x = np.array([1, 2])

# Create a numpy array

y = np.array([2, 1])

# Numpy Array Multiplication

z = np.multiply(x, y)
print(z)

# Array Division

a = np.array([10, 20, 30])
b = np.array([2, 10, 5])
c = np.divide(a, b)
print(c)

# Dot Product
# The dot product of the two numpy arrays u and v is given by:

X = np.array([1, 2])
Y = np.array([3, 2])

# Calculate the dot product

z = np.dot(X, Y)

#Elements of X
print(X[0])
print(X[1])
#Elements of Y
print(Y[0])
print(Y[1])

print(z)

# Adding Constant to Numpy Array
# Create a constant to numpy array

u = np.array([1, 2, 3, -1])
# Add the constant to array

u + 1

print(u)

# Mathematical Function

# The value of pi

np.pi

# Create the numpy array in radians

x = np.array([0, np.pi/2 , np.pi])

# Calculate the sin of each elements

y = np.sin(x)

print(y)


# Linespace

# Makeup a numpy array within [-2, 2] and 5 elements

np.linspace(-2, 2, num=5)
print(np.linspace(-2, 2, num=5))

# Make a numpy array within [-2, 2] and 9 elements

np.linspace(-2, 2, num=9)
print(np.linspace(-2,3, num=9))

# Make a numpy array within [0, 2π] and 100 elements

x = np.linspace(0, 2*np.pi, num=100)

# Calculate the sine of x list

y = np.sin(x)

# Plot the result

plt.plot(x, y)
plt.show()