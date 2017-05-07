import random

class Bicycle():
    def __init__(self, name, wheel, frame, manufacturer):
        self.name = name
        self.wheel = wheel
        self.frame = frame
        self.manufacturer = manufacturer
        self.weight = 2 * self.wheel.weight + self.frame.weight
        self.cost = 2 * self.wheel.cost + self.frame.cost
class Wheels():
    def __init__(self, name, wheel_weight, wheel_cost):
        self.name = name
        self.weight = wheel_weight
        self.cost = wheel_cost

wheel1 = Wheels('wheel1', 1, 20)
wheel2 = Wheels('wheel2', 1.5, 35)
wheel3 = Wheels('wheel3', 1.8, 40)

class Frames ():
    def __init__(self, material, weight, cost):
        self.material = material
        self.weight = weight
        self.cost = cost

aluminum = Frames('frame1', 15, 100)
carbon = Frames('frame2', 18, 150)
steel = Frames('frame3', 20, 100)

class Bike_shop(Bicycle):
    def __init__(self, name, per_cost):
        self.name = name
        self.per_cost = per_cost
        self.inventory = []
        self.profit = 0

    def show_inventory(self):
        for i in self.inventory:
            print ("tên    {}"
                   "    nặng {} kg "
                   "    giá {}$".format(i.name, i.weight, i.cost))

class Customers:
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.owned_bikes = []

#2 create three customer
customer1 = Customers('TÍN', 200)
customer2 = Customers('NGUYÊN', 500)
customer3 = Customers('ANH', 1000)
list_cus = [customer1, customer2, customer3]

class Manufacturers:
    def __init__(self, name, models, money):
        self.name = name
        self.mod_bike = models
        self.money = money

manufacturer1 = Manufacturers('Japan', ['Asama', 'Thể Thao'], .24)
manufacturer2 = Manufacturers('japan', ['Honda', 'Xe Đạp Điện'], .19)
manufacturer3= Manufacturers('japan', ['Martin', 'Xe Đạp'], 0.29)
#------------------------------
#1.Create a bicycle shop that has 6 different bicycle models in stock...
model1 = Bicycle('A', wheel1, aluminum, manufacturer1)
model2 = Bicycle('B', wheel2, carbon, manufacturer2)
model3 = Bicycle('C', wheel3, aluminum, manufacturer1)
model4 = Bicycle('D', wheel2, carbon, manufacturer3)
model5 = Bicycle('E', wheel1, steel, manufacturer3)
model6 = Bicycle('F', wheel3, steel, manufacturer1)

shop = Bike_shop('Dat', .20)
shop.inventory = [model1, model2, model3, model4, model5, model6]
#3.Print the name of each customer...
for i in list_cus:
    lst = i.afford_bike(shop)
    print("{} , Ban có thể mua loai: {}".format(i.name, [lst[j].name for j in range(len(lst))]))
#4Print the initial inventory of the bike shop for each bike it carries.
print ("                             ")
print ('Hàng hóa của {}'.format(shop.name))
shop.show_inventory()
#5Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.
print("                              ")
print("{} mua xe với: {} với giá {}, tài khoản còn lại {}".format(customer1.name, model1.mod_name,(0.2*model1.cost+model1.cost) , customer1.budget-((0.2*model1.cost+model1.cost))))
shop.inventory.remove(model1)
print("{} mua xe với: {} với giá {}, tài khoản còn lại {}".format(customer2.name, model6.mod_name,(0.2*model6.cost+model6.cost) , customer2.budget-((0.2*model6.cost+model6.cost))))
shop.inventory.remove(model6)
print("{} mua xe với: {} với giá {}, tài khoản còn lại {}".format(customer3.name, model3.mod_name,(0.2*model3.cost+model3.cost) , customer3.budget-((0.2*model3.cost+model3.cost))))
shop.inventory.remove(model3)
# 6print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.
print("                               ")
print("Xe còn lại là: {}:".format(shop.name))
shop.the_initial_inventory()
print ("Giá: {}".format(shop.profit))