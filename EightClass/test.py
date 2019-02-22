import random

class Shark:
    kind = "mammal"

    def __init__(self, name):
        self.name = name

    def swim(self):
        self.kind = "orc"


sharky = Shark("bobby")
print(sharky.kind)
sharky.swim()
print(sharky.kind)


class Enemie:
    Namelist = ["Dase Bottom", "Fortintha Long", "Raldabingo Proud", "Dingla Man", "Rebard Good", "Pimmond Ville", "Baman Pipe", "Tomo Miller"]
    Weaponlist = ["sword", "axe", "club", "spear"]
    Clans = ["Immortals", "Primeval", "Turnbull"]
    SP = ["Possession", "Mind Control", "Invisibility", "Flight", "Elasticity", "Super Strength", "Super Speed"]
    def __init__(self):
        self.name = random.choice(Enemie.Namelist)
        self.clan = random.choice(Enemie.Clans)
        self.specialability = random.choice(Enemie.SP)
        self.weapon = random.choice(Enemie.Weaponlist)

    def weaponpicker(self):
        exit()


sharky = Shark("bobby")
print(sharky.kind)
sharky.swim()
print(sharky.kind)

enemies = []
for i in range(0,10):
    enemies.append(Enemie())

for t in enemies:
    print(t.name.ljust(20), t.clan.ljust(20), t.specialability.ljust(20), t.weapon)


totalpoints=0

class Colectible:
    points = 0

    def __init__(self):
        option = 1
        if option == 0:
            self = Potion()
        if option == 1:
            self = Coin()
class Potion(Colectible):
    color = "blue"
    colorlist=["blue", "red", "orange", "green", "yellow"]

    def __init__(self):
        self.color = random.choice(self.colorlist)

    def colect(self):
        if self.color == "green":
            totalpoints -= 300
        else:
            totalpoints += 100

class Coin(Colectible):

    def colect(self):
        totalpoints +=10


newcolec = Colectible()

