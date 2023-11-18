# when class is large -> place class into separate module
class Car:
# special method __init__(): construct objects/constructor
# init = initialize 
# set up parameters inside the ()
# assign received arguments to attributes in __init__ method -> 
    wheels = 4
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        # these are attributes
        # attributes can be anything since self.make = make

# define methods for object car:
    def drive(self): # self is argument, refers to object using this method
        print("This "+self.model+ " is driving")

    def stop(self):
        print("This "+self.model+ " is stopped!")
