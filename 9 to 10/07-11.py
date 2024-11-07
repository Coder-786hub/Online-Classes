# Number of Arguments:-
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.


# Example
# This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("vikas", "kumar")

# If you try to call the function with 1 or 3 arguments, you will get an error


# Arbitrary Arguments, *args:-
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

# Example
# If the number of arguments is unknown, add a * before the parameter name:



def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("harry", "jerry", "panda")
