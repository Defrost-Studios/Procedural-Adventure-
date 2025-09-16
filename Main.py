from CharacterCreation import Character_create
from QuestLineGenerator import STARTQuest
from TBC import TBC

def main():
    print("---Welcome, lone soul, to the world of Precedural!---")
    player = Character_create()
    game = True

    while game == True:
        print("\n What would you like to do? \n 1. Start a quest \n 2. View Character Stats \n 3. Exit Game")
        choice = input("->")
        if choice == "1":
            quest_details = STARTQuest(player)
            TBC(player, quest_details["enemy"])
        elif choice == "2":
            print(f"\n Character Stats: \n Name: {player['name']} \n Class: {player['class']} \n Strength: {player['Strength']} \n Defense: {player['Defense']} \n Intelligence: {player['Intelligence']} \n Luck: {player['Luck']} \n HP: {player['hp']} \n Ball Knowledge: {player['ball knowledge']}")

        elif choice == "3":
            print("So your weak..Well then..")
            break
        else:
            print("Invalid choice, please try again.")
            
        if player.get("hp") <= 0:
            game = False
            break


if __name__ == "__main__":
    main()



   