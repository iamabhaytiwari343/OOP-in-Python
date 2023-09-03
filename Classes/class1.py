class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute: name
        self.age = age    # Attribute: age

    def introduce(self):
        return f"My name is {self.name}, and I am {self.age} years old."


person1 = Person("John Doe", 20)
print(person1.introduce())
person1 = Person("Alice", 30)  # Creating an object of the "Person" class
person2 = Person("Bob", 25)    # Creating another object of the "Person" class
print(person1.name)  # Accessing the "name" attribute of person1
introduction = person2.introduce()  # Calling the "introduce" method on person2
print(introduction)

