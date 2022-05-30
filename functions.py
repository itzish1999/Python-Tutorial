# This file is to learn how to use functions in code.

# Declaring the value of a
a = -4
# Creating a var named b and using the abs() function
b = abs(a)
# Showing the value of a
print(a)
# Showing the value of b
print(b)

""" If you run the code, our output should show 4 
since abs() shows the absolute number 
(converts negative nums to positive ones) """

""" The rubric for creating functions is as follows;
variablename = functioname(param[, param])
The function is named and then a () is used
you input a param and you have the option to input a second one. """

# Function that uses round()

# Decalaring a value for c
c = 1.23456789098765432100000000001
# Creating a var named d and using the round() function
# Note that the 2 means how many decimal places
d = round(x, 2)
# Showing the value of c
print(c)
# Showing the value of d
print(d)

# The easiest way to format data is using the f-string

# F-string can be declared with either a f or F followed by "" with literal text and {} for expressions

# Creating a username
user_name = "Ismaeel"
# Creating an f-string to say hello and my name within the {}
print(f"Hello {user_name}")