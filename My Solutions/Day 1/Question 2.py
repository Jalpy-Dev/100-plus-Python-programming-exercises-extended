'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8 Then, the output should be:40320
'''


def factorial_finder(num):
    '''
    Finds factorial
    '''
    x_num = 1
    for i in range(1, num + 1):
        x_num = i * x_num
    return x_num


print(factorial_finder(8))


# Hella smart way
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)

# x = int(raw_input())
# print fact(x)
