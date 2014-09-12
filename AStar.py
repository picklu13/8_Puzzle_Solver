from Utilities import Utility
from queue import PriorityQueue
class A_Star:
	
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
		print ("Max Queue Size at Any Point " + str(self.maxQueueSize))
          

	def aStarSearch(self, startNode, goalNode, heuristic):
        	aStarQueue = PriorityQueue(0)
        
	        visitedNode = {}
	        parent = {}
	        utility = Utility()
	        goalNodeStateDict = utility.getGoalNodeStateDict(goalNode)
	        aStarQueue.put((1, startNode))
	        while not(aStarQueue.empty()):
	            poppedTuple = aStarQueue.get()
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
	                     cost = child.level-1
	                     sum = heuristicOfChild+cost
	                     aStarQueue.put((sum, child))
	                     self.maxQueueSize +=1
	                        
    