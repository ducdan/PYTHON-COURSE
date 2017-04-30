
import random

class Wheels:
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

class Frames:
    def __init__(self, material, weight, cost):
        self.material = material
        self.weight = weight
        self.cost = cost

class Bicycle_Manufacturers:
    def __init__(self, name, models, per_cost):
        self.name = name
        self.models = models
        self.per_cost = per_cost

class Bicycle:
    def __init__(self, name, wheels, frames, manufacturer):
        self.name = name
        self.wheels = wheels
        self.frames = frames
        self.manufacturer = manufacturer
        self.weight = 2*self.wheels.weight + self.frames.weight
        self.cost = 2*self.wheels.cost + self.frames.cost

class Bikes_Shops():
    def __init__(self, name, per_cost):
        self.name = name
        self.per_cost = per_cost
        self.inventory = []
        self.profit = 0
    def show_inventory(self):
        for i in self.inventory:
            print ("   -{}: ---nặng {} kg "
                   "        ----giá {}$".format(i.name, i.weight, i.cost))

class Customers:
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.owned_bikes = []
    def afford_bike(self, shp):
        l = []
        for bike in shp.inventory:
            sold_cost = bike.cost * (1 + shp.per_cost)
            if (sold_cost < self.fund):
                l.append(bike)

        return l

# Wheels
whe1 = Wheels('Wheels1', 4, 400)
whe2 = Wheels('Wheels2', 3, 200)
whe3 = Wheels('Wheels3', 2, 70)

# Frames
fra1 = Frames('Frames1', 2, 400)
fra2 = Frames('Frames2', 3, 100)
fra3 = Frames('Frames3', 4, 60)

# Manufacturers
vn = Bicycle_Manufacturers('Viet Nam', ['Thống Nhất', 'Thể Thao', 'Xiteen'], .20)
nn = Bicycle_Manufacturers('Nuoc Ngoai', ['Martin', 'Asama', 'Hello Kitty'], .25)
vnnn = Bicycle_Manufacturers('VietNam & NuocNgoai', ['Martin', 'Xiteen', 'Asama'], 0.30)

# Create a bicycle shop that has 6 different bicycle models in stock.

mod1 = Bicycle('Martin', whe2, fra1, nn)
mod2 = Bicycle('Thống Nhất', whe3, fra2, vn)
mod3 = Bicycle('Thể Thao', whe3, fra3, vn)
mod4 = Bicycle('Asama', whe1, fra2, vnnn)
mod5 = Bicycle('Xiteen', whe2, fra3, nn)
mod6 = Bicycle('Hello Kitty', whe1, fra1, vnnn)


shop = Bikes_Shops('Shop1', .20)
shop.inventory = [mod1, mod2, mod3, mod4, mod5, mod6]


#Create three customers.
cus1 = Customers('Tín', 200)
cus2 = Customers('Nam', 500)
cus3 = Customers('Huy', 1000)
list_cus = [cus1, cus2, cus3]


#Print the name of each customer, and a list of the bikes offered.
for i in list_cus:
    lst = i.afford_bike(shop)
    print("{} có thể mua: {}".format(i.name, [lst[j].name for j in range(len(lst))]))


#Print the initial inventory of the bike shop for each bike it carries.
print ("---------------------------------------------")
print ('Hàng hóa của {}'.format(shop.name))
shop.show_inventory()

















