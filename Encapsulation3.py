class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute double underscore _ _

    def salary(self):
        return self.__salary  # Access through public method

obj = Private()
print(obj.salary())  # Works
#print(obj.__salary)  # Raises AttributeError
