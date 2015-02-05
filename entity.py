from random import randint
from abc import ABCMeta


class Entity(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.health = 4 * randint(1, 8) - (-2)
        self.damage = randint(1, 5)
        self.armour = randint(1, 15)
        self.name = ""

    def attack(self, thing_to_attack):
        if randint(1, 20) > thing_to_attack.armour:
            print("The {0} hits {1} for {2} damage ({3} health remaining!".format(self.name, thing_to_attack.name, self.damage, thing_to_attack.health))
            thing_to_attack.health = thing_to_attack.health - self.damage
        else:
            print("The {0} misses {1}!".format(self.name, thing_to_attack.name))

        if thing_to_attack.health <= 0:
            print("The {0} is dead!".format(thing_to_attack.name))

class Player(Entity):

    def __init__(self):
        super(Player, self).__init__()
        self.name = "Player"
        self.floor = 0
        self.room = 0


class Enemy(Entity):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(Enemy, self).__init__()


class Alien(Enemy):
    def __init__(self):
        super(Alien, self).__init__()
        self.name = "Alien"
        self.damage += randint(1, 4)

class Robot(Enemy):
    def __init__(self):
        super(Alien, self).__init__()
        self.name = "Robot"
        self.armour += randint(1, 4)
        self.health += randint(1, 4)