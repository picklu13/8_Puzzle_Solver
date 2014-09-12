from Utilities import Utility
from DepthLimited import DepthLimited

class IncrementalDepthLimited:
    def __init__(self):
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
        for node in path:
            node.printNode()
            print ("-->")
         
             
            
            
        
    '''
    def incrementalDFSLimited(self, startNode, goalNode, limit):
    	depthLimited = DepthLimited()
    	for localLimit in range(1, limit):
    		retVal = depthLimited.dfsLimited(startNode, goalNode, localLimit)
    		print ("DLS With Limit " + str(localLimit) + " returned " + str(retVal))

    '''     
    
    def incrementalDFSLimited(self, startNode, goalNode, limit):
        depthLimited = DepthLimited()
        for localLimit in range(1,limit):
            retVal = depthLimited.dfsLimited(startNode, goalNode, localLimit)
            if retVal !=-1:
                break
    
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
