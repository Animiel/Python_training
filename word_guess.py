import arcade
import random

def word_guess():
    words = ["Incomprehensibilities", "Interdisciplinary", "Inconsequential", "Hypothetically", "Surreptitious", "Pharmaceutical", "History", "Music", "Animals", "Flowers", "Entertainment", "Colors", "Expectations", "Romance", "Vehicle", "Building", "Rhinoceros", "Firstname", "Understatement", "Complementary", "Garden", "Hollywood", "Underestimate", "Saturday", "Volcano", "Unbelievable", "Sadness", "Cherry blossom", "Hundred thousands", "Apocalyptic", "Bookshelf"]
    # words used only to test code, will be deleted when code works, replaced with words
    test_words = ["Horse", "Sheep"]

    print("\n✏️   Welcome to Word Guess game ! ✏️")

    def play_game():

        nonlocal words
        nonlocal test_words
        mistakes = 0
        x = 0
        letter_position = []

        # choosing a word from the list
        computer = random.choice(test_words)
        print(computer)
        # hiding the letters for the player
        mystery_word = "_" * len(computer.lower())

        while mistakes < 3:
            # showing player what it must find
            print(mystery_word)
            # asking player to choose a letter
            player_choice = input("\n✏️   Please choose a letter to try :\n")
            try:
                # verifying if player inserted only one character
                if len(player_choice) == 1:
                    # verifying if the player choice is in the word
                    if player_choice.lower() in computer.lower():
                        computer = list(computer.lower())
                        print(computer)
                        mystery_word = list(mystery_word)
                        print(mystery_word)
                        while x < len(computer):
                            if computer[x] == player_choice.lower():
                                letter_position.append(x)
                            x += 1
                        for x in letter_position:
                            mystery_word[x] = player_choice.lower()
                        letter_position.clear()
                        computer = str(computer)
                        mystery_word = str(mystery_word)
                    # if the letter is not in the word adds a mistake
                    elif player_choice.lower() not in computer.lower():
                        mistakes += 1
                        print("\n🥺  Oh no, that's not in the word...\n👍  Guess again !")
                # if player inserts more characters, returning a message
                else:
                    print("❌  Please input ONE LETTER between A and Z. Numbers or special characters are not allowed. Thank you.")
            # everything else will return this message
            except Exception:
                print("❌  Please input ONE LETTER between A and Z. Numbers or special characters are not allowed. Thank you.")
        # prints a winning message if the word is found
        # code doesn't get here yet either
        else:
            print(f"\n🎉  Congratulations ! You won ! The word you guessed was : {computer} 🎉")
    


    # asking player if he needs the rules of the game => what the end result of this code should do
    rules = input("\nDo you need the rules ?\nPress Y for Yes,\nAnything else for No :\n")
    if rules.lower() == "y":
        print("\n📜 Here are the rules of the game :\n📜 The computer chooses a random word (actually there are only 31 available), each underscore stands for a letter. You need to input one letter at a time to slowly reveal the word.\n📜 Each letter will be revealed as many times as itexists inside the words (if there are 3 Ns, all three will appear).\n📜 You can make 3 mistakes, after that it's game over for you !\n📜 Good luck !")
        play_game()
    # if rules not needed, launching game
    else:
        play_game()



word_guess()