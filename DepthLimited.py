from Utilities import Utility

class DepthLimited:
    def __init__(self):
        self.nodesVisited=0
        self.maxDepth=0
        self.maxQueueSize=0
        return

    def backtrace(self,parentDict,start,end):
        path=[end]
        print (parentDict)
        while path[-1]!=start:
            path.append(parentDict[path[-1]])
        
        print (path)

    
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
        goalNode = path[len(path)-1]
        print (goalNode)
        
        print ("Nodes Compared = " + str(self.nodesVisited))
        print("Max Depth of Node List = "+ str(self.maxDepth))
        print ("Max Queue Size at any Point =" + str(self.maxQueueSize))
        return (self.nodesVisited,self.maxDepth,self.maxQueueSize)
         
          
            
            
        
    
    def dfsLimited(self,startNode,goalNode,limit):
        DFSLimitedQueue=[]
        visitedNode={}
        parent={}
        utility = Utility()
        DFSLimitedQueue.append(startNode)
        self.maxQueueSize=1
        while len(DFSLimitedQueue)!=0:
            popped = DFSLimitedQueue.pop()
            if (popped==goalNode):
#                 print popped==goalNode
                return self.backtrack(popped)
            
            else:
                self.nodesVisited +=1
                if self.maxDepth < popped.level:
                    self.maxDepth = popped.level
                visitedNode[popped.stringRep]=popped
                if not popped.level >= limit:
	                popped.expand()
	                for child in popped.children:
	                    if child.stringRep not in visitedNode:
                                DFSLimitedQueue.append(child)
                                self.maxQueueSize +=1

                            
                    

        return  -1                
    
    
    
    def dfs_Search(self,graph,root,target):
        queue=[]
        parent = {}
        queue.append(root)
        while len(queue)!=0:
            popped = queue.pop()
            if popped==target:
                return self.backtrace(parent,root,target)
            if popped in graph:
                childrenOfPopped = graph[popped]
                for child in childrenOfPopped:
                    if child not in queue:
                        queue.append(child)
                        parent[child] = popped