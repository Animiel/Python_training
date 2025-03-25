import sys
import random
import os
import arcade

def guess_number():

    player_wins = 0
    total_games = 0

    print("\nWelcome to the 'Guess my number' game !")
    
    # asking player for its username
    player_name = input("\nPlease enter your name for a custom game :\n")
    # adding a default value if player doesn't input anything
    if player_name == "":
        player_name = "Player 1"
    
    def start_game():

        nonlocal player_wins
        nonlocal total_games

        # picking a number between 1 and 10
        computer = random.randint(1,10)
        # asking player for its choice
        player = input("\nPlease choose a number between 1 and 10 :\n")
        
        try:
            # checking if player choice is in the good range
            if int(player) >= 1 and int(player) <= 10:
                # if it's the same number adds 1 to the number of games played and to the player's wins
                if computer == int(player):
                    total_games += 1
                    player_wins += 1
                    print(f"🎉 Bravo {player_name}, you won ! 🎉")
                # if not the same number, mentionning it to player and adding 1 to the total of games played
                else:
                    total_games += 1
                    print(f"🥺 Sorry {player_name}, you lost... 🥺")
            # if player choice not in range, just restart game without counting game
            else:
                print(f"\nSorry {player_name}, invalid input...")
                return start_game()
        # if player inserts anything else, remembering him to put a number in
        except Exception as error:
            print("Please, put in a number between 1 and 10, but nothin else.")

        # asking if player wants to replay the game
        while True:
            replay = input("\nDo you want to replay ? Press Y for Yes or,\nRules to see the rules or,\nanything else to quit.\n")
            
            # if player wants to replay, restart the game
            if replay.lower() == "y":
                return start_game()
            # if he needs the rules, show them
            elif replay.lower() == "rules":
                print(f"\n👋 Hi {player_name} ! 👋\n📜 The rules are simple, guess the same number as the computer between 1 and 10. If you have the same, you win, if not you loose. Have fun ! 😊")
                continue
            # if not, game ends, showing some stats to player
            else:
                print("❤️ Thanks for playing ! ❤️")
                print(f"🎲 You played {total_games} games. 🎲")
                print(f"💪 You won {player_wins} games. GG ! 💪")

                # restoring the last score for this game
                file = open("best_scores.txt")
                last_best = file.readline()
                file.close()

                # storing the score if the actual won games are greater than the stored one
                # getting the number from the line in the file and comparing it to the actual wins 
                if player_wins >= int(last_best[-2]):
                    file = open("best_scores.txt", "w")
                    # if true, overwriting the file's data
                    file.write(f"'Guess my number' winning streak : {player_wins}\n")
                    file.write(f"'Guess my number' total games : {total_games}\n")
                    file.close()

                # finally quitting the game
                # previously print() was sys.exit(), but since the game is part of the arcade...
                print(f"Bye {player_name} ! 👋")
                # ...returning to the arcade menu
                arcade.arcade()

                break
    
    # printing the last best score to the player
    try:
        # checking if the file exists
        os.path.isfile("best_scores.txt")
        stats = open("best_scores.txt")
        # getting the stats
        last_winning_streak = stats.readline()
        last_total_games = stats.readline()
        stats.close()
        # printing the stored stats
        print(f"📶 The last winning streak for this game is {last_winning_streak[-2]}.")
        print(f"📶 For a total of {last_total_games[-2]} games.")
    # if anything is wrong, raise an error, but since the file exists, should not happen
    except Exception as e:
        raise e
    
    # asking player if it needs the rules
    rules = input("\nDo you need the rules of the game ?\nPress Y for Yes or,\nanything else for No.\n")
    # if yes, print them and then start the game
    if rules.lower() == "y":
        print(f"\n👋 Hi {player_name} ! 👋\n📜 The rules are simple, guess the same number as the computer between 1 and 10. If you have the same, you win, if not you loose. Have fun ! 😊")
        start_game()
    # if not, just start the game
    else:
        return start_game()
    
    return guess_number

if __name__ == "__main__":
    guess = guess_number()
    guess()