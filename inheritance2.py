class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def show(self):
        print(f"The color of the shape is {self.color}")


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius**2  


class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def area(self):
          return self.width**2


class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def area(self):
        return 0.5 * self.width * self.height  # Formula for the area of a triangle



circle = Circle("Red", True, 7)
circle.show()
print(f"The area of the circle is {circle.area()}")

square = Square("Blue", False, 5)
square.show()
print(f"The area of the square is {square.area()}")

triangle = Triangle("Green", True, 6, 4)
triangle.show()
print(f"The area of the triangle is {triangle.area()}")
