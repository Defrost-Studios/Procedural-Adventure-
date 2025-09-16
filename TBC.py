import random
import time

moveset_mage = {"1": "Fireball", "2": "Holy arrows", "3": "Ultimate Powerball winning numbers"}
moveset_warrior = {"1": "Swordslash", "2": "Mighty Push", "3": "Ultimate drip tactic"}
moveset_rogue = {"1": "RapidStab", "2": "Fingerpistol", "3": "GUM-GUM-ROCKETTT"}
moveset_wretch = {"1": "punch", "2": "kick", "3": "beg"}

def TBC(player, enemy):
    enemy_HP = 50
    if enemy == "awakened Knight" or "Empty Vessel" or "The Destroyer":
        enemy_HP = 200
    print(f"\n Let the Battle Begin against {enemy}!")
    while player["hp"] > 0 and enemy_HP > 0:
        print(f"choose action: \n 1. Attack \n 2. use item \n 3. Run \n 4. Defend")
        action = input("->")
        dmg = 0
        beg = [0, 100]
        if action == "1":
            if player["class"] == "Mage":
                attacktype = input(f"choose attack(ability[dmg](self inflicted dmg)) \n 1. Fireball[15] \n 2. Holy arrows[30] \n 3. Ultimate Powerball winning numbers[100](-15) \n ->")
                attacktype = moveset_mage.get(attacktype, "Fireball")
                if attacktype == "Fireball":
                    enemy_HP -= 15
                elif attacktype == "Holy arrows":
                    enemy_HP -= 30
                else:
                    enemy_HP -= 100
                    player["hp"] -= 15
                if enemy_HP < 0:
                    enemy_HP = 0
                print(f"You Used {attacktype}!")
            if player["class"] == "Warrior":
                attacktype = input(f"choose attack(ability[dmg](self inflicted dmg)) \n 1. Swordslash[10] \n 2. Mighty Push[25] \n 3. Ultimate drip tactic[100](CHANCE = -100) \n ->")
                attacktype = moveset_warrior.get(attacktype, "Swordslash")
                if attacktype == "Swordslash":
                    enemy_HP -= 10
                elif attacktype == "Mighty Push":
                    enemy_HP -= 25
                else:
                    enemy_HP -= 100
                    player["hp"] -= random.choice(beg)
                if enemy_HP < 0:
                    enemy_HP = 0
                print(f"You Used {attacktype}!")
            if player["class"] == "Rogue":
                attacktype = input(f"choose attack(ability[dmg](self inflicted dmg)) \n 1. RapidStab[12] \n 2. Fingerpistol[40] \n 3. GUM-GUM-ROCKETTT[100](+10 ball knowledge) \n ->")
                attacktype = moveset_rogue.get(attacktype, "RapidStab")
                print(f"You Used {attacktype}!")
                if attacktype == "RapidStab":
                    enemy_HP -= 12
                elif attacktype == "Fingerpistol":
                    enemy_HP -= 40
                else:
                    enemy_HP -= 100
                    player["ball knowledge"] += 10
                if enemy_HP < 0:
                    enemy_HP = 0
            if player["class"] == "wretch":
                attacktype = input(f"choose attack(ability[dmg](self inflicted dmg)) \n 1. punch[5] \n 2. kick[10] \n 3. beg[0](chance to escape or die) \n ->")
                attacktype = moveset_wretch.get(attacktype, "punch")
                print(f"You Used {attacktype}!")
                if attacktype == "punch":
                    enemy_HP -= 5
                elif attacktype == "kick":
                    enemy_HP -= 10
                else:
                    enemy_HP -= 0
                    player["hp"] -= random.choice(beg)
                    if player["hp"] <= 0:
                        print("You died while begging..")
                        return
                    else:
                        print("You successfully escaped while begging!")
                        return
                if enemy_HP < 0:
                    enemy_HP = 0
            print(f"{enemy} has {enemy_HP} HP left!")
            
        elif action == "2":
            print("You have no items..")
            continue
        elif action == "3":
            if enemy in ["awakened Knight", "Empty Vessel", "The Destroyer"]:
                print("You can't run from a boss!")
            else:
                print("You successfully fled!")
                return
                
        elif action == "4":
            print("you dont know how to defend yet..")
            continue

        time.sleep(1)

        if player["hp"] > 0 and enemy_HP > 0:
            enemy_attack = random.choice(["light attack", "heavy attack", "special attack"])
            if enemy_attack == "light attack":
                dmg = 10
                if enemy == "awakened Knight" or "Empty Vessel" or "The Destroyer":
                    dmg = 20
            elif enemy_attack == "heavy attack":
                dmg = 20
                if enemy == "awakened Knight" or "Empty Vessel" or "The Destroyer":
                    dmg = 40
            else:
                dmg = 30
                if enemy == "awakened Knight" or "Empty Vessel" or "The Destroyer":
                    dmg = 60
            player["hp"] -= dmg
            print(f"{enemy} used {enemy_attack}! It dealt {dmg} damage. You have {player['hp']} HP left!")

    if player["hp"] <= 0:
        print(f"You have been defeated.. as expected of a {player['class']}..")
        return
    else:
        print(f"You have defeated the {enemy}!")
