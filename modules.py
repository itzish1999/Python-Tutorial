# Creating modules for me to use / Working with modules

# There are different ways for telling date time. Three to be exact. They are as follows
""" 
datetime.date - A date consisting of a month, day and year without the time
datetime.time - A time consisting of an hour, minute, second, microsecond and optional time zone
datetime.datetime - A single item of data consisting of date, time and optionally time zone info.
"""

# Import datetime module and give it an alias of dt
import datetime as dt
from turtle import right

# We are showing the date with the computers internal clock

# Store today's date with a variable named today
today = dt.datetime.today()

# Manually store in today's date
manual_today = dt.date(2020, 6, 8)

# datetime.time format with arguments
# time = dt.time([hour, [minute, [second, [microsecond]]]])
time = dt.time(12, 35, 50, 999999)

# datetime.time without arguments
no_time = dt.time()

# datetime.datetime outline
# date_time = dt.datetime(year, month, day, hour, [minute, second, [microsecond]])

# datetime.datetime
date_time = dt.datetime(2020, 6, 8, 22, 45, 50)

# You can even get the date / time for right now!
right_now = dt.datetime.now()

# You can use an f-string to design it as well
print(f"{today:%A, %m/%d/%Y}")
print(no_time)
print(manual_today)
print(time)
print(date_time)
# Unedited
# print(right_now)
# Edited with f-string
print( f"{right_now:%a, %b %d, %Y time %H:%M:%S}")