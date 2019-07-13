print('hello world')
print("HEllo world")
print("""Hello
world
pec""")
print("hello world", end='\n')
print("Hello", "world", sep="------")
print("hello", "world")

# this is in line comment
print("inline comment")
# print("print this")
print("print not")

# Vairable:
#     container
#     value
#     a -> int a;

# price -> p
# description -> desc
day = 1  # container
week= "first"
print(day)
# print("Today is day " + day)  # string concatination
print("Today is day " + str(day))  # type casting
print("Today is day %d " % day)  # string formatting
print("Today is day %.2f %5s " % (day, week))  # string formating

# %d -> integer
# %f -> float
# %r -> testing
# %s -> string

# Number
# type
# integer
# float
# complex

price = 1
price = 1.0
# price = 1J

# string Vs integer
integer_price = 1
float_price = 1.0
string_price = "IamPrice"
# string_price = new String("IamPrice")

print(type(integer_price))
print(type(string_price))
print(type(float_price))
print(string_price.capitalize())
print(string_price[0:2])

# string escaping
print('hello\\ world')