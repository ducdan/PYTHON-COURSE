# ----------------------------------------
#    Bicycle Project
# ----------------------------------------
from Bicycle_class import *
# ----------------------------------------
""" Create a bicycle shop that has 6 different bicycle models in stock. The
shop should charge its customers 20% over the cost of the bikes. """
# ----------------------------------------
model_1 = Bicycle("Road_racing", 8, 100)
model_2 = Bicycle("Sportive", 7, 200)
model_3 = Bicycle("Hybrid", 6, 300)
model_4 = Bicycle("Track", 5, 500)
model_5 = Bicycle("Folding", 9, 1200)
model_6 = Bicycle("BMX", 3, 700)
# ----------------------------------------
ABC_shop = Bike_shop("ABC", model_1, model_2, model_3,
                            model_4, model_5, model_6)
# ----------------------------------------
""" Create three customers. One customer has a budget of $200, the second
$500, and the third $1000 """
# ----------------------------------------
customer_1 = Customer("An", 200)
customer_2 = Customer("Ly", 500)
customer_3 = Customer("Nam", 1000)
# ----------------------------------------
""" Print the name of each customer, and a list of the bikes offered by the
bike shop that they can afford given their budget. Make sure you price
the bikes in such a way that each customer can afford at least one """
# ----------------------------------------
customers = [customer_1, customer_2, customer_3]
print("1.")
for customer in customers:
    print("Models are appropiate for {}".format(customer.name))
    for model in ABC_shop.stock:
        if customer.budget >= model.cost:
            print("_{}".format(model.name))
    print("*********************************")
# ----------------------------------------
"""Print the initial inventory of the bike shop for each bike it carries."""
# ----------------------------------------
print("2.")
print("ABC_shop have models in stock: ")
ABC_shop.inventory_stock()
print("*********************************")
# ----------------------------------------
""" Have each of the three customers purchase a bike then print the name of
the bike the customer purchased, the cost, and how much money they
have left over in their bicycle fund."""
# ----------------------------------------
print("3. ")
customer_1.buy_bike(model_1)
ABC_shop.export_bike(model_1)
print("{} have bought {} with price {}, the money left is {}"
      .format(customer_1.name, model_1.name, 1.2 * model_1.cost, customer_1.budget))

customer_2.buy_bike(model_3)
ABC_shop.export_bike(model_3)
print("{} have bought {} with price {}, the money left is {}"
      .format(customer_2.name, model_3.name, 1.2 * model_3.cost, customer_2.budget))

customer_3.buy_bike(model_6)
ABC_shop.export_bike(model_6)
print("{} have bought {} with price {}, the money left is {}"
      .format(customer_3.name, model_6.name, 1.2 * model_6.cost, customer_3.budget))

print("*********************************")
# ----------------------------------------
""" After each customer has purchased their bike, the script should print out
the bicycle shop's remaining inventory for each bike, and how much
profit they have made selling the three bikes """
# ----------------------------------------
print("4. ")
print("Models of ABC_shop left : ")
ABC_shop.inventory_stock()
print("*********************************")
# ----------------------------------------
print("5. ")
print("The profit of shop after bought three models")
print(ABC_shop.profit)








