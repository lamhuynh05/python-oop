class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width) #super function
    
    def area(self):
        return self.length*self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width) #super function
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

square = Square(8, 3)
cube = Cube(3, 9, 3)

print(square.area())
print(cube.volume())
