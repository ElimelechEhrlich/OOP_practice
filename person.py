class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1   

    def introduce(self):
        return f'Hi, my name is {self.name} and I am {self.age} years old.'

p1 = Person('Elimelech', 29)
print (p1.introduce())
p1.birthday()
p1.birthday()
print (p1.introduce())
