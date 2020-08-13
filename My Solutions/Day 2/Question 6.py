import math
# Question:
# Write a program that calculates and prints the value according to the given:

# Q = Square root of [(2 _ C _ D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a
# comma-separated sequence.For example Let us assume the following comma
# separated input sequence is given to the program:

# 100,150,180
# The output of the program should be:

# 18,22,24


values = input('Enter values seperated by a comma: ').split(',')


final = []

for i in values:
    i = int(i)
    final.append(int(math.sqrt((2 * i * 50) / 30)))


print(final)
