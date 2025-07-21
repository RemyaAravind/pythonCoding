
# super() 
# call the parent class
class Parent(): 
	
	def show(self): 
		print("Inside Parent") 
		
class Child(Parent): 
	
	def show(self): 
		
		# Calling the parent's class 
		# method 
		
		super().show()  #invoking the super class method
		print("Inside Child") 
		

obj = Child() 
obj.show()   # parent class show or child class show()  //Inside Parent Inside Child

obj1=Parent()
obj1.show()  
