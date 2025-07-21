#Defining and Calling a Function

def greet():
    print("Hello, welcome!")

greet() 


#Function with Parameters

def greet(name):
    print("Hello,", name)

greet("Alice")




#Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)





#Default Parameter Value
def greet(name="Guest"):
    print("Hello,", name)

greet()       
greet("Bob") 




#Function with Multiple Return Values

def get_details():
    name = "Alice"
    age = 25
    return name, age

n, a = get_details()
print("Name:", n, "| Age:", a)




#Function with *args (Multiple Arguments)

def add_all(*numbers):
    return sum(numbers)  # sum is the predefined function

print(add_all(1, 2, 3, 4, 5))  #output:



#Function with **kwargs (Keyword Arguments)
def info(**details):
    for key, value in details.items():
        print(key, ":", value)

info(name="Alice", age=25, city="New York")





# Create a function to get 5 subject mark from the user 
# Create a function to find the total of all marks
# Display all the marks and total
# Function to display the grade based on the total
# Function to display the student based on the grade order (like A ,B ,C)

