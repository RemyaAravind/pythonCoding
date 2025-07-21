
#Exception handling in Python allows you to gracefully manage
#  errors that occur during program execution.

try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")



#####################################################################
try:
    value = int(input("Enter a number: "))  #asd .0
    result = 10 / value 
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")


#Handle multiple exceptions in one block
try:
    # Some code
    pass
except (ValueError, TypeError, ZeroDivisionError) as e:    #catch(Exception e){}
    print(f"An error occurred: {e}")

    #printing all the error

    