from random import randint
import game
class Survivor(object):
    def __init__(self):
        lying = True if randint(0, 80) > 80 else False

        if lying:
            pass
        else:

