# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of
# the number is an even number.The numbers obtained should be printed in a comma-separated sequence on
# a single line.


def even_num_finder(start, finish):
    even_numbers = []
    for num in range(start, finish + 1, 1):
        if num % 2 == 0:
            even_numbers.append(num)

    for num in even_numbers:
        print(num, end=', ')


even_num_finder(1000, 3000)
