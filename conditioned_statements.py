city = input("Enter your city name: ")
temp = float(input("Enter today's temperature in C: "))

print("City:", city)
print("Temperature:", temp)

# @note-->if u need a decimal value in the input, use float() instead of int().

# nxt it is the conditioned stetements 
# the if statement is used to make decisions in the code based on certain conditions. It allows the program to execute different blocks of code depending on whether a condition is true or false.
# if the if conition does not meet the criteria, the else statement will be executed. The else statement is used to specify a block of code that will be executed if the condition in the if statement is false.
# the elif statement is used to check multiple conditions in a sequence. It allows you to specify additional conditions to be checked if the previous conditions were false. If the condition in the if statement is false, the program will check the condition in the elif statement. If that condition is true, the corresponding block of code will be executed. If none of the conditions are true, the else block will be executed.
#  therefore the sinyax is  if > elif > else
if temp > 25:
    print("Great day to go outside!")
if temp > 35:
    print("Weather: Scorching Hot")
elif temp < 15:
    print("Grab a jacket before you go out!")
else:
    print("get a good walk in the city park!")



#  using date-time module to get the current date and time
import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)

print(calendar.calendar(now.month, 2, 1, 6))  # Display the calendar for the current month
print(calendar.calendar(now.year)) 
