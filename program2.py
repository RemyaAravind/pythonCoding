#Using __init__() Function
#In Python, class has __init__() function.
# It automatically initializes object attributes when an object is created.

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1=Dog()  ###
dog2 = Dog("Buddy", 3)

print(dog1.name)  # Output: Buddy
print(dog2.species)  # Output: Canine
print(dog2.age)
print(dog2.name)


#self parameter is a reference to the current instance of the class.
# It allows us to access the attributes and methods of the object.


