from bicycle import Bicycle
from collections import OrderedDict

class Shop(object):
    def __init__(self, sname = "", inventory = OrderedDict(), margin = 0):
        self.sname = sname
        self.inventory = inventory
        self.margin = margin
        self.sold = OrderedDict()
        self.profit = 0
            
    def add(self, bikes):
        if isinstance(bikes, dict):
            for (bike, count) in bikes.items():
                if bike not in self.inventory.keys():
                    self.inventory.update({bike:count}) 
                else:
                    self.inventory[bike] += count 
        if isinstance(bikes, Bicycle):
            if bikes in self.inventory.keys():
                self.inventory[bikes] += 1
            else:
                self.inventory.update({bikes:1})
        return self._show_inventory()            
    def sell(self,bikes):
        if isinstance(bikes, Bicycle):
            if bikes in self.inventory.keys():
                if self.inventory[bikes] > 0:
                    self.inventory[bikes] -= 1
                    self.sold.update({bikes: 1})
                else:
                    print("sold-out")    
            else:
                print("no product in stock")    
        if isinstance(bikes, dict):
            for (bike,count) in bike.items():
                if bike in self.inventory.keys():
                    if self.inventory[bike] > count:
                        self.inventory[bike] -= count
                        print ("selling %d bike", self.inventory[bike])
                        self.sold.update({bike:count})
                    else:
                        print("sold-out")    
                else:
                    print("no product in stock")
        for (bike, count) in self.sold.items():
            self.profit += bike.cost*self.margin*count
        return (self._show_inventory(), self._show_sold(), self._show_profit())
               
    def get_prices(self):
        prices = OrderedDict()
        for bike in self.inventory.keys():
            prices.update({bike.mname:bike.cost*(1+self.margin)})
        return prices
     
    def _show_inventory(self):
        print ("Inventory:")
        for (k,v) in self.inventory.items():
            print ("%s\t%d" %(k.mname, v))  

    def _show_sold(self):
        print ("Sold bikes:")
        for (k,v) in self.sold.items():
            print ("%s\t%d" %(k.mname, v))
                   
    def _show_profit(self):
        print ("Profit:\n", self.profit)





       