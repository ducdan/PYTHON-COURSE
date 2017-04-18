import math
#2
class Circle :
    pi = 3.14
    def __init__(self, r):
        self.r = r

    def area(self):
        return (self.r**2)*self.pi

cir1 = Circle(5)
print("Diện tích hình tròn: {}(đvdt)".format(cir1.area()))

#3
class Rectangle :
    def __init__(self,length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rec1 = Rectangle(5,4)
print("Diện tích HCN: {}(đvdt)".format(rec1.area()))

