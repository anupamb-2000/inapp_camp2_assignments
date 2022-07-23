import random
import math


guessTemp = {

    2 : "hot",

    3 : "warm",

    4 : "neutral",

    5 : "neutral",

    6 : "cold",

    7 : "cold",

    8 : "very cold",

    9 : "very cold"

}


def play_game(no_of_guesses) :

    number = random.randint(1, 10)

    print("I've already guessed one.")

    end_of_game = False

    while not end_of_game and no_of_guesses > 0 :

        print(f"You have {no_of_guesses} attempts remaining.")

        guess = int(input("Enter your guess : "))

        match math.fabs(guess - number):
            case 1:
                remark = "very hot"
            case 2:
                remark = "hot"
            case 3:
                remark = "warm"
            case 4:
                remark = "neutral"
            case 5:
                remark = "neutral"
            case 6:
                remark = "cold"
            case 7:
                remark = "cold"
            case 8:
                remark = "very cold"  
            case 9:
                remark = "very cold" 
            case _:
                print(f"It's a match!Congrats")

        if guess > number : 

            print(f"Your guess is {remark} from the left and cold from the right. Try again")

            no_of_guesses -= 1

        elif guess < number : 

            print(f"Your guess is cold from the left and {remark} from the right. Try again")

            no_of_guesses -= 1
        else : 

            print()

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