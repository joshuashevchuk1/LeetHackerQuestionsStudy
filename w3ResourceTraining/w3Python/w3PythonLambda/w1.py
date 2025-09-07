#
# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and prints the result.
#

def add15():
    return lambda a : a + 15


l1=add15()

print(l1(1))
print(l1(2))
