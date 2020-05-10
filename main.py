import playerClass
import random
import time
pl = playerClass.Player(input("Enter your name: "),"M",5,1,1,1,{"matchbox":1})
def pointDistribution(player,points):
    num = 0

    while points != 0:
        print("you have ",points, " points left!")
        player.stats()
        num = input("enter 1 to add point to hp, 2 for attack, 3 for speed and 4 for luck: ")
        if num == "1":
            player.hp = player.hp + 1
            points = points - 1
        elif num == "2":
            player.attack = player.attack + 1
            points = points - 1
        elif num == "3":
            player.speed = player.speed + 1
            points = points - 1
        elif num == "4":
            player.luck = player.luck + 1
            points = points - 1
        else:
            print("invalid choice! try again")


pointDistribution(pl,6)

enemy = playerClass.enemy1(10,1,1)
def inventoryAdd(pl,addedItem,quantityOfItem):
    inv = "\n"
    pl.inventory[addedItem] = int(quantityOfItem)
    for item in pl.inventory:
        inv += "|You have {},{}|\n".format(pl.inventory[item],item)
    print(inv)
    return inv


inventoryAdd(pl,"Gold",5)



def battle(player,enemy):
    #while loop wont end
    print("you encountered  an enemy!",end=" ")
    enemy.stats()
    if input("Fight or Run: ") == "Run":
        print("you escaped!")
        return
    else:
        pass
    while player.hp >= 0 or enemy.hp >= 0:
        timer = random.randint(3,8)

        zac = time.time()
        print("You have to hit the enemy in ",timer,"seconds")
        a = input()
        kon = time.time()
        print(kon-zac)
        if kon-zac >= timer-1 and kon-zac <= timer+0.5:
            enemy.hp -= player.attack
            print("enemy has ", enemy.hp, "health left!")
            if enemy.hp <= 0:
                print("you won")
        else:
            player.hp -= enemy.attack - player.luck//2
            print("you have ",pl.hp," left!")
            if player.hp <= 0:
                print("you lose!")
    '''
    while player.hp >= 0 or enemy.hp >= 0 :
        if player.speed > enemy.speed :
            enemy.hp = enemy.hp - player.attack
            print("enemy has ", enemy.hp, "health left!")
            player.speed = player.speed - (random.randint(1,5)/10)/player.luck
            if enemy.hp <= 0:
                print("you won!")
                break
        elif enemy.speed >= player.speed:
            player.hp = player.hp - enemy.attack
            enemy.speed = enemy.speed - random.randint(1, 5)/10*player.luck
            print("you have ", player.hp, "left!")
            if player.hp < 0:
                print("you lost!")
    '''

battle(pl,enemy)

