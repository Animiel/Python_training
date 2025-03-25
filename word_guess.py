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

        # choosing a word from the list
        computer = random.choice(test_words)
        print(computer)
        # hiding the letters for the player
        mystery_word = "_" * len(computer)

        # Actually while doesn't work -> code doesn't stop when no _ are in mystery_word or mistakes are over >= 3
        # Hypothesis : while takes mystery_word outside the code so letters never change
        # Solution : try to apply changes on mystery_word outside loop too ?
        while "_" in mystery_word or mistakes < 3:
            # showing player what it must find
            print(mystery_word)
            # asking player to choose a letter
            player_choice = input("\n✏️   Please choose a letter to try :\n")
            try:
                # Is operationnal but only if the right letter with case sensitivity is putted in, if wrong letter (Upper or lower case sensitivity included : H != h) is input adds 'mystery_word' to string
                # verifying if player inserted only one character
                if len(player_choice) == 1:
                    # verifying if the player choice is in the word
                    if player_choice.lower() in computer.lower():
                        # if it is, search for its position
                        letter_position = computer.find(player_choice)
                        # replaces _ at the first occurence of the matching player input
                        mystery_word = mystery_word[:letter_position] + player_choice + mystery_word[letter_position + 1:]
                    # code actually doesn't get here with a wrong guess from player
                    # if the letter is not in the word adds a mistake
                    else:
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