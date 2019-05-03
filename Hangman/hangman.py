HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

guess_limit = 7
guess_count = 0
correct_count = 0
guesses = ""

keep_playing = True

def reset_game():
    global keep_playing 
    keep_playing = True
    
    global guess_count 
    guess_count = 0

    global correct_count
    correct_count = 0

    global guesses
    guesses = ""

def draw_hangman():
    result = guess_count - correct_count
    print(HANGMAN_PICS[result])
    
def print_result():
    for letter in secret_word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()


while keep_playing:
    print("What is your secret word?: ", end="")
    secret_word = input()

    while guess_count < guess_limit:
        draw_hangman()
        print_result()
        print("Guess a letter: ", end="")
        guess_letter = input()

        if guess_letter in guesses:
            print("You already chose that letter.  Try a different guess!")
            break

        guesses = guesses + guess_letter

        if guess_letter in secret_word:
            print("That letter was in the word :)")
            correct_count = correct_count + 1
        else:
            print("That letter was not in the word :(")

        guess_count = guess_count + 1

        print("You have {} guesses remaining.  You have guessed {} letters correctly.".format(guess_limit - guess_count, correct_count))

    keep_playing_check = ""
    while keep_playing_check.upper() != "Y" and keep_playing_check.upper() != "YES" and keep_playing_check.upper() != "N" and keep_playing_check.upper() != "NO":
        print("Do you want to keep playing? (Enter Y or Yes to keep playing, or N or No to quit): ", end="")
        keep_playing_check = input()
    
    if keep_playing_check.upper() == "Y" or keep_playing_check.upper() == "YES":
        reset_game()        
    else:
        keep_playing = False

print("Game over!")