# Define a class, which have a class parameter and have a same instance parameter.

class Person:
    name = 'Person'

    def __init__(self, age, name, gender):
        self.info = {
            'age': age,
            'name': name,
            'gender': gender
        }

    def print_info(self):
        print(self.info)
        for k in self.info:
            print(k, self.info.get(k))


dylan = Person(28, 'Ryan', 'm')
dylan.print_info()
