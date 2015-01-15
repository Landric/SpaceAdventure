from entity import Enemy, Ted

player = Ted()
rooms = generateRooms()

def generateRooms():
    pass

def mainLoop():
    while(True):

        for enemy in rooms[player.location].objects:
            if isinstance(enemy, Enemy):
                combat(player, enemy)

        move()

def move():
    pass

def combat(player, enemy):
    while(player.health > 0 and enemy.health > 0):
        player.attack(enemy)
        enemy.attack(player)
