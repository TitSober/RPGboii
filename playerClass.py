#ban is bool does nothing now

#gender not important rn
class Player:
    def __init__(self, name, gender, bad, race):
        self.name = name
        self.gender = gender
        self.bad = bad
        self.race = race
    def introduction(self):
        print("hi my name is", self.name," I am ",self.race)