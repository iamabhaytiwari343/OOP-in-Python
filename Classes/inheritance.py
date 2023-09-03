# Base class (superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Subclass (derived class)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Subclass (derived class)
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create objects of the derived classes
dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")

# Call methods of the derived classes
print(dog1.speak())  # Output: "Buddy says Woof!"
print(cat1.speak())  # Output: "Whiskers says Meow!"
