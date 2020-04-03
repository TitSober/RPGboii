import playerClass
import random
pl = playerClass.Player(input("Enter your name: "), input("enter your gender"),20,3, 2)
enemy = playerClass.enemy1(10,1,1)

def battle(player,enemy):
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
battle(pl,enemy)


