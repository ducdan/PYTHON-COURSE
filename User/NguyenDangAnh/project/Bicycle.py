import random
class Bicycle():
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = cost
        self.cost = cost
class Shop():
    def __init__(self, name, cost_bicycle):
        self.name = name
        self.cost_bicycle = cost_bicycle
        self.profit = 0
        self.inventory = []
    def inventory_store(self):
        for x in self.inventory:
            print('ten:{},{}(kg),{}$'.format(x.name,x.weight,x.cost))

class Customers():
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund


bicycle0=Bicycle('bicycle0', 18 ,50)
bicycle1=Bicycle('bicycle1', 12 ,100)
bicycle2=Bicycle('bicycle2', 14 ,200)
bicycle3=Bicycle('bicycle3', 15 ,400)
bicycle4=Bicycle('bicycle4', 16 ,800)
bicycle5=Bicycle('bicycle5', 17 ,1000)

store = Shop('Anh-store', 0.2)
store.inventory=[bicycle0,bicycle1,bicycle2,bicycle3,bicycle4,bicycle5]
print('--Danh sách sản phẩm--')
store.inventory_store()

customer0=Customers('anh', 200)
customer1=Customers('em', 500)
customer2=Customers('y3u', 1000)
cus = [customer0,customer1,customer2]


for i in cus:
    print('{} co the mua:'.format(i.name))
    for y in store.inventory:
        if i.fund >= y.cost:
            print('-{}'.format(y.name))
