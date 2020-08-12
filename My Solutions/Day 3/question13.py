# Write a program that accepts a sentence and calculate the number of letters and digits.
#
# Suppose the following input is supplied to the program:
#
# hello world! 123
# Then, the output should be:
#
# LETTERS 10
# DIGITS 3

raw_input = input('Please input a sentence: ')

total_str, total_int = 0, 0

for char in raw_input:
    if char.isalpha():
        total_str += 1
    elif char.isnumeric():
        total_int += 1

print(f'Total letters: {total_str} \n Total numbers: {total_int}')
