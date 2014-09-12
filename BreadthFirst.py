from Utilities import Utility

class BreadthFirst:
    def __init__(self):
        self.nodesVisited=0
        self.maxDepth=0
#         print("....... Solving by Breadth First Search......")
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
            
           
        print ("Nodes Compared = " + str(self.nodesVisited))
        print("Max Length of Node List = "+ str(self.maxDepth))
        
       
         
             
            
            
        
    
    def iterativeBFS(self,startNode,goalNode):
        bfsQueue=[]
        visitedNode={}
        parent={}
        utility = Utility()
        bfsQueue.append(startNode)
        while len(bfsQueue)!=0:
            popped = bfsQueue.pop(0)
            if (popped==goalNode):
#                 print popped==goalNode
                return self.backtrack(popped)
            
            else:
                self.nodesVisited+=1
                if self.maxDepth < popped.level:
                    self.maxDepth = popped.level
                visitedNode[popped.stringRep] = popped
#                 listSuccessor = popped.getSuccessorNodes()
                popped.expand()
                listSuccessor = popped.children
#                 print ("generating children depth "+str(popped.level))
                for child in listSuccessor:
                    if child.stringRep not in visitedNode:
                        bfsQueue.append(child)
                        
    
    
    
    def bfs_search(self,graph,root,target):
        queue=[]
        parent = {}
        queue.append(root)
        while len(queue)!=0:
            popped = queue.pop(0)
            if popped==target:
                return self.backtrace(parent,root,target)
            if popped in graph:
                childrenOfPopped = graph[popped]
                for child in childrenOfPopped:
                    if child not in queue:
                        queue.append(child)
                        parent[child] = popped