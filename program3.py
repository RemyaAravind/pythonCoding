class Dog:
    def __init__(self, name, age): #when you create the object
        self.name = name
        self.age = age

    def __str__(self):  # print the object ie like toString()
        return f"{self.name} is {self.age} years old."  # Correct: Returning a string

dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1)  # _str_
print(dog2)  