import sys
import random

def guess_number():

    print("\nWelcome to the 'Guess my number' game !")
    
    player_name = input("\nPlease enter your name for a custom game :\n")
    if player_name == "":
        player_name = "Player 1"
    
    def start_game():

        computer = random.randint(1,10)
        player = input("\nPlease choose a number between 1 and 10 :\n")
        
        if int(player) >= 1 and int(player) <= 10:
            if computer == int(player):
                print(f"🎉 Bravo {player_name}, you won ! 🎉")
            else:
                print(f"🥺 Sorry {player_name}, you lost... 🥺")
        else:
            print(f"\nSorry {player_name}, invalid input...")
            return start_game()

        while True:
            replay = input("\nDo you want to replay ? Press Y for Yes or,\nRules to see the rules or,\nanything else to quit.\n")
            
            if replay.lower() == "y":
                return start_game()
            elif replay.lower() == "rules":
                print(f"\n👋 Hi {player_name} ! 👋\n📜 The rules are simple, guess the same number as the computer between 1 and 10. If you have the same, you win, if not you loose. Have fun ! 😊")
                continue
            else:
                print("❤️ Thanks for playing ! ❤️")
                sys.exit(f"Bye {player_name} ! 👋")
                break
    
    rules = input("\nDo you need the rules of the game ?\nPress Y for Yes or,\nanything else for No.\n")
    if rules.lower() == "y":
        print(f"\n👋 Hi {player_name} ! 👋\n📜 The rules are simple, guess the same number as the computer between 1 and 10. If you have the same, you win, if not you loose. Have fun ! 😊")
        start_game()
    else:
        return start_game()
        
    return guess_number

# if __name__ == "__main__":
guess_number()