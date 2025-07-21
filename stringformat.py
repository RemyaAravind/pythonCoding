a = "Revature" 
b = 22 

msg = "My name is {0} and I am {1} years old.".format(a,b)
print(msg)

#####################################################################
a = "Python"
print("This article is written in {}.".format(a))

print("Hi! My name is {} and I am {} years old.".format("User", 19))


#fstring
name = 'Om'
age = 22
print(f"Hello, My name is {name} and I'm {age} years old.")





#5!===5*4*3*2*1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) 