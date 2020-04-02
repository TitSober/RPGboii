#bad is bool does nothing now

#gender not important rn
class Player:
    def __init__(self, name, gender, bad, race, hp):
        self.name = name
        self.gender = gender
        self.bad = bad
        self.race = race
        self.hp = hp

    def introduction(self):
        print("hi my name is", self.name," I am ",self.race)


class enemy1:
    def __init__(self,hp,attack,speed):
        self.hp = hp
        self.attack = attack
        self.speed = speed
    def stats(self):
        print("This enemy has: ",self.hp," health, ",self.attack, " attack power and ",self.speed, "speed!")

