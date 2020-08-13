# With a given integral number n, write a program to generate a dictionary
# that contains (i, i x i) such that is an integral number between 1 and n
# (both included). and then the program should print the dictionary.Suppose
# the following input is supplied to the program: 8


def dict_gen(num):
    dict1 = {}
    for i in range(num + 1):
        dict1.update({i: i * i})
    return dict1


print()
print(dict_gen(8))
