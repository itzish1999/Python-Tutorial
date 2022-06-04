# This file is to learn how to use functions in code.

# Declaring the value of a
from sympy import OneMatrix


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
d = round(c, 2)
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

# An f-string with the formula quantity * Unit Price
unit_price = 49.99
quantity = 30
""" Notice the :,.2f ? That is formatting the way the output looks.
the : means that we are going to format the f-string
the , makes any adjustment to the thousands place
the .2f means the second decimal place FIXED """
print(f"Total = ${quantity * unit_price:,.2f}")

# In order to declare a percentage, we must use a float in Python
sales_tax_rate = 0.065
# This formatting is the same but for percentages. the .2% means the 2nd decimal point and add a % at the end
print(f"Sales Tax Rate {sales_tax_rate:.2%}")

# f-strings just doesn't have to be within print() you can name it. f-strings work like any other string

# Introducing line breaking with f-string
user1 = "Ismaeel"
user2 = "Mo"
user3 = "Mud"

# One method is to use the \n method. Please note to use the \ not the /. The \n should be outside the {}
output = f"{user1} \n{user2} \n{user3}"

# Shows our f-string
print(output)

user4 = "Omar"
user5 = "Jana"
user6 = "Ali"

# The method I prefer is the triple quote mark method. Easier to read and easier to write.
second_output = f'''
{user4}
{user5}
{user6}
'''
# Prints our line breaked f-string
print(second_output)

# You can also edit the width of the f-string as well. In the real world, we would always align to the right.

''' You can control the width of your output by following the : with 
< (left aligned)
> (right aligned)
^ (centered) 
Put any of these characters AFTER the : '''
# Note that you can make the output however many characters apart: >20 for example. I used >9.

new_unit_price = 49.95
new_quantity = 32
new_sales_tax_rate = 0.065
new_subtotal = new_quantity * new_unit_price
new_sales_tax = new_sales_tax_rate * new_subtotal
new_total = new_subtotal + new_sales_tax

# Notice how I added the "$" ? what I did was called concatenate; to join.
s_subtotal = "$" + f"{new_subtotal:,.2f}"
s_sales_tax = "$" + f"{new_sales_tax:,.2f}"
s_total = "$" + f"{new_total:,.2f}"

# This code is about the alignment. It takes the total of the code above which presents total prices, etc, with the added $.
new_output = f'''
Subtotal:   {s_subtotal:>9}
Sales Tax:  {s_sales_tax:>9}
Total:      {s_total:>9}
'''
print(new_output)

""" Had I not added the $ instead of using the $ outside each {} bracket the symbol would've been disconnected from the number I am making.
that would've been really inconvenient. So I stuck the $ to the f-string! Now it makes a completely new variable. """

# Note that the f-string always produces a string and not a number. That is why we are able to add commas!

# Concatenating Strings Example

first_name = "John"
middle_name = "Dough"
last_name = "Doe"

# Had we not added the + " ", Python would've presented the full name without the spaces in between
full_name = first_name + " " + middle_name + " " + last_name

print(full_name)