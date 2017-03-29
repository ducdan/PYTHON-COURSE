# ----------------------------------------
class Bicycle():
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
# ----------------------------------------
class Bike_shop(Bicycle):
    account = 10000
    profit = 0
    stock = []
    def __init__(self, name, *bikes):
        self.name = name
        for bike in bikes:
            self.stock.append(bike)
            self.account -= bike.cost

    def import_bike(self, *bikes):
        for bike in bikes:
            self.stock.append(bike)
            self.account -= bike.cost

    def export_bike(self, *bikes):
        for bike in bikes:
            self.stock.remove(bike)
            self.account += (1 + 0.2) * bike.cost
            self.profit += 0.2 * bike.cost

    def inventory_stock(self):
        for model in self.stock:
            print("_Name: {}, Weight: {}, Price: {}".format(model.name, model.weight, model.cost))
# ----------------------------------------
class Customer():
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def buy_bike(self, bike):
        self.budget -= (1 + 0.2) * bike.cost
# ----------------------------------------
class Wheel():
    wheel_types = ("Straight", "Circle", "Sphere")
    def __init__(self, name, weight, cost, type = "Circle"):
        self.name = name
        self.weight = weight
        self.cost = cost
        self.type = type
# ----------------------------------------
class Frame():
    material_types = ("Aluminum", "Carbon", "Steel")
    def __init__(self, weight, cost, material = "Steel" ):
        self.weight = weight
        self.cost = cost
        self.material = material
# ----------------------------------------
class Manufacturer():
    def __init__(self, name):
        self.name = name

    def produce_bike(self, bike_1, bike_2, bike_3):
        self.bike_1 = bike_1
        self.bike_2 = bike_2
        self.bike_3 = bike_3

    def percentage(self, bike):
        self.profit += 0.2 * bike.cost
# ----------------------------------------
class Bicycle_parts(Wheel, Frame):
    def __int__(self, wheel, frame):
        self.wheel_1 = wheel
        self.wheel_2 = wheel
        self.frame = frame
        self.weight = 2 * self.wheel_1.weight + self.frame.weight
        self.cost = 2 * self.wheel_1.cost + self.frame.cost
# ----------------------------------------
class Bicycle_m(Manufacturer):
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer











