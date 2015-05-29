from ia import IA
import random

class Interpretation:
    """
    def generateTablier(self, msg):
       
        self.tablier
        self.tablock
       
    """     

    def __init__(self):
        self.tablier = []
        self.tablock = []

    def routeur(self, msg):
        msgArray = msg.split("\n")
        for mess in msgArray:
            num = mess[0]+mess[1]
            print(num)
            if(num == 'MA'):
                self.generateTablier(mess.split("=")[1])
            elif(num == '10'):
                print(self.tablier)
                print(self.tablock)
                try:
                    coord = IA(self.tablier, self.tablock).getCoordBestLock()
                    print(coord)
                    self.majLock(coord[0],coord[1], 1)
                    print("-> I retourne {}".format(self.cord2Shit(coord[0],coord[1])))
                    return self.cord2Shit(coord[0],coord[1])
                except IndexError:
                    coord0 = random.randint(0, len(self.tablock))
                    coord1 = random.randint(0, len(self.tablock))
                    print(coord0)
                    print(coord1)
                    self.majLock(coord0,coord1, 1)
                    return self.cord2Shit(coord0,coord1)
            elif(num == '20'):
                shit = mess.split(":")[2]
                coord = self.shit2Cord(shit)
                print(coord)
                self.majLock(coord[0],coord[1], -1)
            elif(num == '88'):
                res = msg.split(" ")[4] 
                if res == ("gagné"): 
                    print("-> I retourne win")
                    return "win" 
                else:
                    print("-> I retourne lose")
                    return "loose"
            elif(num == '91'):
                return "stop"
        return ""

    def shit2Cord(self,string): 
        taille = len(string) 
        if taille==3: 
            x = (int) (string[0]) 
            y = ord(string[1]) - 65
            coté = (int) (string[2]) 
        elif taille==4: 
            x = int (string[0]+string[1]) 
            y = ord(string[2]) -65
            coté = (int) (string[3]) 
        if coté ==1: 
            return (x-1,y) 
        elif coté == 2: 
            return (x,y) 
        elif coté == 3: 
            return (x,y+1) 
        elif coté == 4: 
            return (x-1,y+1)

    def cord2Shit(self,x,y): 
        longeur = len (self.tablock) 
        largeur = len (self.tablock[0]) 
        if y < longeur and x < largeur: 
            return str(x+1)+chr(y+65)+"1" 
        elif y== longeur and x == largeur: 
            return str(x)+chr((y-1)+65)+"3" 
        elif y == longeur: 
            return str(x+1)+chr((y-1)+65)+"4" 
        elif x== largeur: 
            return str(x)+chr((y)+65)+"2"


    def generateTablier(self, msg):
        if msg[len(msg)-1] == "|":
            msg = msg[:len(msg)-1]
        lineArray = msg.split("|")
        cbLigne = len(lineArray)+1
        cbColonne = len(lineArray[0].split(":"))+1
        for line  in lineArray:
            caca=line.split(":")
            for index in range(len(caca)):
                caca[index] = (int)(caca[index])
            self.tablier.append(caca)
        for x in range(0,cbLigne):
            foo = []
            for y in range(0,cbColonne):
                foo.append(0)
            self.tablock.append(foo)
        

    def majLock(self,x,y,who): 
        self.tablock[x][y] = who
