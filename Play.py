from BreadthFirst import BreadthFirst
from DepthFirst import DepthFirst
from BoardNode import BoardNode
from DepthLimited import DepthLimited
from IncrementalDeepeningDFS import IncrementalDepthLimited
from BestFirstSearch import BestFirst
from Utilities import Utility
from AStar import A_Star
import time
import AStar


goalState = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
startState= [[0,2,3],[1,8,4],[7,6,5]]
startStateEasy = [[1, 3, 4], [8, 6, 2], [7, 0, 5]]
startStateMedium = [[2,8,1], [0, 4, 3], [7, 6, 5]]
startStateHard = [[5,6,7], [4,0,8], [3,2,1]]
H1 = "HAMMING_DISTANCE"
H2 = "MANHATTN_DISTANCE"


graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }
startState = startStateHard

# startState = startStateEasy
# startState = startStateMedium
# startState = startStateHard

utility = Utility()
blankIndex = utility.getBlankIndex(startState)
stringRepOfStart = utility.getStringRep(startState)
stringRepOfGoal = utility.getStringRep(goalState)
startNode = BoardNode(startState, 'NULL', 'NULL', blankIndex, 1,stringRepOfStart)
goalNode = BoardNode(goalState, "NULL", "NULL", (1, 1),-1,stringRepOfGoal)

bfsSearch = BreadthFirst()
dfsSearch = DepthFirst()
dfsLimited = DepthLimited()
incDFSLimited = IncrementalDepthLimited()
bestFirstSearch = BestFirst()
astar = A_Star()
start_time = time.time()

astar.aStarSearch(startNode,goalNode,H1)
# bestFirstSearch.bestFirstSearch(startNode, goalNode, H2)
# dfsSearch.iterativeDFS(startNode, goalNode)
# dfsLimited.dfsLimited(startNode, goalNode, 100)
# bfsSearch.iterativeBFS(startNode, goalNode)
# incDFSLimited.incrementalDFSLimited(startNode, goalNode, 50)
# dfsSearch.dfs_Search(graph, '1', '11')
end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))

'''
print "id of startNode " + str(id(startNode.config))
x= Utilities()
x.generateSuccessorNodes(startNode)
'''
        
        
        


                
    
    

