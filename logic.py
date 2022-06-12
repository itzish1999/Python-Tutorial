import datetime as dt
import random

# This folder is for understanding how computers do things with data.

""" All of the other files is just data that we fed into the computer with variables!
Now is really the time where we habe the computer DO things.

Computers are often do on a regular basis efficiently and effectively is make decisions.
There are operators that are responsible for this. They are referred to as relational operators
or
Comparison operators. 

Here is how they look:

==    is equal to
!=    is does not equal to
<     is less than
>     is greater than
<=    is less than or equal to
>=    is greater than or equal to """

# Python also has logical operators or referred to as boolean operators. In Python they actually use English
#In hindsight, when understanding Python, you can see why the language uses English; readability for us humans. 

""" The logical / Boolean operators are as follows: 

and   Both are true
or    One or the other is true
not   not is ture """

""" If you are curious about Boolean, the word stems from the name George Boole, who played a role in establishing
the algebra of logic. This basically laid the foundation of modern computers."""

""" All of the operators above are used with the 'if' 'then' and 'else' statements to make a computer or program do something."""

# The word if is used a lot in apps and computers programs to make decisions. Here is an example of the simplest syntax

""" 
if condition: do this
do this no matter what. 

***So the first 'do this' line is if the condition is true.
If the condition is false the first 'do this' is ignored.
the 'do this no matter what' will always be executed no matter what***
"""

# sun = 'down'
# if sun == 'down': print("Good Night!")
# print('I am here!')

""" Make sure you always use 2 equal signs to indicate if the condition is true.

Here is an example if the 'if' condition is false: """

sun = 'up'
if sun == 'down': print('Good Night')

print('I am here!')

# Run this code in the terminal and you will see that the if statement we made is ignored!

""" Notice how we hadn't used indentation? 
Often times, when you have the if statement, you usually have multiple lines of code.
You can still indent with one line of code underneath!
Regardless of the condition of the if statement. Any and all code underneath will run regardless."""

moon = 'full'
if moon == 'full':
    print('Tonight is a Full Moon!')

print("Can't Wait For Sunset!")

# It is preferred to indent the code underneath the 'if' because it is easier to read

# You can have any amount of code underneath the if statement that's indented. They will execute if the statement is true:

total = 100
sales_tax_rate = 0.065
# To indicate if something is true/false you must spell it with a capital T or F
taxable = True

if taxable:
    print(f"Subtotal : ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(f"Sales Tax: ${sales_tax:.2f}")
    total = total + sales_tax

print(f"Total    : ${total:.2f}")

""" Notice how we used if taxable:   ?
that is synonymous with if taxable == True: because we specified that taxable = True prior to the if statement."""

# Again, if taxable was false, what would happen? The 4 indented lines of code will skip.

# -------------------------- Adding else in your code ----------------------------------------------------

""" So far we reviewed the if condition in which if a condition is true, the code executes.
the else statement can work when our variable is false!
Sometimes you may want one chunk of code to execute 'if' a condition is true; otherwise (else) if it isn't true you want other
code to be executed. Eample of logic and syntax:

if condition:
    do intended lines here
    ....

else:
    do intended lines here
    ....
do remaining un-indented lines no matter what
"""

""" 
# Get the current date and time
now = dt.datetime.now()
# Make a decision based on hour
if now.hour < 12:
    print('Good Morning!')
else:
    print('Good Afternoon')
print('Hope You Are Doing Well!') """

""" This code looks at the clock in your computer to make that decision with dt.datetimenow().
now.hour specifies to look at the hour and says that if the hour of the time right now is less than 12.
If it is true, the computer will print Good Morning!
otherwise (else) it will print Good Afternoon! """

# Now what if it is a different time, say 8pm? you can use another statement called elif (else if) The syntax is as follows:

"""
if condition:
    do this line of code
elif:
    do this line of code
do this line of code regardless
"""

# You can have any number of elif conditions. You can include or not a final else statement that executes if all previous elifs are false

# A few examples

""" TRUE CONDITION
traffic_light = 'green'
if traffic_light == 'green':
    print('Drive!')
elif traffic_light == 'red':
    print('Stop!')
print('I will execute no matter what')
^ Prints the if condition
"""

""" FALSE CONDITION
traffic_light = 'red'
if traffic_light == 'green':
    print('Drive!')
elif traffic_light == 'red':
    print('Stop!')
print('Imma run regardless')
^ prints the elif condition
"""

""" ALL ARE FALSE
traffic_light = 'yellow'
if traffic_light == 'green':
    print('Drive!')
elif traffic_light == 'red':
    print('Stop!')
print('I still run regardless')
^ only prints 'I still run regardless'
"""

""" ELSE OPTION IF ALL ARE FALSE"""
traffic_light = 'yellow'
if traffic_light == 'green':
    print('Drive!')
elif traffic_light == 'red':
    print('Stop!')
else:
    print('Drive With Caution!')
print('Driving 101!')
# ^ Prints the else condition we left. 'If all else fails. do this'

#------------------------------TERNARY OPERATIONS----------------------------------------

# Here is another example of if, else, elif being used

# Setting a number variable named age
age = 22
# If the number provided is less than 21
if age < 21:
    beverage = 'Water'
# If the number is greater than or equal to and less than 21, 80
elif age >= 21 and age < 80:
    beverage = 'Beer'
# Any number above 80
else:
    beverage = 'Juice'
# Message that runs regardless of code. I could've printed in each operation, however that was more code. 
# I got lazy... We concated instead
print('Have a ' + beverage)

#-----------------------------------LOOPS---------------------------------------------

""" Sometimes you need to perform a task over and over again. That is where the for loop comes in!
The for loop enables you to repeat a line of code over and over again, or even several lines of code. """

# Syntax for a for loop:
"""
for x in range(y):
    do this
    do this
    ...
un-indented code that is executed AFTER the loop; different than in if, else and elif
"""

# A for loop example with the previos syntax
"""
for nums in range(7):
    print(nums)
print('All Done!')
^ run this code and see the output"""

# Running the code it prints only 0 - 6. The loop will always start at 0. You would have to specify:

for nums in range(1, 10):
    print(nums)
print('All Done!')

""" When specifying where to start the number on the left serves that purpose.
Separated by a comma, the number on the right is the ending point.
BE WEARY that the number on the left also means 1 number greater than the ending point!!!!"""

#-----------------------------------LOOPING THROUGH A STRING---------------------------

""" So far what we have covered is the idea that you can loop through a range() of numbers. 
This is completely optional to do; in fact there are many other ways to loop through things.

Lets take a string for an example. You can loop through any string you create and the computer will return each character in the string.
Here is the syntax:

for x in string:
    do this
    do this
    ....
do this when the loop is done

replace x with any variable name that you'd like. The string should be text enclosed within quotation marks
or
a name of a variable that contains a string."""

"""
for string_loop in "Pickles":
    print(string_loop)
print("All Done!")
^ Run this code and you will see Pickles spelled out! Here is a challenge.
"""

# Here is an example of a string loop with another variable that contains a string
string_name = "New York"
for string_loop in string_name:
    print(string_loop)
print("Loop Complete!")
# ^ Run this code and see what the outcome is. You see how we gave our string a name and it printed it? The loop also included the space

#--------------------------------------------------LOOPING THROUGH A LIST--------------------------------------------------------------

""" In Python a list is a bunch of strings or numbers enclosed in a [] that is separated by commas.
If you are familiar with different languages, it is basically an array.
The syntax is the same with the string except you need to layout the list/array. """

"""
for list_loop in ["Apples", "Oranges", "Lemon", "Cheeries", "Grapes", "Pears"]:
    print(list_loop)
print("List Of Food")
"""
# ^ Run this code and you will see all of the items displayed on the console log or terminal.

# Note you can also assign a variable that contains a list...

food_list = ["Apples", "Oranges", "Lemon", "Cheeries", "Grapes", "Pears"]

for list_loop in food_list:
    print(list_loop)
print("List Of Food!")

""" Usually, you'd want to go through the whole list, yet there are some instances where you may want to break out of the loop
to do so you can say to the loop to break if x condition is met.
The syntax is as follows:

for x in items:
    if condition:
        [do this... ] # What is in between the square brackets is optional
        break
    do this
"""


# answers = ["A", "B", "c", "D"]
# for odd_one_out in answers:
   #  if odd_one_out == "c":
     #    print("c is Different From All Other Answers!")
   #      break
 #    print(odd_one_out)
# print("We Succesfully Picked The Odd One Out...")
# Run this code and see what happens


""" In this example I created a for loop that cycled through the list of answers. I wanted to pick the only Letter that was different.
in this case it was c. I added the if condition in which I specified with a comparison operator that if there is 'c',
print out the statement I made and break from c. """

# You can also use continue in a loop which is similar to break
answers = ["A", "B", "c", "D"]
for odd_one_out in answers:
    if odd_one_out == "c":
        print("Removed Odd One")
        continue
    print(odd_one_out)
print("Loop Is Done")

# You can also nest loops. Just be aware of indentation because each loop determines which line of code is located within:

# Outer loop
for outer in ["First", "Second", "Third"]:
    print(outer)
    # Inner loop
    for inner in range(3):
        print(inner + 1)
print("Successfully Nested")

# An alternative way to loop for, you can use while. 
# There is a very subtle difference. For a for loop, you get a fixed number (one for each item).
# For while loops you loop as long as (while) some condition is true. Below is the syntax:

"""
while condition:
    do this ......
    do this ......
do this when loop is done.
"""
# Please note that when using while loops you have to make sure that the condition that makes the loop stop happens eventually. 
# Otherwise the program would loop forever and you might have to shut off the program... Ex:

counter = 65
while counter < 91:
    counter += 1
    print(counter)
print("Successful While Loop")

# You can also use if and continue in a while loop

print("Odd Numbers")
counter = 0
while counter < 10:
    # Get a random number
    number = random.randint(1, 999)
    if int(number / 2) == number / 2:
        # If it's an even number, don't print it.
        continue
    # Otherwise, if it's odd, print it and increment the counter.
    print(number)
    # Increment the loop counter
    counter += 1
print("Loop is Done")

""" You can also use break in while loops as well"""