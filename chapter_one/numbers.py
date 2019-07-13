# numbers
# 3 types
# int
# float
# complex

int_number = 1
float_nummber = 1.0
complex_number = 1j

# expression
# +
# -
# /
# *
# % value -> int, float, complex
# <
# >
# >=
# <= -> value boolean -> true/ false

# do expression
# count number of student in class
girls = 6
boys = 20
print("total number of students %d " % (girls + boys))

total_student = 26
print("Number of girls in class %d" % (total_student - boys))
print("Count %.2f" % (20 - 10 / 5 * 6))

# % modulusP
print("calculate %f" % (25 % 6))
print(5 / 4)

# boolean expression
print("Is 5 greater than 4", 5 > 4)
print("Is 5 greater than equal to 4", 5 >= 4)

# ! -> not
# used on conditional

number_1 = 10
number_2 = 45
number_3 = 20
calculate = number_1 * number_2 / number_3
print(calculate)

#  input prompt
# inbult function
# takes user input
#  function -> input() python 3
# python 2 -> raw_input()

# example
name = input("Type your name: ")
print("welcome to python %s" % name)

# input -> always take only string
age = input("Enter your age :")
print("Your age is %f " % (float(age) + 1))

# conditional -> if

# name
# age
# give result > adult, child, aged
#  child ->less than equal 16
# adult -> greater than 16 less than equal 30
# aged -> greater than 30

# if - condition -> statement
# #
# if (condition):
#     statement
#
# # nested
# if(condition):
#     pass
# elif(condition):
#     pass
# else:
#     pass
#

name = input("Enter your name :")
age = input("Enter your age: ")
typecast_age = int(age)

if typecast_age <= 16:
    print("%s is child" % name)
elif 16 < typecast_age <= 30:
    print("%s is adult" % name)
else:
    print("%s is aged" % name)

# function

