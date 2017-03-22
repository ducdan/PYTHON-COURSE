# Bartender project
import random
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def order(question, ingredient):
    print "Please answer 'y' or 'n' to order!"

    for key, value in question.items():
        # Enter the taste
        print (value)
        ans = raw_input('Order: ')

        # Check for order
        time = 2
        while ((ans != 'y') & (ans != 'n') & (time > 0)):
            print "Please answer y or n to order!"
            print (value)
            ans = raw_input('Try again: ')
            time -= 1
        if (time == 0):
            print "Your order is invalid for 3 times."

         # Random the ingredients
        if (ans == 'y'):
            yield random.choice(ingredient[key])


result = order(questions, ingredients)
for i in result:
    print "   Service: ", i
print 'Thank you for order! :) '


