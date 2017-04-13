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

def get_input():
    x = input("")
    while len(x) == 0:
        print("please input your answer")
        x = input("")
    return x 

def is_yes(user_answer=" "):
    if user_answer == "y" or "yes" in user_answer:
        return True
    else:
        return False 
    
def get_ingredients():
    output = []
    for taste in questions.keys():    
        print (questions[taste])
        answer = get_input()        
        if is_yes(answer):
            output.append(random.choice(ingredients[taste]))                
    return output

while True:
    print ("These ingredients match your choices: ", ', '.join(get_ingredients()), "\nThank you")
        