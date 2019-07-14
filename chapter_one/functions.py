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
def display(arg1, arg2, arg3):
    print(arg1)


# keyword
# arg1 = "pec"
display(arg1=1, arg3=3, arg2=2)

# default


def display_default(arg1='this is default string'):
    print(arg1)


# double gap
display_default("this is new string")

# length argument


def display_length(arg, *arg1): # * -> more than one
    print(arg1)


display_length(1)


# inline function
# only one body
# lambda
# anyonomous function


inline_function = lambda arg1, arg2: arg1 + arg2

inline_function(1, 3)


#  Exercise
# input sentence
# word sorted -> ascending
# print first word and last word


def print_first_and_last_word():
    """
    It is used to print first and last word
    :return: word
    """
    sentence = input("Enter a sentence: ")
    # split
    # "The man from Kathmandu"
    # the, man , from
    words = sentence.split(' ')
    print(words)
#     sorted()
    sorted_word = sorted(words)
    print(sorted_word)
#     first and last word
    print("First Word: %s" % sorted_word[0])
    print("Last Word: %s" % sorted_word[-1])

print_first_and_last_word()

# print_first_and_last_word :
#     sort function
#     print function

