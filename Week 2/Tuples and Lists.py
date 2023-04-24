# START OF LISTS IN PYTHON UPTO LINE 70

# Create a list

L = ["Michael Jackson", 10.1, 1982]
print(L)

# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )

# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)

# Use append to add elements to list

L.append(['a','b'])
print(L)

# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Delete the element based on the index

print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space

print('hard rock, Metal'.split(',')) # Without any argument in soplit it will take Space as splitter

# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Examine the copy by reference

print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

# Clone (clone by value) the list A

B = A[:]

print(B)

print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

# END OF LISTS IN PYTHON

# START OF TUPLES


# Create your first tuple

tuple1 = ("disco",10,1.2 )
print(tuple1)

# Print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# Print the type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# Use negative index to get the value of the last element

tuple1[-1]

# Concatenate two tuples

tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

# Slice from index 0 to index 2

print(tuple2[0:3])

# Slice from index 3 to index 4

print(tuple2[3:5])

# Get the length of tuple

len(tuple2)

# A sample tuple

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# Sort the tuple

RatingsSorted = sorted(Ratings)
print(Ratings)
print(RatingsSorted)

# Create a nest tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print(NestedT)

# Print element on each index

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

# Print the first element in the second nested tuples

print(NestedT[2][1][0])

# Print the first element in the second nested tuples

print(NestedT[4][1][0])