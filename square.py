# I'm going to create a program that will display 
# the square root of a number.
# first I'm going to declare a variable a.
# and then a second variable b to hold the square root of a.
# and then print a message that will ask the user to 
# enter the desire number as the input
# And last I'll use the math library to display 
# the result of the square root of a.

import math
a = int(input("please enter the value a:"))
b = math.sqrt(a)
print("the result of the square root is:", b)
