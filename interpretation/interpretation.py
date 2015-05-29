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
        self.tabLock = []

    def routeur(self, msg):
        num = msg[0]+msg[1]
        
        if(num == '1-'):
            1+0
        elif(num == '2-'):
            1+0
        elif(num == '01'):
            self.generateTablier(msg.split("=")[1])
        elif(num == '10'):
            ia.coupOptimal(self.tablier)


    def generateTablier(self, msg):
        lineArray = msg.split("|")
        for line  in lineArray:
                self.tablier.append(line.split(":"))
                
        
    
    def majLock(x,y,who): 
        self.tablock[x][y] = who
