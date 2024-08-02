## State Space Search
- looking at different possibilities before making a decision
- like looking at all possible routes to a destination and then choosing the shortest and best based on criteria
- **Back-tracking**- some paths may lead to dead-end so we go back to the previous choice-point and try an alternative
- **State**- 
	- description of a scenario (time, location, capability)
	- Initial/starting state is the intiail state of the problem to be solved
	- goal/final state is the state to be achieved
	- state is like a snapshot where entities currently are in terms of time, location, capability where it may change
	- if an entity (dog) is starting a certain state (2) and it needs to reach state 8 for its other entity (treats)
		- starting state at(dog, 2) at(treats, 8)
		- goal state at(dog, X) at(treats, X)
- **State Space**- 
	- tree structure
	- each node of the tree represents a state
	- initial state is the root of the tree
	- if node A is a parent of node B, then it is viable to move from state A to state B
	- the goal state may/may not be a node in the tree
	- can think of it like each child node is a possibility of action from the parent node (they have to be connected somehow)
	- nodes can be in multiple branches (if there are multiple ways to connect to it)
	- sometimes the goal state can be on multiple branches (occurs in state space multiple times)
	- sometimes the goal state will be on no branches  (not in the state space)
- trying to identify the shortest path from the initial state to the goal state
- **Constructing State Space**- representation of states is critical when solcing problem using state space search. good representation can have a dramatic effect on the amount of computation required and could mean the difference between solcing and not solving the problem
	- General structure for search problems
		1. Starting state
			- starting city
			- current state of a two player game like chess
		2. Goal state (or a test for goal state)
			- destination city
			- winning state of the game (checkmate)
		3. Permissible operators
			- go to city X
			- move queen to position X
	- Seeing what the intiail state would be for the problem, what the end state is and what are the possible moves that can be done for the entity to get from the start start to the goal state
- **State Space Search**- 
	- involves finding a path from the intiail state of a search problem to the goal state in the state space
	- in planning and robotics, the path from the intitial state to the goal state is also called a plan
	- it represents a sequence of actions to be taken to achieve the goal
	- **Plan**- the different nodes for the state that are used to reach the goal from the initial

## Blind Search (breadth-first, depth-first, depth-first with depth limit)
- **Breadth-first search**-
	- explores the state space lebel-by-level
	- only when no more states to be explored at a given level it moves on to the next level
	- goes by the levels of the tree, may take a while to get to the bottom of a singular branch if they are all long as it has to clear every parent node off that level
	- does not maintain a list of states on the current path (however you can if path is required by storing ancestor information along with each state)
		- so much rapid changing of branches as need to get all off the level
	- can construct solution by tracing back along the parents from the goal state to the start state
	- all nodes at level *n* are examinded before proceeding to level *n +1* , if it finds a solution then it is a **guaranteed to be shortest path to the goal**
	- **GUaranteed shortest path** - if there are several solutions its gauarnteed to find shortest solution first
		- good for problems where its known that a simple solution exists
	- if bad branching factor (average number of descendents per node) cam soon lead to an explosion of states that need to be kept in memory (exponential function of path length at any time)
	- if each state has an average of B children, then nu mnber of states oin a given level is B times the number of states on previous level *Bn* states on level *n*
		- because each child will have a parent and then have multiple children as well
	- if all Open list, then combinatorially explosive nature of the space may prevent finding a soltuion
	- Space Complexity makes it impractical for large problems
- **Depth-first search**- 