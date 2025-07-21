try:
    # file = open('data.txt', 'r')
    # data = file.read()
    # number = int(data)
    value = int(input("Enter a number: "))
    result = 10 / value
   
except ZeroDivisionError:
    print("Divide by zero error!")
except ValueError:
    print("Invalid data as input!")
else:
    # Executed only if no exceptions occurred
    print(f"Successfully divided: {value}")
finally:
    # Always executed, regardless of exceptions
    # if 'file' in locals():
    #     file.close()
    print("Project Execution completed")