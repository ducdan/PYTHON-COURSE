import math

class Circle:
    pi=3.14
    pi=3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def computeFre(inStr):
    inStr += ' '

    split_Str = list(set(inStr.split())) # Split and remove the same words
    split_Str.sort()      # Sort list of words according to the key alphanumerically
    # [The,sentence,...]
    # Compute the frequency of each word
    freq = []
    for i in split_Str:
        i += ' '
        freq.append(inStr.count(i))

    # Show result
    for i in range(len(split_Str)):
        print("   {}: {}".format(split_Str[i], freq[i]))

while (True):
    print
    print ('Please enter 1, 2, 3 to continue one of exercises. Enter the others to stop.')
    ex = input('Enter the exercise: ')

    if (ex == '1'):     # Exercise 1
        #Str = input('   Enter the sentence: ')
        Str = 'New to Python or choosing between Python 2 and Python 3? Read Python 3 or Python 2. '
        computeFre(Str)
    elif (ex == '2'):   # Exercise 2
        rad = float(input('   Nhap vao ban kinh: '))
        aCircle = Circle(rad)
        print("   Dien tich hinh tron la: %.2f" % aCircle.area())
    elif (ex == '3'):   # Exercise 3
        len = float(input('   Nhap vao chieu dai: '))
        wid = float(input('   Nhap vao chieu rong: '))
        aRec = Rectangle(len, wid)
        print('   Dien tich hinh chu nhat la: %.2f' % aRec.area())
    else:      # Stop program
        print ('Stopping...')
        break




