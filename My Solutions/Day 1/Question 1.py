# Write a program which will find all such numbers which are divisible by 7 but
# are not a multiple of 5, between 2000 and 3200 (both included).The numbers
# obtained should be printed in a comma-separated sequence on a single line.


def div_by7(start, stop):
    for num in range(start, stop):
        if (num % 7 == 0) and (num % 5 != 0):
            print(num, end=', ')


div_by7(2000, 3201)
