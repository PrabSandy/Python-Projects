def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

'''Code Explanation:

We define the main function that initializes the arguments: 
global count, global display, global word, global already_guessed, global length and global play_game. 
They can be used further in other functions too depending on how we want to call them.
Words_to_guess: Contains all the Hangman words we want the user to guess in the game.
Word: we use the random module in this variable to randomly choose the word from words_to_guess in the game.
Length: len() helps us to get the length of the string.
Count: is initialized to zero and would increment in the further code.
Display: This draws a line for us according to the length of the word to guess.
Already_guessed: This would contain the string indices of the correctly guessed words.'''