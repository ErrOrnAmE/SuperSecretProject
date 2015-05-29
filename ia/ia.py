#!/usr/bin/env python3
# -*- coding: utf-8 -*-

tablier = [[1,2,3],[4,5,6],[7,8,9]]

tablock = [[0,1,0,0],[0,-1,0,0],[0,0,0,0],[0,0,0,0]]

largeur = 3
hauteur = 3

class IA(object):

	def __init__(self,tablier,tablock):
		self.tablier = tablier;
		self.tablock = tablock;

	def createMap(self):
		self.lock = Lock(self.tablier,self.tablock,0,1)




class Lock(object):

	def __init__(self,tablier,tablock,x,y):

		self.x = x
		self.y = y

		if (tablock[y][x] != 0):
			self.diff = None
			print("Indisponible")
			return

		if (x > 0 and y > 0 and x < largeur and y < hauteur):
			conteneurs = tablier[y-1:y+1]
			for index in range(len(conteneurs)):
				conteneurs[index] = conteneurs[index][x-1:x+1]

			print(conteneurs)

			locks = tablock[y-1:y+2]
			for index in range(len(locks)):
				locks[index] = locks[index][x-1:x+2]

			#print(conteneurs)

			avant = self.nbPointsLock(conteneurs,locks)
			locks[1][1] = 1
			#print(locks)
			apres = self.nbPointsLock(conteneurs,locks)

			#print("nous: "+str(apres[0]-avant[0])+" eux:"+str(apres[1]-avant[1]) )
			self.diff = (apres[0]-avant[0])-(apres[1]-avant[1])
		elif (x == 0 and y == 0):
			minilocks = tablock[0:2]
			for index in range(len(minilocks)):
				minilocks[index] = minilocks[index][0:2]

			print(minilocks)

			euxLocks = self.nbLocks(minilocks,-1)
			nousLocks = self.nbLocks(minilocks,1)

			if (euxLocks == nousLocks or euxLocks == nousLocks + 1):
				self.diff = tablier[0][0]
			else:
				self.diff = 0
		elif (x == 0):
			minilocks = tablock[y-1:y+3]
			for index in range(len(minilocks)):
				minilocks[index] = minilocks[index][0:2]

			eux = 0
			nous = 0

			euxLocksHaut = self.nbLocks(minilocks[0:2],-1)
			nousLocksHaut = self.nbLocks(minilocks[0:2],1)

			euxLocksBas = self.nbLocks(minilocks[1:3],-1)
			nousLocksHaut = self.nbLocks(minilocks[1:3],1)

			if (euxLocksHaut > nousLocksHaut):
				eux = tablier[y][x]
			elif (nousLocksHaut > euxLocksHaut):
				nous = tablier[y][x]

			avant = (nous,eux)
			eux = 0
			nous = 0

			minilocks[1][0] = 1

			euxLocksHaut = self.nbLocks(minilocks[0:2],-1)
			nousLocksHaut = self.nbLocks(minilocks[0:2],1)

			euxLocksBas = self.nbLocks(minilocks[1:3],-1)
			nousLocksHaut = self.nbLocks(minilocks[1:3],1)

			if (euxLocksHaut > nousLocksHaut):
				eux = eux + tablier[y][x]
			elif (nousLocksHaut > euxLocksHaut):
				nous = nous + tablier[y][x]

			apres = (nous,eux)

			self.diff = (apres[0]-avant[0])-(apres[1]-avant[1])
		

		print(str(x)+":"+str(y)+" > "+str(self.diff))

	def nbPointsLock(self,conteneurs,locks):
		nous = 0
		eux = 0
		for y in range(len(conteneurs)):
			for x in range(len(conteneurs[y])):
				minilocks = locks[y:y+2]
				for index in range(len(minilocks)):
					minilocks[index] = minilocks[index][x:x+2]

				euxLocks = self.nbLocks(minilocks,-1)
				nousLocks = self.nbLocks(minilocks,1)

				if (euxLocks > nousLocks):
					eux = eux + conteneurs[y][x]
				elif (nousLocks > euxLocks):
					nous = nous + conteneurs[y][x]

		return (nous,eux)

	def nbLocks(self,locks,value):
		nb = 0
		for y in range(len(locks)):
			for x in range(len(locks[y])):
				if (locks[y][x] == value):
					nb = nb+1
		return nb

		


ia = IA(tablier,tablock)
ia.createMap()

#lock = Lock(tablier,tablock,1,1)

print("")
print("")
print("")

#print(lock.nbLocks([[-1,1],[-1,1]],1))