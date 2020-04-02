import random
import time

def displayIntro():
    print("Hello and Welcome to the game!")
    time.sleep(3)
    print('You have come upon 2 paths to take.')
    time.sleep(2)
    print('You could choose 1, which takes you through varies trails, that may vary well lead you home.')
    time.sleep(3)
    print('You could choose 2, which takes you on a journey of possibly Death.')
    time.sleep(1)
    print()
def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Which path would you like to take 1 or 2?" )
    return path
def checkPath(choosePath):
    print("You head down the path...")
    time.sleep(5)
    print('There is an Orge, he smacks you a few times!')
    time.sleep(1)
    print('You evade his 5th...6th...7th blow.')
    time.sleep(5)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print()
    time.sleep(3)

    correctPath = random.randint(1,2)

    if choosePath == correctPath:
        print('You have found a treasure chest full of gold, found you a lady, and none the less killed 20 Orges')
        print('Your city would like to congratulate you on your efforts')
        time.sleep(4)
        print('We are having a parade and giving you a key to the city!!!')
    else:
        print('We are sorry to announce the death of a great warrior...')
        print('We would like to set aside multiple days for grievance and rest for the loved ones.')




playAgain = 'Yes'
while playAgain == 'Yes' or playAgain =="Y" or playAgain == "y" or playAgain == "yes":
    displayIntro()
    choice = choosePath()
    checkPath(choice)
    playAgain = input("Do you want to play again? Yes or Y to continue playing?")


displayIntro()
choosePath()
