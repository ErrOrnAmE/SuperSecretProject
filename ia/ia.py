#!/usr/bin/env python3
# -*- coding: utf-8 -*-

tablier = [[1,2,3],[4,5,6],[7,8,9]]

tablock = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

largeur = len(tablier[0])
hauteur = len(tablier)

class IA(object):

	def __init__(self,tablier,tablock):
		self.tablier = tablier;
		self.tablock = tablock;

	def getCoordBestLock(self):
		maxLock = None
		for y in range(len(self.tablock)):
			for x in range(len(self.tablock[y])):
				lock = Lock(self.tablier,self.tablock,x,y)
				if (lock.diff != None and (maxLock == None or lock.diff > maxLock.diff) ):
					maxLock = lock

		return (maxLock.x,maxLock.y)




class Lock(object):

	def __init__(self,tablier,tablock,x,y):

		self.x = x
		self.y = y

		if (tablock[y][x] != 0):
			self.diff = None
			#print("Indisponible")
			return

		if (x > 0 and y > 0 and x < largeur and y < hauteur):

			#print("au milieu")

			conteneurs = tablier[y-1:y+1]
			for index in range(len(conteneurs)):
				conteneurs[index] = conteneurs[index][x-1:x+1]

			#print(conteneurs)

			locks = tablock[y-1:y+2]
			for index in range(len(locks)):
				locks[index] = locks[index][x-1:x+2]

			avant = self.nbPointsLock(conteneurs,locks)
			locks[1][1] = 1
			apres = self.nbPointsLock(conteneurs,locks)

			self.diff = (apres[0]-avant[0])-(apres[1]-avant[1])

		elif (x == 0 and y == 0):

			#print("en haut à gauche")

			minilocks = tablock[0:2]
			for index in range(len(minilocks)):
				minilocks[index] = minilocks[index][0:2]

			#print(minilocks)

			euxLocks = self.nbLocks(minilocks,-1)
			nousLocks = self.nbLocks(minilocks,1)

			if (euxLocks == nousLocks or euxLocks == nousLocks + 1):
				self.diff = tablier[0][0]
			else:
				self.diff = 0

		elif (x == largeur and y == 0):

			#print ("en haut à droite")

			minilocks = tablock[0:2]
			for index in range(len(minilocks)):
				minilocks[index] = minilocks[index][x-1:]

			#print(minilocks)

			euxLocks = self.nbLocks(minilocks,-1)
			nousLocks = self.nbLocks(minilocks,1)

			if (euxLocks == nousLocks or euxLocks == nousLocks + 1):
				self.diff = tablier[y][x-1]
			else:
				self.diff = 0

		elif (x == 0 and y == hauteur):

			#print ("en bas à gauche")

			minilocks = tablock[y-1:]
			for index in range(len(minilocks)):
				minilocks[index] = minilocks[index][0:2]

			euxLocks = self.nbLocks(minilocks,-1)
			nousLocks = self.nbLocks(minilocks,1)

			if (euxLocks == nousLocks or euxLocks == nousLocks + 1):
				self.diff = tablier[y-1][x]
			else:
				self.diff = 0

		elif (x == largeur and y == hauteur):

			#print ("en bas à droite")

			minilocks = tablock[y-1:]
			for index in range(len(minilocks)):
				minilocks[index] = minilocks[index][x-1:]

			euxLocks = self.nbLocks(minilocks,-1)
			nousLocks = self.nbLocks(minilocks,1)

			if (euxLocks == nousLocks or euxLocks == nousLocks + 1):
				self.diff = tablier[y-1][x-1]
			else:
				self.diff = 0

		elif (x == 0):

			#print("à gauche")

			minilocks = tablock[y-1:y+2]
			for index in range(len(minilocks)):
				minilocks[index] = minilocks[index][0:2]

			c = [ [tablier[y-1][x]], [tablier[y][x]] ]

			#print(self.nbPointsLock(c,minilocks))
			avant = self.nbPointsLock(c,minilocks)

			minilocks[y][x] = 1

			#print(self.nbPointsLock(c,minilocks))
			apres = self.nbPointsLock(c,minilocks)
		
			self.diff = (apres[0]-avant[0])-(apres[1]-avant[1])

		elif (y == 0):

			#print("en haut")

			minilocks = tablock[0:2]
			for index in range(len(minilocks)):
				minilocks[index] = minilocks[index][x-1:x+2]

			c = [ [tablier[y][x-1], tablier[y][x]] ]

			avant = self.nbPointsLock(c,minilocks)

			minilocks[y][x] = 1

			apres = self.nbPointsLock(c,minilocks)

			self.diff = (apres[0]-avant[0])-(apres[1]-avant[1])

		elif (x == largeur):

			#print("à droite")

			minilocks = tablock[y-1:y+2]
			for index in range(len(minilocks)):
				minilocks[index] = minilocks[index][x-1:]

			c = [ [tablier[y-1][x-1]], [tablier[y][x-1]] ]

			avant = self.nbPointsLock(c,minilocks)
			#print(avant)

			minilocks[1][1] = 1

			apres = self.nbPointsLock(c,minilocks)
			#print(apres)

			self.diff = (apres[0]-avant[0])-(apres[1]-avant[1])

		elif (y == hauteur):

			#print("en bas")

			minilocks = tablock[y-1:]
			for index in range(len(minilocks)):
				minilocks[index] = minilocks[index][x-1:x+2]

			c = [ [tablier[y-1][x-1],tablier[y-1][x]] ]

			#print (minilocks)
			#print (c)

			avant = self.nbPointsLock(c,minilocks)
			#print(avant)

			minilocks[1][1] = 1

			apres = self.nbPointsLock(c,minilocks)
			#print(apres)

			#print((apres[0]-avant[0])-(apres[1]-avant[1]))

			self.diff = (apres[0]-avant[0])-(apres[1]-avant[1])

		#print(str(x)+":"+str(y)+" > "+str(self.diff))

	def nbPointsLock(self,conteneurs,locks):
		nous = 0
		eux = 0
		for y in range(len(conteneurs)):
			'''if (isinstance(conteneurs[y],int)):
				minilocks = locks[y:y+2]
				for index in range(len(minilocks)):
					minilocks[index] = minilocks[index][0:2]

				print()
				print(minilocks)

				euxLocks = self.nbLocks(minilocks,-1)
				nousLocks = self.nbLocks(minilocks,1)

				print("x: "+str(0)+" y: "+str(y)+" > "+str(nousLocks)+"/"+str(euxLocks))

				if (euxLocks > nousLocks):
					eux = eux + conteneurs[y]
				elif (nousLocks > euxLocks):
					nous = nous + conteneurs[y]

				print(nous,eux)
			else:'''

			for x in range(len(conteneurs[y])):
				minilocks = locks[y:y+2]
				for index in range(len(minilocks)):
					minilocks[index] = minilocks[index][x:x+2]

				'''print()
				print(minilocks)'''

				euxLocks = self.nbLocks(minilocks,-1)
				nousLocks = self.nbLocks(minilocks,1)

				#print("x: "+str(x)+" y: "+str(y)+" > "+str(nousLocks)+"/"+str(euxLocks))

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

		


#ia = IA(tablier,tablock)

#lock = Lock(tablier,tablock,1,1)

#print(ia.getCoordBestLock())

#print(lock.nbLocks([[0,1],[0,0]],1))



#Pour récupérer les coordonnées à jouer:
#print(IA(tablier,tablock).getCoordBestLock())