from customer import Customer
from bicycle import Bicycle, Wheel, Frame 
from shop import Shop
from collections import OrderedDict

wheel1 = Wheel("aluminum", 1, 10)
wheel2 = Wheel("carbon", 2, 15)
wheel3 = Wheel("steel", 3, 20)
frame1 = Frame("EU", 1, 10)
frame2 = Frame("AU", 2, 40)
bike1 = Bicycle("VN1", frame = frame1, wheel = wheel1)   
bike2 = Bicycle("VN2", frame = frame1, wheel = wheel2)
bike3 =Bicycle("CN1", frame = frame1, wheel = wheel3)
bike4 =Bicycle("CN2", frame = frame2, wheel = wheel1)
bike5 =Bicycle("US1", frame = frame2, wheel = wheel2)
bike6 =Bicycle("US2", frame = frame2, wheel = wheel3) 
inventory = OrderedDict()
inventory[bike1] = 6
inventory[bike2] = 5
inventory[bike3] = 3
inventory[bike4] = 3
shop1 = Shop(sname = "Saigon", inventory = inventory, margin = 0.2)
shop1.add(bike3)
shop1.add({bike5: 2, bike6: 1})
pp1 = Customer("Khoe", 200)
pp2 = Customer("Tri", 500)
pp3 = Customer("Hung", 1000)

print(pp1.cname, "can buy", pp1.canbuy(shop1)) 
print(pp2.cname, "can buy", pp2.canbuy(shop1)) 
print(pp3.cname, "can buy", pp3.canbuy(shop1) )
shop1._show_inventory()
pp1.buy(shop1, bike1)
shop1.sell(bike1)
pp2.buy(shop1, bike2)
shop1.sell(bike2)
pp3.buy(shop1, bike3)
shop1.sell(bike3)


