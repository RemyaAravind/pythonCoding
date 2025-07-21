#Python subclass
class Animal:
    def __init__(self, name):
        self.name = name  

    def species(self):
         return "Hello"
       

class Dog(Animal):    #create the child class
    def sound(self):
            return "Woof!"


a = Animal("Generic Animal")  # init method

d = Dog("Buddy")  

# Accessing attributes and methods
print(a.name)  # Output: Generic Animal
print(d.name)    # Output: Buddy
print(d.sound())  # Output: Woof!


print(a.sound())
print(a.species())   #

print(d.sound())
print(d.species())   #



