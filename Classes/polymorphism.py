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


class Duck(Animal):
    def speak(self):
        return "Quack!"

# Function that uses polymorphism


def animal_sound(animal):
    return animal.speak()


# Create instances of different animal classes
dog = Dog()
cat = Cat()
duck = Duck()

# Call the function with different animal objects
print("Dog says:", animal_sound(dog))
print("Cat says:", animal_sound(cat))
print("Duck says:", animal_sound(duck))

# Polymorphism is one of the four fundamental principles of object-oriented programming (OOP), along with encapsulation, inheritance, and abstraction. It allows objects of different classes to be treated as objects of a common superclass. In Python, polymorphism is achieved through method overriding, where a subclass provides a specific implementation of a method that is already defined in its superclass. Polymorphism simplifies code and makes it more flexible and extensible.
