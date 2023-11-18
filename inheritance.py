class Animal: #parent class
    alive = True

    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    #child class inherit using () and everything that parent class has inside
    def run(self):
        print("This animal is running")

class Fish(Animal):
    def swim(self):
        print("This animal is swimming")

class Hawk(Animal):
    def fly(self):
        print("This animal is flying")

# create objects from the classes above
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#inheritance
print(rabbit.alive) #class variable
# methods using functions in the parent class
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()