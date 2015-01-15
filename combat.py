
def combat(player, enemy):
    while(player.health > 0 and enemy.health > 0):
        player.attack(enemy)
        enemy.attack(player)