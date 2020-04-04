import playerClass
import random
pl = playerClass.Player(input("Enter your name: "), input("enter your gender"),20,3, 2)
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

battle(pl,enemy)

menu = [pl.greeting,battle]
print("")
inventory = [[pl.greeting,2,3,4],   
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]]
inventory[0][0]()

