# First function example: Add 1 to a and store as b

def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)

print(add(17))


# Define a function for multiple two numbers

def Mult(a, b):
    c = a * b
    return (c)
    print('This is not printed')


result = Mult(12, 2)
print(result)

# Use mult() multiply two different type values together

print(Mult(3, "Michael Jackson "))


# Function Definition

def square(a):
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c)
    return (c)

print(square(2))


# Define functions, one with return value None and other without return value

def MJ():
    print('Michael Jackson')


def MJ1():
    print('Michael Jackson')
    return (None)
MJ()
MJ1()

# a and b calculation block1

a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0
else:
    c1 = 5
print(c1)

# a and b calculation block2

a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0
else:
    c2 = 5
print(c2)

# Make a Function for the calculation above

def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0
    else:
        c = 5
    return(c)

# Code replace of Block 1 with Function
a1 = 4
b1 = 5
c1 = Equation(a1, b1)
print(c1)

# Code replace of Block 2 with Function

a2 = 0
b2 = 0
c2 = Equation(a2, b2)
print(c2)


# Function example

def type_of_album(artist, album, year_released):
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"


x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

# Print the list using for loop

def PrintList(the_list):
    for element in the_list:
        print(element)

PrintList(['1', 1, 'the man', "abc"])

# Compare Two Strings Directly using in operator
# add string
string = "Michael Jackson is the best"


# Define a funtion
def check_string(text):
    # Use if else statement and 'in' operatore to compare the string
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'


print(check_string("Michael Jackson is the best"))


# Compare two strings using == operator and function
def compareStrings(x, y):
    # Use if else statement to compare x and y
    if x == y:
        return 1


# Declare two different variables as string1 and string2 and pass string in it
string1 = "Michael Jackson is the best"
string2 = "Michael Jackson is the best"

# Declare a variable to store result after comparing both the strings
check = compareStrings(string1, string2)

# Use if else statement to compare the string
if check == 1:
    print("\nString Matched")
else:
    print("\nString not Matched")


# Python Program to Count words in a String using Dictionary
def freq(string):
    # step1: A list variable is declared and initialized to an empty list.
    words = []

    # step2: Break the string into list of words
    words = string.split()  # or string.lower().split()

    # step3: Declare a dictionary
    Dict = {}

    # step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)

    # step5: Print the dictionary
    print("The Frequency of words is:", Dict)


# step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")

# Example for setting param with default value

def isGoodRating(rating=4):
    if (rating < 7):
        print("this album sucks it's rating is", rating)

    else:
        print("this album is good its rating is", rating)

# Test the value with default value and with input
isGoodRating()
isGoodRating(10)

# Example of global variable

artist = "Michael Jackson"

def printer(artist):
    global internal_var
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist)
printer(internal_var)

# Example of global variable

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)

# Deleting the variable "myFavouriteBand" from the previous example to demonstrate an example of a local variable

# del myFavouriteBand

# Example of local variable

def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)


# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

# Collections and Functions
#  When the number of arguments are unknown


def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

# Similarly, The arguments can also be packed into a dictionary as shown:
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

# Functions can be incredibly powerful and versatile. They can accept (and return) data types, objects and even other functions as arguements. Consider the example below:

def addItems(list):
    list.append("Three")
    list.append("Four")


myList = ["One", "Two"]

addItems(myList)

print(myList)
