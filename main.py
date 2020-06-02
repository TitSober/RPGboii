import playerClass
import random
import time
pl = playerClass.Player(input("Enter your name: "),"M",5,1,1,1,{"matchbox":1},0,1)
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

def checkIfLvlUp(pl):
    while pl.xp >= pl.lvl*10:
        pl.lvl +=1
        pl.xp -= pl.lvl*10
        print("You leveled up! You are currently level",pl.lvl)
        pointDistribution(pl,3)
def experience_add(pl,xp_value):
    pl.xp += xp_value
    checkIfLvlUp(pl)


experience_add(pl,100)
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

    print("you encountered  an enemy!",end=" ")
    enemy.stats()
    if input("Fight or Run: ").lower() == "run" and player.luck >= 3:
        print("you escaped!")
        return
    else:
        pass
    while player.hp >= 0 or enemy.hp >= 0:
        #print(player.hp)
        #print(enemy.hp)
        timer = random.randint(3,8)

        zac = time.time()
        print("You have to hit the enemy in ",timer,"seconds")
        a = input()
        kon = time.time()
        #print(kon-zac)
        if kon-zac >= timer-1 and kon-zac <= timer+1:
            enemy.hp -= player.attack
            print("enemy has ", enemy.hp, "health left!")
            if enemy.hp <= 0:
                print("you won")
                return
        else:
            print("You missed!")
            player.hp -= enemy.attack
            print("you have ",pl.hp," health points left!")
            if player.hp <= 0:
                print("you lose!")
                return
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

