class Wheels:
    def __init__(self, name, wweight, wcost):
        self.name = name
        self.wweight = wweight
        self.wcost = wcost

class Frames:
    def __init__(self, material, fweight, fcost):
        self.material = material
        self.fweight = fweight
        self.fcost = fcost
class Manufacturers:
    def __init__(self, name, models, money):
        self.name = name
        self.mod_bike = models
        self.money = money
class Bicycle:
    def __init__(self, mod_name, wheels, frames, manufacturer):
        self.mod_name = mod_name
        self.wheels = wheels
        self.frames = frames
        self.manufacturer = manufacturer
        self.weight = 2 * self.wheels.wweight + self.frames.fweight
        self.cost = self.wheels.wcost + self.frames.fcost

class Bike_Shops(Bicycle):
    def __init__(self, name, money):
        self.name = name
        self.inventory = []
        self.money = money
        self.profit = (0.1*mod6.cost +0.2*mod6.cost) + (0.1*mod4.cost +0.2*mod4.cost) + (0.2*mod1.cost +0.2*mod1.cost)
    def the_initial_inventory(self):
        for i in self.inventory:
            print(" Model {}: {}kg--{}$(chưa bao gồm VAT)".format(i.mod_name, i.weight, i.cost))

class Customers:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
    def afford_buy(self, i):
        lst = []
        for bike in i.inventory:
            price = bike.cost * (1 + i.money)
            if (price <= self.budget):
                lst.append(bike)
        return lst

# Wheels
f1 = Wheels('F1', 1.5, 300)
f2 = Wheels('F2', 2, 150)
f3 = Wheels('F3', 2, 50)

# Frames
aluminum = Frames('Aluminum', 2, 300)
carbon = Frames('Carbon', 3, 150)
steel = Frames('Steel', 4, 50)

# Manufacturers
giant = Manufacturers('Giant', ['Road Bike', 'Mountain Bike', 'Hybrid Bike'], .20)
jett = Manufacturers('Jett', ['BMX Bike', 'Folding Bike', 'Fixed Bike'], .15)
galaxy = Manufacturers('Galaxy', ['Folding Bike', 'Touring Bike', 'Hybrid Bike'], .10)
# Create a bicycle shop that has 6 different bicycle models in stock.
# Bicycle
mod1 = Bicycle('S+', f1, aluminum, giant)
mod2 = Bicycle('S', f1, carbon, jett)
mod3 = Bicycle('A', f2, aluminum, giant)
mod4 = Bicycle('B', f3, carbon, galaxy)
mod5 = Bicycle('C', f2, steel, giant)
mod6 = Bicycle('D', f3, steel, galaxy)

# Bikes Shop
shop = Bike_Shops('Lucias', .20)
shop.inventory = [mod1, mod2, mod3, mod4, mod5, mod6]

# Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
# Customers
cus1 = Customers('Luci', 200)
cus2 = Customers('Rei', 500)
cus3 = Customers('Ez', 1000)
list_cus = [cus1, cus2, cus3]

# Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget.

for customer in list_cus:
    lst = customer.afford_buy(shop)
    print("{} có thể mua xe rank: {}".format(customer.name, [lst[bicycle].mod_name for bicycle in range(len(lst))]))

# Print the initial inventory of the bike shop for each bike it carries.
print('__________')
print ('Bản kiểm kê ban đầu của cửa hàng {}:'.format(shop.name))
shop.the_initial_inventory()

# print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.
print('__________')
print("{} mua xe rank: {} với giá {}, tài khoản còn lại {}".format(cus1.name, mod6.mod_name,(0.2*mod6.cost+mod6.cost) , cus1.budget-((0.2*mod6.cost+mod6.cost))))
shop.inventory.remove(mod6)
print("{} mua xe rank: {} với giá {}, tài khoản còn lại {}".format(cus2.name, mod3.mod_name,(0.2*mod4.cost+mod4.cost) , cus2.budget-((0.2*mod4.cost+mod4.cost))))
shop.inventory.remove(mod4)
print("{} mua xe rank: {} với giá {}, tài khoản còn lại {}".format(cus3.name, mod6.mod_name,(0.2*mod1.cost+mod1.cost) , cus3.budget-((0.2*mod1.cost+mod1.cost))))
shop.inventory.remove(mod1)
#  print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.
print('__________')
print("Các mẫu xe còn lại trong cửa hàng {}:".format(shop.name))
shop.the_initial_inventory()
print ("Profit: {}".format(shop.profit))
