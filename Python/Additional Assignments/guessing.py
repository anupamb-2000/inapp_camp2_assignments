import random

def play_game(no_of_guesses) :
    number = random.randint(1, 10)
    print("I've already guessed one.")
    end_of_game = False
    while not end_of_game and no_of_guesses > 0 :
        print(f"You have {no_of_guesses} attempts remaining.")
        guess = int(input("Enter your guess : "))
        if guess > number : 
            print("Your guess is warm from the left and cold from the right. Try again")
            no_of_guesses -= 1
        elif guess < number : 
            print("Your guess is cold from the left and warm from the right. Try again")
            no_of_guesses -= 1
        else : 
            print(f"It's a match!Congrats")
            end_of_game = True
    if no_of_guesses == 0 :
        print("You've run out of guesses, you lose.")
        print(f"The number is {number}")
    print("1. Play the game")
    print("2. Exit")
    ch = int(input())
    no_of_guesses = 5
    if(ch == 1):
        play_game(no_of_guesses) 
    elif(ch == 2):
        exit()
    else:
        print("Invalid choice!")
  
print("Welcome to the Number Guessing Game!")
print("1. Start the game")
print("2. Exit")
ch = int(input())
no_of_guesses = 5
if(ch == 1):
    play_game(no_of_guesses) 
elif(ch == 2):
    exit()
else:
    print("Invalid choice!")