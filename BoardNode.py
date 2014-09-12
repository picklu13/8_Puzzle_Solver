
class BoardNode:
    def __init__(self,config,parentNode,operation,blankIndex,level=-1,stringRep=""):
        self.config=config
        self.parent = parentNode
        self.operation = operation
        self.blankIndex = blankIndex
        self.level = level
        self.stringRep = stringRep
        self.children=[]
    
    def printConfig(self): 
        for row in self.config:
            print (row) 
          
    
    def printNode(self):
        
        '''
        if self.parent !="NULL":
            print "parentConfig of the Node "
            utility.printConfig(self.parent.config)
            print "operated by " + self.operation
        '''
        print ("Puzzle Config ==")
        self.printConfig()
        print ("Obtained  by " + self.operation + " operation from Parent. Current Level: " + str(self.level))
        
    def getoperatedConfig(self,config,operation,blankIndex):
        rowBlank= blankIndex[0]
        columnBlank = blankIndex[1]
        configChanged=False
        newblankIndex = (0,0)
        if operation =="LEFT":
            if not(blankIndex[1]==0):
                config[rowBlank][columnBlank] = config[rowBlank][columnBlank-1]
                config[rowBlank][columnBlank-1]=0
                newblankIndex = (rowBlank,columnBlank-1)
                configChanged=True
                
        if operation == "RIGHT":
            if not (blankIndex[1]==2):
                config[rowBlank][columnBlank] = config[rowBlank][columnBlank+1]
                config[rowBlank][columnBlank+1]=0
                newblankIndex = (rowBlank,columnBlank+1)
                configChanged=True

        
        if operation == "UP":
            if not (blankIndex[0]==0):
                config[rowBlank][columnBlank] = config[rowBlank-1][columnBlank]
                config[rowBlank-1][columnBlank]=0
                newblankIndex = (rowBlank-1,columnBlank)
                configChanged=True

        
        if operation =="DOWN":
            if not (blankIndex[0]==2):
                config[rowBlank][columnBlank] = config[rowBlank+1][columnBlank]
                config[rowBlank+1][columnBlank]=0
                newblankIndex = (rowBlank+1,columnBlank)
                configChanged=True

        stringRepOfConfig = self.getStringRep(config)
        return (configChanged,config,newblankIndex,stringRepOfConfig)
   
   
    def getStringRep(self,config):
        stringReper=""
        for i in range(3):
            for j in range(3):
                stringReper +=str(config[i][j])
        return stringReper
    
    
    def expand(self):
        
        opList=["LEFT","RIGHT","UP","DOWN"]
        
                
        blankIndex= self.blankIndex
        for op in opList:
            curConfig=[[1,1,1],[1,1,1],[1,1,1]]
            for x in range(3):
                for y in range(3):
                    curConfig[x][y]=self.config[x][y]
            newConfigDetails = self.getoperatedConfig(curConfig, op, blankIndex)
            configChanged = newConfigDetails[0]
            
            
            if configChanged:
                newConfig = newConfigDetails[1]
                newBlankIndex = newConfigDetails[2]
                newStringRep = newConfigDetails[3]
                newChildNode = BoardNode(newConfig,self,op,newBlankIndex,self.level+1,newStringRep)
                self.children.append(newChildNode)
        
            
        
    
    
    
    def generateSuccessorConfiguration(self):
        listOfChildrenConfig=[]
        
#        curConfig = curNode.config
        opList=["LEFT","RIGHT","UP","DOWN"]
        for op in opList:
            tempnode = BoardNode(self.config,self.parent,self.operation,self.blankIndex,self.level,self.stringRep)
#            print "id of copied listConfig " + str(id(tempnode))
            newConfiguration = self.getoperatedConfig(tempnode.config,op,tempnode.blankIndex)
            configChanged = newConfiguration[0]
            stringRepOfConfig= newConfiguration[3]
            
            if configChanged:
                newConfig = newConfiguration[1]
                newblankIndex = newConfiguration[2]
               
                listOfChildrenConfig.append((newConfig,newblankIndex,op,stringRepOfConfig))
        
        return listOfChildrenConfig
    
    
    
    def getSuccessorNodes(self):
        listOfSuccessorNodes=[]
        listOfSuccessorConfigs = self.generateSuccessorConfiguration()
        for configDetail in listOfSuccessorConfigs:
            boardConfig  = configDetail[0]
            blankIndex = configDetail[1]
            op = configDetail[2] 
            stringRep = configDetail[3]
            level = self.level+1
            newNode = BoardNode(boardConfig,self,op,blankIndex,level,stringRep)
            listOfSuccessorNodes.append(newNode)
        
        return listOfSuccessorNodes
    
    def __lt__(self, other):
        return self.stringRep < other.stringRep

    def __str__(self):
    	return str( self.config) + " at depth " + str(self.level) 
    	
    def __repr__(self):
    	return self.config
    	
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.stringRep==other.stringRep)
            '''
           
            for i in range(3):
                for j in range(3):
                    if self.config[i][j] != other.config[i][j]:
                        return False
            
            return True
              '''
      
                    
