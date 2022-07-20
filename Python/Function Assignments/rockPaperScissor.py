#Make a two-player Rock-Paper-Scissor game. One of the players is the computer.
#5 chances. Print out the winner and points earned by both players
#Remember the rules :
#Rock beats scissor
#Scissors beats paper
#Paper beats rock

from random import randint

#ASCII Art Dictionary
art = {1: """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
2: """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
3: """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""}

#game rules dictionary
rules = {1 : 3, 2 : 1, 3 : 2}

#function to get the user's choice
def userChoice():
    U = int(input(""" 
Pick a choice:
    1. Rock
    2. Paper
    3. Scissor
    """))
    if U not in [1,2,3]:
        print("Invalid Input!")
        exit()
    return U

#function to get the computer's choice
def computerChoice():
    C = randint(1,3)
    return C

#function to check scores
def checkScore(u, c):
    global uScore, cScore
    if(rules[u] == c):
        print("\nRound Result : User won the round")
        uScore += 1
    elif(rules[c] == u):
        print("\nRound Result : Computer won the round")
        cScore += 1
    else:
        print("\nRound Result : Tied!")
    print("SCORES : ")
    print(f"\tUser : {uScore}")
    print(f"\tComputer : {cScore}")


#initializing user and computer scores
uScore = 0
cScore = 0

#loop for 5 rounds
for i in range(5):
    u = userChoice()
    print(f"""User's Choice : 
    {art[u]}""")
    c = computerChoice()
    print(f"""Computer's Choice : 
    {art[c]}""")
    checkScore(u,c)
if(uScore > cScore) :
    print("\n\nUSER WON! Congratulations\n")
elif(cScore > uScore):
    print("\n\nCOMPUTER WINS! Better luck next time\n")
else:
    print("\n\nIt's a TIE!\n")