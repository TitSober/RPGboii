
class Player:
    def __init__(self, name, gender, hp,attack, speed,luck, inventory,xp,lvl):
        self.name = name
        self.gender = gender
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.luck = luck
        self.inventory = inventory
        self.xp = xp
        self.lvl = lvl
    def stats(self):
        return "Your max health is ",self.hp,",your attack is  ",self.attack,", your speed is ",self.speed," and your luck is ",self.luck,"!"," You are Level",self.lvl


class enemy1:
    def __init__(self,hp,attack,speed):
        self.hp = hp
        self.attack = attack
        self.speed = speed
    def stats(self):
        print("This enemy has: ",self.hp," health, ",self.attack, " attack power and ",self.speed, "speed!")

