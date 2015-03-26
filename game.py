from entity import Enemy, Player
from station import Station


class Game(object):

    def __init__(self):
        self.player = Player()
        self.station = Station()

    def play(self):

        while True:
            self.station.levels[self.player.floor].rooms[self.player.room].describe()

            for enemy in self.station.levels[self.player.floor].rooms[self.player.room].entities:

                if isinstance(enemy, Enemy):
                    while self.player.health > 0 and enemy.health > 0:
                        self.player.attack(enemy)
                        if enemy.health > 0:
                            enemy.attack(self.player)
                    self.station.levels[self.player.floor].rooms[self.player.room].entities.remove(enemy)

            # Lose condition
            if self.player.health <= 0:
                print "Oh no, you've died!"
                break

            self.take_turn()

            # Win condition
            if self.player.floor >= len(self.station.levels):
                print "You've escaped!"
                break

    def take_turn(self):
        # move
        # item
        # map?
        self.move()

    def move(self):
        input = raw_input("Which door would you like to enter?")
        visible_doors = self.station.levels[self.player.floor].rooms[self.player.room].doors
        door = next((door for door in visible_doors if door.label == input), None)
        if door is None:
            print "There is no door labeled {0} here!".format(input)
        else:
            self.player.room = door.enter(self.player.room)
            if self.player.room == -1:
                self.player.floor += 1
                self.player.room = 0

if __name__ == "__main__":

    while True:
        game = Game()
        game.play()

        again = raw_input("Do you want to play again?")
        if again.lower != "y":
            print "Goodbye!"
            break

