# Keyword Arguments
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.

# Example
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "harry", child2 = "jerry", child3 = "panda")



# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Kumar")
