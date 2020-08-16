# Define a function which can compute the sum of two numbers.

def sum_func(num1, num2):
    try:
        return int(num1 + num2)
    except ValueError as err:
        return 'Please input a number', err


print(sum_func(5, 10))
