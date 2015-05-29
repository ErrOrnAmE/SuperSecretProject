#!/usr/bin/env python3
# -*- coding: utf-8 -*-

tablier = [[1,2,3],[4,5,6],[7,8,9]]

tablock = [[-1,1,0,0],[-1,0,0,0],[0,0,0,0],[0,0,0,0]]

class IA(object):

	def __init__(self,tablier,tablock):
		self.tablier = tablier;
		self.tablock = tablock;

	def createMap(self):
		self.lock = Lock(self.tablier,self.tablock,1,1)




class Lock(object):

	def __init__(self,tablier,tablock,x,y):
		conteneurs = tablier[x-1:x+1]
		for index in range(len(conteneurs)):
			conteneurs[index] = conteneurs[index][y-1:y+1]

		locks = tablock[x-1:x+2]
		for index in range(len(locks)):
			locks[index] = locks[index][y-1:y+2]

		#print(conteneurs)

		avant = self.nbPointsLock(conteneurs,locks)
		locks[1][1] = 1
		#print(locks)
		apres = self.nbPointsLock(conteneurs,locks)

	def nbPointsLock(self,conteneurs,locks):
		nous = 0
		eux = 0
		for x in range(len(conteneurs)):
			for y in range(len(conteneurs[x])):
				minilocks = locks[x:x+2]
				for index in range(len(minilocks)):
					minilocks[index] = minilocks[index][y:y+2]

				euxLocks = self.nbLocks(minilocks,-1)
				nousLocks = self.nbLocks(minilocks,1)

				if (euxLocks > nousLocks):
					eux = eux + conteneurs[x][y]
				elif (nousLocks > euxLocks):
					nous = nous + conteneurs[x][y]

		print("score:")
		print(nous)
		print(eux)

	def nbLocks(self,locks,value):
		nb = 0
		for x in range(len(locks)):
			for y in range(len(locks[x])):
				if (locks[x][y] == value):
					nb = nb+1
		return nb

		


ia = IA(tablier,tablock)
ia.createMap()

#lock = Lock(tablier,tablock,1,1)

print("")
print("")
print("")

#print(lock.nbLocks([[-1,1],[-1,1]],1))