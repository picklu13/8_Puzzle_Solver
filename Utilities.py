import copy

class Utility:
    def __init__(self):
        return
   
    def getStringRep(self,config):
        stringReper=""
        for i in range(3):
            for j in range(3):
                stringReper +=str(config[i][j])
        return stringReper
   
    def printConfig(self,config):
        for row in config:
            print (row) 
        
    def getHeuristic(self,childNode,goalNode,heuristic,goalNodeStateDict):    
    	goalConfig = goalNode.config
    	childConfig = childNode.config
    	if heuristic == "HAMMING_DISTANCE":
    		numTileDisplced=0
    		for i in range(3):
    			for j in range(3):
    				if childConfig[i][j]!=goalConfig[i][j]:
    					numTileDisplced+=1
    		
    		return numTileDisplced
    	else:
    		manhattanDistance=0
    		for i in range(3):
    			for j in range (3):
    				cell = childConfig[i][j]
    				goalCellPos =goalNodeStateDict[cell]
    				manhattanDistance+= self.getManhattanDistanceForCell( (i,j), goalCellPos )
    		
    		return manhattanDistance
    		
    	
    def getManhattanDistanceForCell(self,tup1,tup2):
    	dist=abs(tup1[0]-tup2[0] )  + abs(tup1[1]-tup2[1])
    	return dist
    	
    def getGoalNodeStateDict(self,goalNode):
    	goalStateDict={}
    	config = goalNode.config
    	for i in range(3):
    			for j in range(3):
    				goalStateDict[config[i][j]] = (i,j)
    				 
    	return goalStateDict
    	  
    '''  
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
        
	'''
                
    def getBlankIndex(self,state):
        	for i in range(3):
        		for j in range(3):
        			if state[i][j]==0:
        				return (i,j)
    
    '''
    def generateSuccessorConfiguration(self,curNode):
        listOfChildrenConfig=[]
        
#        curConfig = curNode.config
        opList=["LEFT","RIGHT","UP","DOWN"]
        for op in opList:
            tempnode = copy.deepcopy(curNode)
#            print "id of copied listConfig " + str(id(tempnode))
            newConfiguration = self.getoperatedConfig(tempnode.config,op,tempnode.blankIndex)
            configChanged = newConfiguration[0]
            stringRepOfConfig= newConfiguration[3]
            
            if configChanged:
                newConfig = newConfiguration[1]
                newblankIndex = newConfiguration[2]
               
                listOfChildrenConfig.append((newConfig,newblankIndex,op,stringRepOfConfig))
        
        return listOfChildrenConfig
        
    '''