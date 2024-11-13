import math
class Main:
    def __init__(self,r):
        self.radius=r
    def circle_area(self):
        return math.pi*self.radius*self.radius
    def circle_perimeter(self):
        return 2*math.pi*self.radius
r=float(input())
circle=Main(r)
print("area of a circle is:",circle.circle_area())
print("perimeter of a circle",circle.circle_perimeter())
