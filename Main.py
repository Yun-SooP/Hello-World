while True:

    # main menu of the game collection
    print("""
    Welcome~
    This is the main menu.
    Available games:
        1) Hangman
        2) Guess the number
        3) Guess the word

    Type in the number of the game you want to play.
    If you want to exit, then type in: escape
        """)

    number_of_game = input("Your choice: ")
    if number_of_game == "escape":
        break
    right_choice = False

    # selection of game
    while not right_choice:
        match number_of_game:
            case "1":
                right_choice = True
                with open("lib\Hangman.py") as f:
                    exec(f.read())
            case "2":
                right_choice = True
                with open("lib\GuessTheNumber.py") as f:
                    exec(f.read())
            case "3":
                right_choice = True
                with open("lib\GuessTheWord.py") as f:
                    exec(f.read())
            case _:
                print("That's a wrong choice.")
                number_of_game = input("Try again: ")