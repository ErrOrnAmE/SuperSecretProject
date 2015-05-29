class Interpretation:
    """
    def generateTablier(self, msg):
       
        self.tablier
        self.tablock
       
    """     

    def __init__(self):
        self.nbJetons=20
        self.nbJetonsAdvers=20
        self.scoreNous=0
        self.scoreAdvers=0
        self.tablier = []
        self.tablock = []

    def routeur(self, msg):
        msgArray = msg.split("\n")
        for mess in msgArray:
            num = mess[0]+mess[1]
            if(num == 'MA'):
                self.generateTablier(mess.split("=")[1])
            elif(num == '10'):
                IA(self.tablier, self.tablock).getCoordBestLock()
            elif(num == '20'):
                shit = mess.split(":")[2]
                coord = self.shitToCoord(shit)
                self.majLock(coord[0],coord[1], 1)
            elif(num == '88'):
                res = msg.split(" ")[4] 
                if res == ("gagné"): 
                    return "win" 
                else:
                    return "lose"
            return ""


    def generateTablier(self, msg):
        if msg[len(msg)-1] == "|":
            msg = msg[:len(msg)-1]
        lineArray = msg.split("|")
        cbLigne = len(lineArray)
        cbColonne = len(lineArray[0].split(":"))
        for line  in lineArray:
            self.tablier.append(line.split(":"))
        for x in range(0,cbColonne):
            foo = []
            for y in range(0,cbLigne):
                foo.append(0)
            self.tablock.append(foo)
        

    def majLock(x,y,who): 
        self.tablock[x][y] = who
