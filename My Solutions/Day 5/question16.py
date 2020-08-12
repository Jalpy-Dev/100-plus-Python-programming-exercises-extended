# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated
# numbers. >Suppose the following input is supplied to the program:
#
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
#
# 1,9,25,49,81

num_list = input('Please input a list of numbers seperated by commas: ').split(',')
num_list = list(map(lambda num: int(num), num_list))
final_list = []

for number in num_list:
    if number % 2 != 0:
        final_list.append(str(number ** 2))


print(', '.join(final_list))
