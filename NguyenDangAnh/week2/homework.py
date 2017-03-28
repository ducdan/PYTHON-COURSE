2
pi=3.14
class Circle :
    def __init__(self, r):
        self.r=r
    def area(self):
        return (self.r**2)*pi

aCircle = Circle(2)
print( 'diện tích hình tròn là: %s' %aCircle.area())
#
3
class Rectangle :
    def __init__(self,length , width):
        self.length = length
        self.width = width
    def area(self): return self.length * self.width


aRectangle = Rectangle(2,4)
print('diện tích hình chữ nhật là: %s' %aRectangle.area())

1
# string =input( "nhập vào một chuỗi: ")
# key = "a"
#
#
# def count_words( key):
#     return float(len(string) - len(string.replace(key, ''))) / float(len(key))
#
#
# dem = count_words(key)
# print("output:%s: %d" % (key, dem))




