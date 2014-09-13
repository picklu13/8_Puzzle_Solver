8_Puzzle_Solver
===============
Inspired by http://www.cs.utexas.edu/users/novak/asg-8p.html

Coded for a representation for the state of an 8-puzzle and functions to generate the legal moves and to apply an operator to
a given state. Implemented the following search algorithms and test them on the start states and goal state shown below; 
in each case, measured and printed out the number of nodes examined and the total time required to solve the puzzle, 
as well as the sequence of moves to solve the problem.

Goal:        Easy:        Medium:        Hard:        Worst:

1 2 3        1 3 4        2 8 1          2 8 1        5 6 7
8   4        8 6 2          4 3          4 6 3        4   8
7 6 5        7   5        7 6 5            7 5        3 2 1

Depth-first blind search, with testing for duplicate states.
Bounded depth-first search, with testing for duplicate states.
Iterative Deepening search, with testing for duplicate states.
Iterative Deepening A* (IDA*) search, using the heuristic function h = sum of Manhattan distances between all tiles and 
their correct positions. (Manhattan distance is the sum of the x distance and y distance magnitudes.)
Uniform-cost (breadth-first) search with no heuristic information (h = 0).
Heuristic search using the heuristic function h = number of tiles that are not in the correct place (not counting the blank).
Heuristic search using the Manhattan heuristic function.
Heuristic search using the heuristic function h = (sum of Manhattan distances) * 2.

Input: a board configuration
(1 3 4 8 6 2 7 0 5)

Output: sequence of moves
(UP RIGHT UP LEFT DOWN)



