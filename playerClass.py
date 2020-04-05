
class Player:
    def __init__(self, name, gender, hp,attack, speed,luck):
        self.name = name
        self.gender = gender
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.luck = luck
    def stats(self):
        print("Your max health is ",self.hp,",your attack is  ",self.attack,", your speed is ",self.speed," and your luck is ",self.luck,"!")


class enemy1:
    def __init__(self,hp,attack,speed):
        self.hp = hp
        self.attack = attack
        self.speed = speed
    def stats(self):
        print("This enemy has: ",self.hp," health, ",self.attack, " attack power and ",self.speed, "speed!")

