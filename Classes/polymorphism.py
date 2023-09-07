# Polymorphism allows objects of different classes to be treated as objects of a common superclass. It is often achieved through method overriding. In Python, you can override methods in a subclass to provide a specific implementation.

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"
