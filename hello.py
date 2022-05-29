# This is my first ever python comment!
""" This is my first multi-line comment
This is the beginning to understanding and using Python as a whole! """

# Working with operators / creating a variable name
quantity = 10
# This variable contains a float
unit_price = 1.99
# This variable contains the result of multiplying quantity times unit price
extended_price = quantity * unit_price
#Show the results
print(extended_price)


""" Variable naming conventions should typicall follow the PEP 8 styling conventions or Camel Case
Python purists typically like PEP 8 because the underscore that separates multiple words are easier to distinguish
Camel Case is also pretty common.
(PEP 8) my_number = 2
(Camel Case) myNumber = 2 """

#Boolean example
x = 10
# If else statement depending on X
if x == 0:
# Really important to use : and indent the preceeding line
    print("X is zero")
# Same applies to the beginning of the else statement
else:
    print("x is ", x)
# This code will execute no matter what BECAUSE it isn't indented
print("All done")

""" Indentation is super important in Python.
For now its pivotal to remember that in regards to this code,
the indented lines will execute DEPENDING on the value of x. """