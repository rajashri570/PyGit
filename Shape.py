class Shape:
    def cal_area(self):
        pass
    def cal_perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def cal_area(self):
        return 3.14 * self.r * self.r
    def cal_perimeter(self):
        return 2 * 3.14 * self.r
class Rectangle(Shape):
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def cal_area(self):
        return self.l * self.w
    def cal_perimeter(self):
        return 2 * (self.l + self.w)
    
c = Circle(3)
print("Area of circle : ",c.cal_area())
print("Perimeter of circle : ",c.cal_perimeter())
r = Rectangle(4,5)
print("Area of rectangle : ",r.cal_area())
print("Perimeter of rectangle : ",r.cal_perimeter())
