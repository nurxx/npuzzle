from math import sqrt

global N

class Node:
	'''
	Class Node holding the state of the puzzle, possible movement/direction, parent node,
	g(n) - the depth and f(n) the total estimated cost of the state
	'''

	def __init__(self, state, direction, parent, g_n, f_n):
		self.state = state
		self.direction = direction
		self.parent = parent
		self.g_n = g_n
		self.f_n = f_n


def heuristic(node, goal):
	manhattan_distance = 0
	for i in range(len(node.state)):
		for j in range(len(node.state)):
			if node.state[i][j] != 0:
				x , y = get_value_index(goal, node.state[i][j])[0]
				manhattan_distance += abs(i - x) + abs(j - y)

	return manhattan_distance

    
def idastar(initial_node, goal_state):
	threshold = heuristic(initial_node, goal_state)

	while True:
		result = search(initial_node, goal_state, threshold)

		if isinstance(result, int):
			threshold = result
		else:
			return result
			break


# Pseudocode credit: https://en.wikipedia.org/wiki/Iterative_deepening_A*
def search(current_node, goal_state, threshold):
	visited = []  # Store visited states
	total_cost = set()  # Set of values for the distance between the current node and start node
	stack = list([Node(current_node.state, None, None, 0, threshold)])

	while stack:
		node = stack.pop()
		visited.append(node.state)
		# Check if a goal state
		if node.state == goal_state:
			goal_node = node
			return goal_node

		if node.f_n > threshold:
			total_cost.add(node.f_n)
		else:
			children = get_possible_movements(node)

			for child in children:
				if child.state not in visited:
					h_n = heuristic(child, goal_state) 
					child.f_n = h_n + child.g_n
					stack.append(child)  
					visited.append(child.state) 

	return min(total_cost) 

def get_value_index(state, value):
	return [(index, row.index(value)) for index, row in enumerate(state) if value in row]

def get_moved_state(state, row, col, x, y):
	new_state = []
	for id, s in enumerate(state):
		new_state.append(list(s))
		
	zero_value = new_state[row][col] 
	new_state[row][col] = new_state[x][y]
	new_state[x][y] = zero_value

	return new_state


# Get node children
def get_possible_movements(node):
	node_children = list() 
	row, col = get_value_index(node.state, 0)[0]
	if row > 0:
		move_up = get_moved_state(node.state, row, col, row - 1, col)
		node_children.append(Node(move_up, 'up', node, node.g_n + 1, 0 ))
		
	if row < len(node.state) - 1:
		move_down = get_moved_state(node.state, row, col, row + 1, col)
		node_children.append(Node(move_down, 'down', node, node.g_n + 1, 0 ))
		
	if col > 0:
		move_left = get_moved_state(node.state, row, col, row, col - 1)
		node_children.append(Node(move_left, 'left', node, node.g_n + 1, 0 ))

	if col < len(node.state) - 1:
		move_right = get_moved_state(node.state, row, col, row, col + 1)
		node_children.append(Node(move_right, 'right', node, node.g_n + 1, 0 ))

	return node_children
    
def get_path_to_goal(initial, goal):
	moves = list()
	# Map used to swap the values for Up <-> Down, Left <-> Right
	map_moves = {
		"up": "down",
		"down": "up",
		"left": "right",
		"right": "left"
	}
 
	node = goal # starting from goal and back to the root to find the path

	while initial != node.state:
		moves.insert(0, map_moves[node.direction])	
		node = node.parent
		
	return moves

    
def generate_goal_state(n):
	goal_zero_index = int(input(""))
	goal_state = list(range(1,n+1))
	if goal_zero_index == -1:
		goal_state.insert(n, 0)
	else:
		goal_state.insert(goal_zero_index, 0)

	step = int(sqrt(n+1))
	goal_state = [goal_state[i:i+step] for i in range(0, len(goal_state), step)]
	return goal_state
    

def get_user_input():
	N = int(input(""))
	goal_state = generate_goal_state(N)
	rows = cols = int(sqrt(N + 1))
	initial_state = []
	for i in range(rows):
		row = list(map(int, input().split()))
		initial_state.append(row)
    
	return N, initial_state, goal_state

def print_state(state):
	for row in range(len(state)):
		for col in range(len(state)):
			print(state[row][col], end = " ")
		print()
    
    
def main():
    # Assuming that the puzzle is solveable
	N, initial_state, goal_state = get_user_input()

	print("\n----- Initial state -----\n")
	print_state(initial_state)

	print("\n----- Goal state -----\n")
	print_state(goal_state)
  
	initial_node = Node(initial_state, None, None, 0, 0)
	goal_node = idastar(initial_node, goal_state)
	moves = get_path_to_goal(initial_state, goal_node)
	print("\n----- Moves -----\n")
	print("\n")
	print(len(moves))
	print(*moves, sep = "\n")

if __name__ == '__main__':
	main()
