# ---------------------------------------------------------------------------------------
import random
# ---------------------------------------------------------------------------------------
# recommending choices for customer
questions = {"strong": "Do ye like yer drinks strong?",
             "salty": "Do ye like it with a salty tang?",
             "bitter": "Are ye a lubber who likes it bitter?",
             "sweet": "Would ye like a bit of sweetness with yer poison?",
             "fruity": "Are ye one for a fruity finish?",}

# recommending appropriate ingredient with the taste
ingredients = {"strong": ["glug of rum", "slug of whisky", "splash of gin"],
               "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
               "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
               "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
               "fruity": ["slice of orange", "dash of cassis", "cherry on top"],}
# ---------------------------------------------------------------------------------------
def favourite_taste(questions):
    """ Print questions and return the favourite taste"""
    while True:
        for taste, question in questions.items():    # show questions one by one
            print(question)                          # print recommendation
            chosen_taste = input("Please press 'y' or 'Y' if you like it :)': ") # get answer from customer
            if chosen_taste == 'y' or chosen_taste == 'Y':
                return taste
            else:                                    # press any buttons except Y or y then do thing
                pass
        print("Maybe, another round :)'")            # repeat the questions list
# ---------------------------------------------------------------------------------------
def bartender(taste, ingredients):
    """ Choice ingredient randomly based on the taste"""
    print("Maybe you like a little of:  ")
    return ingredients[taste][random.randint(0,2)] # random value from list ingredients with "key" of taste
# ---------------------------------------------------------------------------------------
print(bartender(favourite_taste(questions), ingredients))  # print random ingredient




