import playerClass
import random
pl = playerClass.Player(input("Enter your name: "),"M",5,1,1,1,[])
def pointDistribution(player,points):
    num = 0

    while points != 0:
        print("you have ",points, " points left!")
        player.stats()
        num = int(input("enter 1 to add point to hp, 2 for attack, 3 for speed and 4 for luck"))
        if num == 1:
            player.hp = player.hp + 1
            points = points - 1
        elif num == 2:
            player.attack = player.attack + 1
            points = points - 1
        elif num == 3:
            player.speed = player.speed + 1
            points = points - 1
        elif num == 4:
            player.luck = player.luck + 1
            points = points - 1
        else:
            print("invalid choice! try again")


pointDistribution(pl,6)

enemy = playerClass.enemy1(10,1,1)

def battle(player,enemy):
    speed = player.speed
    print("you encountered  an enemy!",end=" ")
    enemy.stats()
    if input("Fight or Run: ") == "Run":
        print("you escaped!")
        return
    else:
        pass
    while player.hp >= 0 or enemy.hp >= 0 :
        if player.speed > enemy.speed :
            enemy.hp = enemy.hp - player.attack
            print("enemy has ", enemy.hp, "health left!")
            player.speed = player.speed - random.randint(1,5)/10
            if enemy.hp <= 0:
                print("you won!")
                break
        elif enemy.speed >= player.speed:
            player.hp = player.hp - enemy.attack
            enemy.speed = enemy.speed - random.randint(1, 5)/10
            print("you have ", player.hp, "left!")
            if player.hp < 0:
                print("you lost!")
    player.speed = speed

def addToInventory(player,item):
    player.inventory.append(item)

addToInventory(pl,"gold coin")
print(pl.inventory)

'''
battle(pl,enemy)

menu = [pl.greeting,battle]
print("")
inventory = [[pl.greeting,2,3,4],   
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]]
inventory[0][0]()

'''