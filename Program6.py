class Color:

    def __init__(self):
        self.name = 'Green'
        self.lg = self.Lightgreen()    ###inner class invocation

    def show(self):
        print('Name:', self.name)

    class Lightgreen:           #inner class created with the name Lightgreen

        def __init__(self):
            self.name = 'Light Green'
            self.code = '024avc'

        def display(self):
            print('Name:', self.name)
            print('Code:', self.code)

outer = Color()     #outer class object creation 
  # line 5 inner class instantiation is also happening(_init_ method inside Lightgreen is calling)

outer.show()        #outer class method invocation

#inner=Lightgreen() # invoking 

g = outer.lg        #inner class object creation
g.display()         #inner class method calling

#we have two classes remote and battery. Every remote needs a battery 
# but a battery without a remote won’t be used.
# So, we make the Battery an inner class to the Remote.
#college and department