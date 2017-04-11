class Shop:
    def __init__(self):
        self.inc_rate=0.2
        self.p
        pass
    def setInventory(self,Blist):
        self.__inventory=Blist
        #*0.2
    def getInventory(self):
        return self.__inventory
    def getoffer(self,money):
        # xu ly duyet so tien
        #money=200
        lstoffer=[]
        for bi in self.__inventory:
            if(bi.cost<=money):
                money=money-bi.cost
                lstoffer.append(bi)
        return lstoffer
    def printInventory(self):
        for x in self.__inventory:
            print(x.name)
    def ban(self,bi):
        self.__inventory.remove(bi)
        print(bi.name)
        print(bi.cost)
        self.profit+=bi.cost


class Bicycle:
    def __init__(self,name,cost,frame,wheel,manuf):
        self.name =name
        self.cost=cost

class Customer:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    def mua(self,bi):
        self.bicycle=bi
        self.money=self.money-bi.cost

    if __name__ == '__main__':
        def getBi(self):
            return self.bicycle
        #..

def mua(customer,shop):
    offer=shop.getoffer(customer.money)#1st
    customer.mua



cus1=Customer('A',200)
cus2=Customer('A',200)
cus3=Customer('A',200)

print(cus1.name)
shop=shop().inventory

lstname = ['mau do', '  ']
lstcost = ['1000', '  ']
lstbi={}
for i in range(6):
    lstbi.append(Bicycle(lstname[i],lstcost[i]+lstcost*0.2))
shop.setinventory(lstbi)


class wheel:
    def __init__(self,weight,cost):
        self.cost=cost
        self.weight=weight

    pass
class frame
    pass

class manuf:
    def __init__(self):