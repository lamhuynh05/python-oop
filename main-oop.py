from car import Car

# create object
# to construct car object -> we need matching sets of argument
# in python, we don't need to pass any argument for self 
car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red" )
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_2.stop()

car_1.wheels = 2
print(car_1.wheels)
print(car_2.wheels)