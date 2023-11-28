class Car:
    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engines")
        return self

car = Car()

# call 2 methods at once
car.turn_on().drive()

# # call all 4 methods 
car.turn_on().drive().brake().turn_off()

# if we call many methods:
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
