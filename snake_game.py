import arcade
import random

def snake_game():

    # initializing game grid
    game_board = [
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""]
    ]
    # initializing player position
    black_square = {
        "position": [random.randint(0, 3), random.randint(0, 4)],
        "has_key": False
    }
    # initializing exit key position
    finish_key = {
        "position": [random.randint(0, 3), random.randint(0, 4)]
    }
    # initializing finish line position
    finish_line = {
        "position": [random.randint(0, 3), random.randint(0, 4)]
    }

    print("\n🎲  Welcome to a small Snake-like game ! 🎲")

    def play_game():
        
        nonlocal game_board
        nonlocal black_square
        nonlocal finish_key
        nonlocal finish_line
        x = 0
        y = 0
        # getting the single position of special cells
        bs_row = black_square["position"][0]
        bs_col = black_square["position"][1]
        fk_row = finish_key["position"][0]
        fk_col = finish_key["position"][1]
        fl_row = finish_line["position"][0]
        fl_col = finish_line["position"][1]

        # filling the rest of the grid function
        def filling_grid():
            nonlocal x
            nonlocal y

            # positionning special cells first in the game grid
            game_board[bs_row][bs_col] = "◼️  "
            game_board[fk_row][fk_col] = "🗝️  "
            game_board[fl_row][fl_col] = "🏁  "

            # filling the rest of the grid with blank cells
            # for each line
            for lists in game_board:
                # fill all the elements inside the row
                for element in lists:
                    # only if the position is empty
                    if element == "":
                        element = "◻️  "
                        game_board[x][y] = element
                    # getting to the next element in the row
                    y += 1
                # print that row
                print(game_board[x])
                # reinitializing the column number
                y = 0
                # getting to the next row
                x += 1
        
        # moving around the grid function
        def moving_in_grid():
            nonlocal bs_col
            nonlocal bs_row
            nonlocal fk_col
            nonlocal fk_row
            nonlocal fl_col
            nonlocal fl_row
            nonlocal x
            nonlocal y

            x = 0
            y = 0

            # asking the direction to move on to the player
            player = input("\nWhere do you want to move ?\nR for ➡️   RIGHT ➡️  ,\nL for ⬅️   LEFT ⬅️  ,\nU for ⬆️   UP ⬆️  ,\nD for ⬇️   DOWN ⬇️\n")

            # depending on the direction chosen, move that way
            if player.lower() == "r":
                # filling the previous position of player with a blank cell
                game_board[bs_row][bs_col] = "◻️  "
                # adding one to the column position of the player
                bs_col += 1
                # if position reaches out of range, placing the player to the beginning of the row
                if bs_col > 4:
                    bs_col = 0
                # if player gets on the exit key cell (could have made the condition that way too : if game_board[bs_row][bs_col] == game_board[fk_row][fk_col])
                if bs_col == fk_col and bs_row == fk_row:
                    # replacing the key cell by player cell
                    game_board[fk_row][fk_col] = "◼️  "
                    # player gets the key in "inventory"
                    black_square["has_key"] = True
                    # showing the updated rows
                    # couldn't use filling_grid() as it would place the key cell again, it's not really a problem for the code right now, but visually it has no sense
                    for lists in game_board:
                        print(lists)
                else:
                    # else showing the grid after the changes
                    filling_grid()
                # continue moving around the grid
                moving_in_grid()
            # same mechanics as above but adapted to the movements
            elif player.lower() == "l":
                game_board[bs_row][bs_col] = "◻️  "
                bs_col -= 1
                if bs_col < 0:
                    bs_col = 4
                if bs_col == fk_col and bs_row == fk_row:
                    game_board[fk_row][fk_col] = "◼️  "
                    black_square["has_key"] = True
                    for lists in game_board:
                        print(lists)
                else:
                    filling_grid()
                moving_in_grid()
            elif player.lower() == "u":
                game_board[bs_row][bs_col] = "◻️  "
                bs_row -= 1
                if bs_row < 0:
                    bs_row = 3
                if bs_col == fk_col and bs_row == fk_row:
                    game_board[fk_row][fk_col] = "◼️  "
                    black_square["has_key"] = True
                    for lists in game_board:
                        print(lists)
                else:
                    filling_grid()
                moving_in_grid()
            elif player.lower() == "d":
                game_board[bs_row][bs_col] = "◻️  "
                bs_row += 1
                if bs_row > 3:
                    bs_row = 0
                if bs_col == fk_col and bs_row == fk_row:
                    game_board[fk_row][fk_col] = "◼️  "
                    black_square["has_key"] = True
                    for lists in game_board:
                        print(lists)
                else:
                    filling_grid()
                moving_in_grid()
            # if wrong direction input, rebooting the choice
            else:
                print("\n❌  Please input a valid letter. ❌")
                moving_in_grid()
        
        # calling the functions created above to play the game
        filling_grid()
        moving_in_grid()
                
    



    # asking player if it needs the rules
    rules = input("\nDo you need the rules of the game ?\nPress Y for Yes or,\nanything else for No.\n")
    # if yes, print them and then start the game
    if rules.lower() == "y":
        print("\n📜  The rules are simple,\n📜  Your position is shown by a black square ◼️  ,\n📜  There is a key 🗝️   on the grid, you need it to finish the game, so you have to collect it,\n📜  Once in possession of the key, run to the finish line 🏁  !\n")
        play_game()
    # if not, just start the game
    else:
        return play_game()

    return snake_game

# if __name__ == "__main__":
snake_game()