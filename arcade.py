from enum import Enum
import guess_number
import word_guess

def arcade():

    class Games(Enum):
        Guess_my_number = 1
        Word_Guess = 2
        Test2 = 3

    # making a enumerated list of the games availbale
    games = list(Games)

    print("\n🎲  Welcome to the Arcade ! 🎲\n")
    print("Here is our list of available games :\n")
    # the list not being fixed, looping through it to show the games available, as I might add several more games for fun to it in future, else we could use some simple printing if there was a fixed number of games
    for game in games:
        print(f"{game.value}. {str(game).replace("Games.", "").replace("_", " ")}")

    def select_game():

        nonlocal games

        # asking player for the game it wants to play
        player_choice = input("\nPlease choose the game you want to play, by typing it's number :\n")
        try:
            # actually only one game available, so if picking it, launches the game
            if int(player_choice) == 1:
                guess_number.guess_number()
            elif int(player_choice) == 2:
                word_guess.word_guess()
        # if input is anything else, asking player to choose between the games available
        except Exception:
            print(f"Please choose a number between {games[0].value} and {len(games)}")
        
    select_game()
    
    return arcade

if __name__ == "__main__":
    arcade()