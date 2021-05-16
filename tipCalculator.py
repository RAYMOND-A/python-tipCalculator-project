# Data types
# primitive data types

# String

name = "Hello"

print("first character is " + name[0])
print("Last character is " + name[-1])

print("123" + "345")

# Integers

print(123 + 456)

# Large integers
large_number = 123_456_789 # this helps humans to easily read large number values
print(large_number)

# Float

pi = 3.14159

# boolearn
a = True
b = False

# Type Error, Type Checking and Type Conversion
num_char = len(input("what's your name?"))
print(type(num_char))

new_num_char = str(num_char)

print("your name has " + new_num_char + " characters")

# data types challenge

two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number))

# new_two_digit_number = str(two_digit_number)

first_number_string = two_digit_number[0]
last_number_string = two_digit_number[-1]
print(first_number_string)
print(type(first_number_string))

first_number_int = int(first_number_string)
last_number_int = int(last_number_string)
print(first_number_int)
print(type(first_number_int))

sum_of_input_number = first_number_int + last_number_int
print(sum_of_input_number)
print(type(sum_of_input_number))

sum_converted_to_string = str(sum_of_input_number)

print("sum of two digit number inputted is " + sum_converted_to_string)

# when you dividing two number it always returns a Float
print(6/3)

# exponent in python 

# PEMDAS LR [parenthesis, Exponent, Multiplication&Division, Addition&Substraction] [Left to Right]
# ()
# **
# */
# +-

print( 2 ** 3)

# building BMI calculator exercise

# BMI = Weight in kg / square of height in meters

height = input("enter your heught in m: ")
weight = input("enter your weight in kg: ")

float_weight = float(weight)
float_height = float(height)

float_BMI = float_weight / (float_height**2)

int_BMI = int(float_BMI)

print("BMI is " + str(int_BMI))

# rounding floating points numbers  we use the round function

# rounding to whole number or int
print(round(2.6666666))

# rounding to a give precision or to 2 d.p in the case below
print(round(2.6666666, 2))

# another way to round a floating point value is by using // operator
# example 8//3 gives you 2

print(type(8 // 3))

result  = 4/2
result /= 2 # result = result / 2

score = 0
height = 1.8
isWinning = True
# f-Sring incorporates various types and print to the console

print(f"your score is {score}, your height is {height}, your winning is {isWinning}")

# your life in weeks challenge

age = input("what is your current age: ")

int_age = int(age)

days_spent = int_age * 365
months_spent = int_age * 12
weeks_spent = int_age * 52

days_in_90years = 90 * 365
months_in_90years = 90 * 12
weeks_in_90years = 90 * 52

days_left = days_in_90years - days_spent
weeks_left = weeks_in_90years - weeks_spent
month_left = months_in_90years - months_spent

print(f"if you are to die at 90years, you have {days_left} days, {weeks_left} weeks and {month_left} months left")

# project tip calculator

print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people_to_split = input("how many people to split the bill? ")

float_total_bill = float(total_bill)
float_percentage_tip = float(percentage_tip)
float_people_to_split = float(people_to_split)

percentage_tip_amount = (float_percentage_tip / 100) * float_total_bill

total_and_percentage_tip_amount = float_total_bill + percentage_tip_amount

amount_each_person_pay = total_and_percentage_tip_amount / float_people_to_split

rounded_amount_pay_per_person = round(amount_each_person_pay, 2)

print(f"Each person should pay: ${rounded_amount_pay_per_person}")