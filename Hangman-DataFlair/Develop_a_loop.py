# A loop to re-execute the game when the first round ends:

def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

'''Code Explanation:

Play_loop: This function takes in the argument of play_game.
Play_game: We use this argument to either continue the game after it is played once or end it according to what the user suggests.
While loop is used to execute the play_game argument. It takes the parameter, y=yes and n=no. 
If the user gives an input of something else other than y/n, it asks the question again for the appropriate answer. 
If the user inputs “y”, the game restarts, otherwise the game ends.'''

