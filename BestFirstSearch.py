from Utilities import Utility
from queue import PriorityQueue

class BestFirst:

	def __init__(self):
		self.nodesVisited=0
		self.maxDepth=0
		self.maxQueueSize=0
		return
    
	def backtrack(self,finalNode):
		tempnode = finalNode
		configList=[]
		opList = []
		path=[finalNode]
		while tempnode.parent!="NULL":
			path.append((tempnode.parent))
			tempnode = tempnode.parent
			
		
		path.reverse()
		moveString =""
		for node in path:
			moveString += " "+ node.operation
			
		
		print (moveString)
			
		   
		print ("Nodes Compared = " + str(self.nodesVisited))
		print("Max Length of Node List = "+ str(self.maxDepth))
         
             
            
            
        
    
	def bestFirstSearch(self, startNode, goalNode, heuristic):
        	bestFitstQueue = PriorityQueue(0)
        
	        visitedNode = {}
	        parent = {}
	        utility = Utility()
	        goalNodeStateDict = utility.getGoalNodeStateDict(goalNode)
	        bestFitstQueue.put((1, startNode))
	        while not(bestFitstQueue.empty()):
	            poppedTuple = bestFitstQueue.get()
	            self.nodesVisited+=1
	            popped = poppedTuple[1]
	            if (popped == goalNode):
	#                 print popped==goalNode
	                return self.backtrack(popped)
	            
	            else:
	                visitedNode[popped.stringRep]=popped
	                if self.maxDepth < popped.level:
	                    self.maxDepth = popped.level
	                popped.expand()
	                
	                for child in popped.children:
	                    if child.stringRep not in visitedNode:
	                     heuristicOfChild = utility.getHeuristic(child, goalNode, heuristic, goalNodeStateDict)
	                     bestFitstQueue.put((heuristicOfChild, child))
	                     self.maxQueueSize +=1
	                        
    
    
    
