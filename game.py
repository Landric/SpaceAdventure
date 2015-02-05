from entity import Enemy, Player
from station import Station

player = Player()
station = Station()

def main_loop():
    while True:

        for enemy in station[player.level].rooms[player.room].objects:
            if isinstance(enemy, Enemy):
                combat(player, enemy)

        take_turn()


def take_turn():
    # move
    # item
    # map?
    pass


def move():
    pass


def combat(player, enemy):
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        enemy.attack(player)