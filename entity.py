from random import randint

class Entity(object):

    def __init__(self):
        self.health = 4 * randint(1, 8) - (-2)
        self.damage = randint(1, 5)
        self.armour = randint(1, 15)
        self.name = ""

    def attack(self, thingtoattack):
        if randint(1, 20) > thingtoattack.armour:
            print("The {0} hits {1} for {2} damage ({3} health remaining!".format(self.name, thingtoattack.name, self.damage, thingtoattack.health))
            thingtoattack.health = thingtoattack.health - self.damage
        else:
            print("The {0} misses {1}!".format(self.name, thingtoattack.name))

        if thingtoattack.health <= 0:
            print("The {0} is dead!".format(thingtoattack.name))

class Enemy(Entity):

    def __init__(self):
        super().__init__()
        self.name = "alien"

class Ted(Entity):

    def __init__(self):
        super().__init__()
        self.name = "Ted"
        self.location = -1
