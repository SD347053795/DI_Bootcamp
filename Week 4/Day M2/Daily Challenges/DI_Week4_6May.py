import math
class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Please provide either radius or diameter")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

c1 = Circle(radius=3)
c2 = Circle(diameter=4)
print(c1.radius)
print(c2.diameter)
print(c1.area)
print(c1)

c3 = c1 + c2
print(c3.radius)

print(c1 < c3)
print(c1 == c2)
print(c1 > c2)
circles = [Circle(radius=5), Circle(radius=3), Circle(radius=7)]
sorted_circles = sorted(circles)
for circle in sorted_circles:
    print(circle)

# #Bonus
# import turtle
# def draw_circle(radius):
#     turtle.circle(radius)
# turtle.speed(0)  # Set the speed to the maximum
# turtle.penup()
# for circle in sorted_circles:
#     turtle.penup()
#     turtle.setpos(0, -circle.radius)
#     turtle.pendown()
#     draw_circle(circle.radius)
#     turtle.penup()
#     turtle.setpos(0, 0)
# turtle.done()

#Gold
get_input = lambda: (input("Name: "), int(input("Age: ")), int(input("Score: ")))
data = [get_input() for _ in range(5)]
sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2]))
print(sorted_data)
