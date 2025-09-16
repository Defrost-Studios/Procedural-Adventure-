import random

def Character_create():
    Name = input("enter your Name:")
    print("---Choose class--- \n" \
    "1. Warrior \n" \
    "2. Mage \n" \
    "3. Rogue \n" \
    "4. Wretch \n")
    userchoice = input("->")
    classes_list = {"1": "Warrior", "2": "Mage", "3": "Rogue", "4": "wretch"}
    Choice = classes_list.get(userchoice, "wretch")
    BaseStates = {"Warrior": (10, 7, 5, 3),
                  "Mage": (5, 6, 10, 4),
                  "Rogue": (6, 4, 7, 8),
                  "wretch": (5, 3, 7, 8)}
    Strength, Defense, Intelligence, Luck = BaseStates[Choice]

    player = {
        "name": Name,
        "class": Choice,
        "Strength": Strength,
        "Defense": Defense,
        "Intelligence": Intelligence,
        "Luck": Luck,
        "hp": 100,
        "ball knowledge": 0
    }
    print(f"Character Created! Welcome {Name}, to The world of Precedural!")
    return player