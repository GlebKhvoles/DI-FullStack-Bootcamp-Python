import math
class Circle:
    def __init__(self, area):
        self.area = area
    @classmethod
    def create_by_radius(cls, radius):
        return cls(math.pi * (radius**2))
    @classmethod # great solution
    def create_by_diameter(cls, diameter):
        return cls(math.pi / 4 * (diameter**2))
    def __repr__(self):
        return f"I'm circle with area equal {self.area}"
    def __add__(self, other):
        if isinstance(other, Circle): # what if it's not Circle then what you want to do? the same about the functions __eq__, __lt__, __gt__
            self.area += other.area
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.area == other.area
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.area < other.area
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.area > other.area


circle_1 = Circle.create_by_radius(7)
circle_2 = Circle.create_by_diameter(18)
circle_3 = Circle.create_by_diameter(13)
print(circle_1)
print(circle_2)

circle_1 + circle_2
print(circle_1)

if circle_1 > circle_2:
    print('Circle 1 bigger than cirle 2')

if circle_1 < circle_2:
    print('Circle 2 bigger than cirle 1')

if circle_3 == circle_2:
    print('Circle 2 and cirle 3 are equal')

circle_2 + circle_3
list_circles = [circle_1, circle_2, circle_3]
list_circles.sort()
print(list_circles)
