from enum import Enum
import guess_number

def arcade():

    class Games(Enum):
        Guess_my_number = 1
        Test1 = 2
        Test2 = 3

    games = list(Games)

    print("\n🎲  Welcome to the Arcade ! 🎲\n")
    print("Here is our list of available games :\n")
    for game in games:
        print(f"{game.value}. {str(game).replace("Games.", "").replace("_", " ")}")

    def select_game():

        nonlocal games

        player_choice = input("\nPlease choose the game you want to play, by typing it's number :\n")
        try:
            if int(player_choice) == 1:
                guess_number.guess_number()
        except Exception:
            print(f"Please choose a number between {games[0].value} and {len(games)}")
        
    select_game()
    
    return arcade

arcade()