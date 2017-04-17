class Frame(object):
    def __init__(self,name = "" , weight = None, cost = None):
        self.name = name
        self.weight = weight
        self.cost = cost
    
class Wheel(object):
    def __init__(self,material = "", weight = None, cost = None):
        self.material = material
        self.weight = weight
        self.cost = cost

class Manufacturer(object):
    def __init__(self, name = "", overcost = 0):
        self.name = name
        self.overcost = overcost
        
class Bicycle(object):
    def __init__(self, mname = "", frame = Frame(), wheel = Wheel(), manufacturer = Manufacturer()):
        self.mname = mname
        self.cost = frame.cost + wheel.cost*2
        self.weight = frame.weight + wheel.weight*2
        self.manufacturer = manufacturer

        
    