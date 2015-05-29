class Interpretation:
    """
    def generateTablier(self, msg):
       
        self.tablier
        self.tablock
       
    """     

    def generateTablier(self, msg):
        self.tablier = []
        lineArray = msg.split("|")
        for line  in lineArray:
                self.tablier.append(line.split(":"))
        return self.tablier

    

    
