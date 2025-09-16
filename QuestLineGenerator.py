import random

locations = ["Underground Caverns", "Deep Docks", "Blue lake", "Sky Islands", "Crimson Lands"]
questType = ["Enemy", "Puzzle Challenge", "Rescue mission", "treasure chest"]
enemies = ["Javalin Spiders", "Hallowed Knight", "King Slime", "mellodious Skeleton"]
BossEnemies = ["awakened Knight", "Empty Vessel", "The Destroyer"]
ran = ["Enemy", "BOSS"]
def STARTQuest(player):
    location = random.choice(locations)
    quest = random.choice(questType)
    types = random.choice(ran)
    print(f"\n You travel to The {location} in search for a(n) {quest}!")
    if types == "BOSS":
        enemy = random.choice(BossEnemies) 
    else:
        enemy = random.choice(enemies)
    if types == "Enemy":
        print(f"A {enemy} appears before you!")
    elif quest == "Puzzle Challenge":
        print(f"You found A puzzle! but you can't solve it unfortunately..")
        print(f"but you encountered a {enemy}!")
    elif types == "BOSS":
        print(f"You encounter a wild {enemy}!")
    return {"location": location, "quest_type": quest, "enemy": enemy}