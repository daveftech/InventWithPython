import random

myNumber = random.randint(1, 20)
guessesTaken = 0

print("Welcome to the number guessing game.")
print("What is your name?")
name = input()
print("Thanks, {}.  I am thinking of a number between 1 and 20.  Guess what it is, or press 'q' to quit:".format(name))

for guessesTaken in range(6):
    guess = input()
    guess = int(guess)
    guessesTaken + 1

    if guess < myNumber:
        print("I'm sorry, that guess was too low.  Guess again!")
    if guess > myNumber:
        print("I'm sorry, that guess was too high.  Guess again!")
    if guess == myNumber:
        break    


if guess == myNumber:
    print("Good job, {}!  You got it correct in {} guesses.  See you again next time!".format(name, guessesTaken + 1))
else:
    print("Sorry, {}, but you took {} guesses and didn't guess my number.  It was {}  See you again next time!".format(name, guessesTaken + 1, myNumber))


