from shop import Shop
from bicycle import Bicycle
class Customer(object):
    def __init__(self, cname, fund):
        self.cname = cname
        self.fund = fund

    def budget_left(self,price):
        return self.fund - price
    def canbuy(self, ashop = Shop()):
        canbuy = []
        for (k,v) in ashop.get_prices().items():
            if self.fund > v:
                canbuy.append(k)
        return canbuy
    def buy(self, ashop = Shop(), bike = Bicycle):
        if bike.mname in self.canbuy(ashop):
            self.fund -= ashop.get_prices()[bike.mname]
            print ("%s buy %s bike at %s, and have $%d remaining." %(self.cname, bike.mname, ashop.sname, self.fund))
        else:
            print("too expensive to buy")