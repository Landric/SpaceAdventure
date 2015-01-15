#!/usr/bin/env python3

import random

class GameException(Exception):
	def __init__(self, str):
		pass

class Door(object):
	def __init__(self, number, destination):
		self.__doorNumber = number
		self.__roomDestiny = destination

	def which(self):
		return self.__doorNumber

	def checkDestination(self, destination):
		return self.__roomDestiny == destination

	def getDestination(self):
		return self.__roomDestiny

	def go(self):
		return self.__roomDestination

class Room(object):
	def __init__(self, number):
		self.__number = number
		self.__doors = []
		self.__objects = []
		self.__doorNumber = 1

	def which(self):
		return self.__number

	def getDoors(self):
		return self.__doors

	def addDoor(self, destination):
		for i in range(len(self.__doors)):
			if self.__doors[i].checkDestination(destination):
				raise GameException("Destination is already connected")
		tmpDoor = Door(self.__doorNumber, destination)
		self.__doorNumber += 1
		self.__doors.append(tmpDoor)

	def addObject(self, Object):
		self.__objects.append(Object)

	def enterRoom(self):
		print("You are in room number %d" % self.__number)

class RoomGenerator(object):
	def __init__(self, num_rooms):
		self.__numRooms = num_rooms
		self.__rooms = []

	def getRooms(self):
		for i in range(self.__numRooms):
			print("Creating room %d" % i)
			newRoom = Room(i+1)
			self.__rooms.append(newRoom)
		print("Created %d rooms" % self.__numRooms)

	def generate(self):
		x = 0
		y = 0
		for i in range(self.__numRooms + 10):
			y = random.randint(0, self.__numRooms-1)
			try:
				print("Connecting room %d to room %d" % (x,y))
				self.__rooms[x].addDoor(self.__rooms[y])
				self.__rooms[y].addDoor(self.__rooms[x]) 
				print("Connected room number %d to room number %d" % (x+1, y+1))
				x = y
			except GameException as e:
				print("Room number %d is already connected to room number %d" % (x+1, y+1))
				# Do nothing, just move on

	def rooms(self):
		return self.__rooms

if __name__ == '__main__':
	generator = RoomGenerator(20)
	generator.getRooms()
	generator.generate()

	while(1):
		currRoom = generator.rooms()[0]
		currRoom.enterRoom()
		i = random.randint(0, len(currRoom.getDoors()))
		currRoom = (currRoom.getDoors()[i]).getDestination()
		currRoom.enter()
