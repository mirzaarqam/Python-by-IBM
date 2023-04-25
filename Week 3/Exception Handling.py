# potential code before try catch

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")

# potential code before try catch

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
# code to try to execute
except (ZeroDivisionError, NameError):
    print("There could be Zero Division Error or Syntax Err0r")
# code to execute if there is an exception of the given types

# code that will execute if there is no exception or a one that we are handling

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

# Now lets let the user know that we are done processing their answer. Using the finally, let's add a print.
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")