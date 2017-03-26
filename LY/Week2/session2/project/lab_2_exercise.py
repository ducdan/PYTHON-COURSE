# --------------------------------------------------------------------------------
def frequency(sentence):
    """ Find frequency of each word in sentence"""
    sentence = str(sentence)              # make sure input is string type
    print("The sentence is: {}".format(sentence))
    words = sentence.split(" ")           # split sentence into words with space seperator
    freq = {}                             # frequency for every word in sentence

    for word in words:                    # count substring word in sentence
        freq[word] = sentence.count(word)

    print("Output: > ")
    for word_key in sorted(freq.keys()):  # sort words in abc order and print
        print("{} : {}".format(word_key, freq[word_key]))
# --------------------------------------------------------------------------------
st = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
frequency(st)

# --------------------------------------------------------------------------------
import math
# --------------------------------------------------------------------------------
class Circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
# --------------------------------------------------------------------------------
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
# --------------------------------------------------------------------------------
cir = Circle(3)
print(cir.area())
rec = Rectangle(2,5)
print(rec.area())

