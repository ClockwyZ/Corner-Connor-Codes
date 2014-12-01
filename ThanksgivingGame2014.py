import random
import sys
import math


def FightClowns(FightChance, NumberOfOpponents): # Change
    FightSuccessRandom=random.randint(1, 100)
    FightOutcome=FightChance*FightSuccessRandom/NumberOfOpponents
    if FightOutcome>=50: # 50 is a placeholder for the time being, need to adjust later
        FightOutput=1 # 1 signifies a victory
    elif FightOutcome<50:
        FightOutput=0 # 0 signifies a loss
    return FightOutput

print("You enter the building and find yourself in a dark hallway. \n\
By the light of the flickering torch you carry, you move along the \n\
length of the hallway and find a large steel door with an ancient 4-dial \n\
combination lock set in the center. The surface of the door is rusted, but \n\
the door doesn\'t budge when you push against it. Driven by your curiosity, \n\
you decide to enter a combination.\n\
There is a desk against the wall with a drawer half open.")
password=random.randint(1000, 9999)
password=str(password)
guess=0

while guess!=password:
    print('\nWhat combination do you enter?')
    guess=input()

    if guess==password:
        print("The lock clicks and the door slowly opens as you push \n\
against it. You cautiously step into the hallway beyond as \n\
electric lights flicker to life ahead.")
    elif guess=='Check the drawer':
        print("The harsh sound of metal-on-metal grates your nerves as \n\
the ancient drawer jerks open. On a yellowed piece of paper, you see the\n\
following four numbers written:")
        print(password)
    else:
        print("The door won't budge.")


