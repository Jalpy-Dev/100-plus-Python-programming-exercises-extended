# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#
# Suppose the following input is supplied to the program:
#
# Hello world!
# Then, the output should be:
#
# UPPER CASE 1
# LOWER CASE 9

raw_input = input('Please enter a sentence: ')

uppercase, lowercase = 0, 0

for char in raw_input:
    if char.isupper():
        uppercase += 1
    if char.islower():
        lowercase += 1

print(f'Uppercase letters: {uppercase} \nLowercase letters: {lowercase}')
