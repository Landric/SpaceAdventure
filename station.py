from random import randint, shuffle
from entity import Robot, Alien


class GameException(Exception):
    def __init__(self, msg):
        super(GameException, self).__init__(msg)


class Station(object):

    def __init__(self, levels=1, min_rooms=20, max_rooms=20):
        self.levels = []

        if levels < 1:
            print "Cannot make a station with 0 or fewer levels; reverting to default of one level"
            levels = 1
        if min_rooms < 1:
            print "Cannot make a station with 0 or fewer rooms; reverting to default of twenty rooms"
            min_rooms = 20
        if min_rooms > max_rooms:
            print "Maximum rooms cannot be less than minimum rooms; reverting to default of minimum rooms ({0})".format(min_rooms)
            max_rooms = min_rooms

        for i in range(levels):
            self.levels.append(Level(i, randint(min_rooms, max_rooms)))


class Level(object):

    def __init__(self, id, rooms):
        self.id = id
        self.rooms = []
        # Create rooms
        for room in range(rooms):
            self.rooms.append(Room(room))

        # Create connections
        this_room = 0

        labels = ["{0}{1}".format(id, str(l)) for l in range(int(rooms*1.5))]
        shuffle(labels)

        for i in range(int(rooms*1.5)-1):
            next_room = randint(0, rooms-1)

            door = Door(i, labels.pop(), this_room, next_room)
            self.rooms[this_room].doors.append(door)
            self.rooms[next_room].doors.append(door)

            this_room = next_room

        exit = Door(int(rooms*1.5), labels.pop(), this_room, -1)
        self.rooms[this_room].doors.append(exit)


class Room(object):
    def __init__(self, id):
        self.id = id
        self.doors = []
        self.objects = []
        self.entities = []

        if randint(0, 100) > 80:
            if randint(0, 1) == 1:
                self.entities.append(Alien())
            else:
                self.entities.append(Robot())

    def describe(self):
        print "You are in a room."
        print "There are {0} doors here. The doors are labelled {1}.".format(
            len(self.doors),
            ", ".join([door.label for door in self.doors])
        )
        if self.objects:
            print "You can see a {0} on the floor here.".format(", ".join([object for object in self.objects]))
        if self.entities:
            print "There is a {0} in the room!".format(", ".join([entity.name for entity in self.entities]))
        if not(self.objects or self.entities):
            print "There is nothing else of note in this room."


class Door(object):

    def __init__(self, id, label, a, b):
        self.id = id
        self.label = label
        self.side_a = a
        self.side_b = b

    def enter(self, location):
        if self.side_a == location:
            return self.side_b
        elif self.side_b == location:
            return self.side_a
        else:
            raise GameException("Player cannot see door {0} from here!".format(self.id))