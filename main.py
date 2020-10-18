# This file contains code of unit conversion caluculator
#This code is written in 2 files. They are main.py file and calci.py file.
#main.py file calls the functions in calci.py file and calci.py contains the caluculations required

'''
This a bot designed for playing a word game and helping converting units

This bot greets you with a warm  message. it cheers up you with a cute picture link.

Then the bot asks you to select one of the options to do.

Then the bot will respond accordingly

'''

#Importing required files

from  game import main as gm
from  calci import main as cm



print("Hi there I'm Carlo. I can help ypu cheerup by playing a game or helping in conversion of units. So select one of the option below")
print("1. Word Game\n2. Unit convertor")

while True:
    try:
        choice = int(input())
    except ValueError:
        print("Must be a number")
    else:
        if choice in [1, 2]:
            if choice == 1:
                print("So you are going to Game session. My friend SARA will play the game with you")
                gm.main(gm)
            
            else:
                print("I'm handing over the part to VICTOR. He will help you in converting units.")
                cm.main(cm)


        else:
            print("Must be in range 1 and 2")



