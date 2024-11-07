# Python Functions

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.



# Creating a Function
# In Python a function is defined using the def keyword:

# Example:-
def my_function():
  print("Hello from a function")


# Calling a Function:-
# To call a function, use the function name followed by parenthesis:

# Example
def my_function():
  print("Hello from a function")

my_function()


# Arguments:-
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# Example:-
def my_function(fname):
  print(" My name is "+fname )

my_function("Harry")
my_function("Jerry")
my_function("Panda")