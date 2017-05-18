# Bicycle Project
import random

class Wheels:
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

class Frames:
    def __init__(self, material, weight, cost):
        self.material = material    #{aluminum, carbon, steel}
        self.weight = weight
        self.cost = cost
#-------------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------------
class Bikes_Shops():
    def __init__(self, name, per_cost):
        self.name = name
        self.per_cost = per_cost
        self.inventory = []
        self.profit = 0
    def show_inventory(self):
        for i in self.inventory:
            print ("   {} nang {} kg va co gia goc {}$".format(i.name, i.weight, i.cost))
    def sell_bikes(self, model, customer):
        self.inventory.remove(model)
        customer.owned_bikes.append(model)
        customer.fund -= model.cost * (1 + self.per_cost)
        self.profit += model.cost * self.per_cost
        print ("{} mua {} voi gia {}$. Tai khoan con {}$.".format(customer.name, model.name, model.cost * (1 + self.per_cost), customer.fund))
#-------------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------------
# Wheels
clincher = Wheels('Clincher', 3, 500)
tubular = Wheels('Tubular', 2, 100)
tubeless = Wheels('Tubeless', 2, 50)

# Frames
alum = Frames('Aluminum', 3, 300)
carbon = Frames('Carbon', 4, 200)
steel = Frames('Steel', 5, 50)

# Manufacturers
yamaha = Bicycle_Manufacturers('Yamaha', ['Road', 'Mountain', 'Touring'], .20)
vindec = Bicycle_Manufacturers('Vindec', ['Utility', 'Road', 'Racing'], .25)
cube = Bicycle_Manufacturers('Cube', ['Sport', 'Racing', 'Mountain'], 0.30)
#-------------------------------------------------------------------------------------
# 1. Create a bicycle shop that has 6 different bicycle models in stock.
# Bicycle
mod0 = Bicycle('Model 0', clincher, alum, vindec)
mod1 = Bicycle('Model 1', tubular, alum, yamaha)
mod2 = Bicycle('Model 2', tubeless, steel, cube)
mod3 = Bicycle('Model 3', clincher, steel, cube)
mod4 = Bicycle('Model 4', tubular, carbon, vindec)
mod5 = Bicycle('Model 5', tubeless, carbon, yamaha)

# Bikes Shop
shop = Bikes_Shops('Bikes', .20)
shop.inventory = [mod0, mod1, mod2, mod3, mod4, mod5]

# -------------------------------------------------------------------------------------
# 2. Create three customers.
Customers
cus0 = Customers('Tom', 200)
cus1 = Customers('Maria', 500)
cus2 = Customers('John', 1000)
list_cus = [cus0, cus1, cus2]

#-------------------------------------------------------------------------------------
# 3. Print the name of each customer, and a list of the bikes offered.
for i in list_cus:
    lst = i.afford_bike(shop)
    print("{} co the mua: {}".format(i.name, [lst[j].name for j in range(len(lst))]))

# -------------------------------------------------------------------------------------
# 4. Print the initial inventory of the bike shop for each bike it carries.
# print ("---------------------------------------------")
# print ('Kiem ke hang hoa cua {}'.format(shop.name))
# shop.show_inventory()
#
# # -------------------------------------------------------------------------------------
# # 5. Buy bike for each customer.
# print ("---------------------------------------------")
# for i in list_cus:
#     lst = i.afford_bike(shop)
#     bike = random.choice(lst)
#     shop.sell_bikes(bike, i)
#
# #-------------------------------------------------------------------------------------
# # 6. The bicycle shop's remaining inventory & profit
# print("----------------------------------------------")
# print("Kiem ke hang hoa con lai trong kho cua {}:".format(shop.name))
# shop.show_inventory()
# print ("Loi nhuan cua cua hang: {}".format(shop.profit))











