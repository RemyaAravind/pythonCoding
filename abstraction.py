#Data abstraction in Python is a programming concept that hides complex 
# implementation details while exposing only essential information and 
# functionalities to users.

from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method (must be implemented in child classes)

# Concrete Class (inherits and implements abstract methods)
class Dog(Animal):
    def make_sound(self):
        return "Bark!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Trying to instantiate an abstract class will cause an error:
# a = Animal()  # TypeError: Can't instantiate abstract class

# Using concrete classes
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Bark!
print(cat.make_sound())  # Output: Meow!
