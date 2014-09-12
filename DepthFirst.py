from Utilities import Utility

class DepthFirst:
    def __init__(self):
        self.nodesVisited=0
        self.maxDepth=0
        return

    def backtrace(self, parentDict, start, end):
        path = [end]
        print (parentDict)
        while path[-1] != start:
            path.append(parentDict[path[-1]])
        
        print (path)

    
    def backtrack(self, finalNode):
        tempnode = finalNode
        configList = []
        opList = []
        path = [finalNode]
        while tempnode.parent != "NULL":
            path.append((tempnode.parent))
            tempnode = tempnode.parent
            
        
        path.reverse()
        moveString=""
        for node in path:
            moveString += " "+ node.operation
            
        
        print (moveString)
        '''
        for node in path:
            node.printNode()
            print ("-->")
        '''
        
        print ("Nodes Compared = " + str(self.nodesVisited))
        print("Max Length of Node List = "+ str(self.maxDepth))
             
            
            
        
    
    def iterativeDFS(self, startNode, goalNode):
        dfsQueue = []
        visitedNode = {}
        parent = {}
        utility = Utility()
        numPopped = 0
        dfsQueue.append(startNode)
        while len(dfsQueue) != 0:
            popped = dfsQueue.pop()
            numPopped += 1
            print (popped)
            print ("Num Popped " + str(numPopped))

            if (popped == goalNode):
                return self.backtrack(popped)
            
            else:
                visitedNode[popped.stringRep]= popped
                self.nodesVisited+=1
                if self.maxDepth < popped.level:
                    self.maxDepth = popped.level
                popped.expand()
                listSuccessor = popped.children
                for child in listSuccessor:
                    if child.stringRep not in visitedNode:
                        dfsQueue.append(child)
                        
    
    
    
    def dfs_Search(self, graph, root, target):
        queue = []
        parent = {}
        queue.append(root)
        while len(queue) != 0:
            popped = queue.pop()
            if popped == target:
                return self.backtrace(parent, root, target)
            if popped in graph:
                childrenOfPopped = graph[popped]
                for child in childrenOfPopped:
                    if child not in queue:
                        queue.append(child)
                        parent[child] = popped
