# Define a class with a generator which can iterate the numbers, which are divisible by 7,
# between a given range 0 and n.
#
# Suppose the following input is supplied to the program:
#
# 7
# Then, the output should be:
#
# 0
# 7
# 14

class DivisBySeven:
    @staticmethod
    def divis_by_seven(endn):
        for num in range(0, endn):
            if num % 7 == 0:
                yield num


for i in DivisBySeven.divis_by_seven(21):
    print(i)
