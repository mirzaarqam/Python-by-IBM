# Condition Equal

a = 5
print(a == 6)

# Greater than Sign

i = 6
print(i > 5)

# Greater than Sign

i = 2
print(i > 5)

# Inequality Sign

i = 2
print(i != 6)

# Use Equality sign to compare the strings

print("ACDC" == "Michael Jackson")

# Use Inequality sign to compare the strings

print("ACDC" != "Michael Jackson")

# Compare characters

print('B' > 'A')

# Compare characters

print('BA' < 'AB')

# If statement example

age = 19
# age = 18

# expression that can be true or false
if age > 18:
    # within an indent, we have the expression that is run if the condition is true
    print("you can enter")

# The statements after the if statement will run regardless if the condition is true or false
print("move on")

# Elif statment example

age = 18

if age > 18:
    print("you can enter")
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf")

print("move on")

# Condition statement example

album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")

print('do something..')

# Condition statement example

album_year = 1980

if (album_year > 1979) and (album_year < 1990):
    print("Album year was in between 1980 and 1989")

print("")
print("Do Stuff..")

# Condition statement example

album_year = 1983

if not (album_year == 1984):
    print ("Album year is not 1984")