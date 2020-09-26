# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()


'''Code Explanation:

We call all the arguments again under the hangman() function.
Limit: It is the maximum guesses we provide to the user to guess a particular word.
Guess: Takes the input from the user for the guessed letter. Guess.strip() removes the letter from the given word.
If loop checks that if no input is given, or two letters are given at once, or a number is entered as an input, 
it tells the user about the invalid input and executes hangman again.'''
