# Question:
# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods


class cool_class():
    def __init__(self):
        self.getString()
        self.printString()

    def getString(self):
        self.text = input('Type something please: ')

    def printString(self):
        print(self.text)


person1 = cool_class
person1()
