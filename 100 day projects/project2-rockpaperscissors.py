'''
    this is a classic game rock paper scissors made using python

'''
print("welcome to the game of rock,paper or scissors")
choices=['rock','paper','scissors']
import random
i=0
while i<5:
    computerchoice=random.choice(choices)
    playerchoice=input("choose rock,paper or scissors:")
    if(playerchoice.lower() in choices):
        if(computerchoice.lower()==playerchoice):
            print("computer chose",computerchoice)
            print("draw")
        elif((computerchoice.lower()=='rock' and playerchoice.lower()=='scissors') or (computerchoice.lower()=='paper' and playerchoice.lower()=='rock') or (computerchoice.lower( )=='scissors' and playerchoice.lower=='paper')):
            print("computer chose",computerchoice)
            print("computer has won!!!")
        else:
            print("computer chose",computerchoice)
            print("you have won!!!")
        i+=1
    else:
        print("wrong input(please choose rock,paper or scissors)")
print("thanks you for playing")
    