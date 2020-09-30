# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
# my_dict = dict()

# for i in range(1, 20):
#     my_dict[i] = i ** 2
    
# print(my_dict)

my_dict = {i:i**2 for i in range(1,21)}

print(my_dict)