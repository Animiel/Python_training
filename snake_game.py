import arcade
import random

def snake_game():

    game_board = [
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""]
    ]
    black_square = {
        "position": [random.randint(0, 3), random.randint(0, 4)],
        "has_key": False
    }
    finish_key = {
        "position": [random.randint(0, 3), random.randint(0, 4)]
    }
    finish_line = {
        "position": [random.randint(0, 3), random.randint(0, 4)]
    }
    print(black_square["position"])
    print(finish_key["position"])
    print(finish_line["position"])

    print("\n🎲  Welcome to a small Snake-like game ! 🎲")

    def play_game():
        
        nonlocal game_board
        nonlocal black_square
        nonlocal finish_key
        nonlocal finish_line
        x = 0
        y = 0
        bs_row = black_square["position"][0]
        bs_col = black_square["position"][1]
        fk_row = finish_key["position"][0]
        fk_col = finish_key["position"][1]
        fl_row = finish_line["position"][0]
        fl_col = finish_line["position"][1]

        game_board[bs_row][bs_col] = " ◼️  "
        game_board[fk_row][fk_col] = " 🗝️  "
        game_board[fl_row][fl_col] = " 🏁  "

        for lists in game_board:
            for element in lists:
                if element == "":
                    element = " ◻️  "
                    game_board[x][y] = element
                y += 1
            y = 0
            x += 1
        
        print(game_board)
                
    



    # asking player if it needs the rules
    rules = input("\nDo you need the rules of the game ?\nPress Y for Yes or,\nanything else for No.\n")
    # if yes, print them and then start the game
    if rules.lower() == "y":
        print("\n📜  The rules are simple,\n📜  Your position is shown by a black square ◼️  ,\n📜  There is a key 🗝️   on the grid, you need it to finish the game, so you have to collect it,\n📜  Once in possession of the key, run to the finish line 🏁  !")
        play_game()
    # if not, just start the game
    else:
        return play_game()

    return snake_game

# if __name__ == "__main__":
snake_game()