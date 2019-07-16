//  STONE PAPER SCISSOR

from random import randint

def game_choice():
    print("Enter 1 to select Stone")
    print("Enter 2 to select Paper")
    print("Enter 3 to select Scissor")

def user_win():
    print("Yes!!! I win this round")
    print("---Scores---")
    global uc
    uc = uc + 1
    print("User: ", uc)
    print("Computer: ", cc)
    print("------------")

def Computer_win():
    print("Uggh!!! I lost this round")
    print("---Scores---")
    print("User: ", uc)
    global cc
    cc = cc + 1
    print("Computer: ", cc)
    print("------------")

print("Welcome to Stone|Paper|Scissor")
n = int(input("Enter 1 to play:"))

uc = 0
cc = 0
while (uc < 5 and cc < 5):

    game_choice()
    c = randint(1,3)
    print(c)
    ch = input("I choose ")
    if c == 1 and ch == "Paper":
        user_win()
    elif c == 1 and ch == "Scissor":
        Computer_win()
    elif c == 2 and ch == "Stone":
        Computer_win()
    elif c == 2 and ch == "Scissor":
        user_win()
    elif c == 3 and ch == "Stone":
        user_win()
    elif c == 3 and ch == "Paper":
        Computer_win()
    else:
        print("Enter a valid Choice.Please try again!!!")
        continue
if uc == 5:
    print("User won the game!!!")
elif cc == 5:
    print("Computer won the game!!!")
