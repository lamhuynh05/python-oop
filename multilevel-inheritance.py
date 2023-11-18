class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This animal is barking")

dog = Dog()
dog.eat()
print(dog.alive)
dog.bark()