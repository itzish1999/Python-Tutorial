# Creating modules for me to use / Working with modules

# There are different ways for telling date time. Three to be exact. They are as follows
""" 
datetime.date - A date consisting of a month, day and year without the time
datetime.time - A time consisting of an hour, minute, second, microsecond and optional time zone
datetime.datetime - A single item of data consisting of date, time and optionally time zone info.
"""

# Import datetime module and give it an alias of dt
import datetime as dt

# We are showing the date with the computers internal clock

# Store today's date with a variable named today
today = dt.datetime.today()

# Manually store in today's date
manual_today = dt.date(2022, 6, 8)

# datetime.time format with arguments
# time = dt.time([hour, [minute, [second, [microsecond]]]])
time = dt.time(12, 35, 50, 999999)

# datetime.time without arguments
no_time = dt.time()

# datetime.datetime outline
# date_time = dt.datetime(year, month, day, hour, [minute, second, [microsecond]])

# datetime.datetime
date_time = dt.datetime(2022, 6, 8, 22, 45, 50)

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

# Calculating timespans

""" In the programming world. Sometimes we need to know the duration or timespan.
Timespan is how long in terms of years, months, weeks, days, hours, minutes or whatever.
For timespans, the Python datetime module has a class called datetime.timedelta. """

# timedelta is created AUTOMATICALLY whenver you subtract two dates, times, or datetimes to determine the duration between them
# You can also define any timedelta using this syntax
# datetime.timedelta(days=, seconds=, microseconds=, milliseconds=, minutes=, hours=, weeks=)

"""
AUTOMATICALLY DETERMINED 
new_years_day = dt.date(2022, 1, 1)
memorial_day = dt.date(2022, 5, 27)
days_between = memorial_day - new_years_day
print(days_between)
"""

# DEFINED
new_years_day = dt.date(2022, 1, 1)
memorial_day = dt.date(2022, 5, 27)
duration = dt.timedelta(days = 146 ) # 146 = days between nyd and memorial day.
print(new_years_day + duration) # You can also subtract

# You can also use datatime.timedelta with datetime
start_time = dt.datetime(2022, 3, 31, 8, 0, 0)
finish_time = dt.datetime(2022, 3, 31, 14, 34, 45)
time_between = finish_time - start_time
print(f" Time {time_between}")
print(type(time_between)) # Type just tells us what type of data it is. In this case timedelta; duration

# Yet another timedelta ex. with an age calculator

now = dt.date.today()
birth_date_time = dt.date(1999, 8, 7)
age = now - birth_date_time
print(f"Your age {age}")
print(type(age))

# My time vs UTC time

here_now = dt.datetime.now()
utc_now = dt.datetime.utcnow()

# Difference of my time vs utc time
time_difference = (utc_now - here_now)

# Show results
print(f"My Time    : {here_now:%I:%M %p}")
print(f"UTC Time   : {utc_now:%I:%M %p}")
print(f"Difference : {time_difference}")
