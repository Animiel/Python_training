import sys
import random
import os
import arcade

def guess_number():

    player_wins = 0
    total_games = 0

    print("\nWelcome to the 'Guess my number' game !")
    
    player_name = input("\nPlease enter your name for a custom game :\n")
    if player_name == "":
        player_name = "Player 1"
    
    def start_game():

        nonlocal player_wins
        nonlocal total_games

        computer = random.randint(1,10)
        player = input("\nPlease choose a number between 1 and 10 :\n")
        
        try:
            if int(player) >= 1 and int(player) <= 10:
                if computer == int(player):
                    total_games += 1
                    player_wins += 1
                    print(f"🎉 Bravo {player_name}, you won ! 🎉")
                else:
                    print(f"🥺 Sorry {player_name}, you lost... 🥺")
            else:
                print(f"\nSorry {player_name}, invalid input...")
                return start_game()
        except Exception as error:
            print("Please, put in a number between 1 and 10, but nothin else.")

        while True:
            replay = input("\nDo you want to replay ? Press Y for Yes or,\nRules to see the rules or,\nanything else to quit.\n")
            
            if replay.lower() == "y":
                return start_game()
            elif replay.lower() == "rules":
                print(f"\n👋 Hi {player_name} ! 👋\n📜 The rules are simple, guess the same number as the computer between 1 and 10. If you have the same, you win, if not you loose. Have fun ! 😊")
                continue
            else:
                print("❤️ Thanks for playing ! ❤️")
                print(f"🎲 You played {total_games} games. 🎲")
                print(f"💪 You won {player_wins} games. GG ! 💪")

                file = open("best_scores.txt")
                last_best = file.readline()
                file.close()

                if player_wins >= int(last_best[-2]):
                    file = open("best_scores.txt", "w")
                    file.write(f"'Guess my number' winning streak : {player_wins}\n")
                    file.write(f"'Guess my number' total games : {total_games}\n")
                    file.close()

                print(f"Bye {player_name} ! 👋")
                arcade.arcade()

                break
  
    try:
        os.path.isfile("best_scores.txt")
        stats = open("best_scores.txt")
        last_winning_streak = stats.readline()
        last_total_games = stats.readline()
        stats.close()
        print(f"📶 The last winning streak for this game is {last_winning_streak[-2]}.")
        print(f"📶 For a total of {last_total_games[-2]} games.")
    except Exception as e:
        raise e
    
    rules = input("\nDo you need the rules of the game ?\nPress Y for Yes or,\nanything else for No.\n")
    if rules.lower() == "y":
        print(f"\n👋 Hi {player_name} ! 👋\n📜 The rules are simple, guess the same number as the computer between 1 and 10. If you have the same, you win, if not you loose. Have fun ! 😊")
        start_game()
    else:
        return start_game()
    
    return guess_number

if __name__ == "__main__":
    guess = guess_number()
    guess()