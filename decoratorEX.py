
#Decorator will help us to add extra functionality to the exisiting function without changing the code 

#logging ,authentication ,database functionality 

# 


import inspect

def decorator(func):
    
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function

@decorator  #greet = decorator(greet)
def greet():
    print("Hello, World!")

greet()

print(inspect.signature(decorator))






# Explanation:

# decorator takes the greet function as an argument.
# It returns a new function (wrapper) that first prints a message,
# calls greet() and then prints another message.
# The @decorator syntax is a shorthand for greet = decorator(greet).