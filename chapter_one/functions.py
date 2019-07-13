# functions

# = , ==
a=5
if a==5:
    print(a)

# function
# -> declare ->
# name,
# parameter,
# function body
# return


def my_function(arg1):
    """
    It is used to print
    :param arg1: string
    :return: None
    """
    print(arg1)


my_function("Welcome")

# pass by reference vs pass by value
# Array
numbers = [1, 2, 3, 4]


# pass by reference
def change_numbers(array_list):
    print("Numbers before change", array_list)
    # local variable, scope -> locally
    numbers = [2, 3, 5]
    print("Numbers after change", numbers)

print("numbers before call ", numbers)
change_numbers(numbers)
print("numbers after call ", numbers)

# argument type
# -> required
# -> keyword
# -> default
# -> variable length


# required
def display(arg1,arg2, arg3):
    print(arg1)


# keyword
# arg1 = "pec"
display(arg1=1, arg3=3, arg2=2)
