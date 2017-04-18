import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?", }

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"], }

def order(question, ingredient):
    print('Hi! Would you like something to drink?')

    for key, ques in question.items():
        print ("For example: {}".format(ques))
        ans = input("Press 'y - Y' or 'n - N' to answer: ")

        while ((ans != 'y') & (ans != 'Y') & (ans != 'n') &(ans !='N')):
            ans = input('Please try again: ')

        if (ans == 'y') or (ans == 'Y'):
            yield random.choice(ingredient[key])

result = order(questions, ingredients)
for x in result:
    print (">>> Enjoy your {}. Cheers!!!".format(x))
print ("Here’s to our success!!!")