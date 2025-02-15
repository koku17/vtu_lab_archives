#!/bin/python

from collections import deque

# Define the jug capacities
jug1_capacity = 4
jug2_capacity = 3
target_volume = 2

# Initial state with both jugs empty
initial_state = (0,0)

# Function to check if a state is valid
def is_valid_state(state):
	jug1,jug2 = state
	return 0 <= jug1 <= jug1_capacity and 0 <= jug2 <= jug2_capacity

# Function to perform pour actions
def pour(from_jug,to_jug,state):
	jug1,jug2 = state
	if from_jug == 1 and jug1 > 0 and jug2 < jug2_capacity:
		amount_poured = min(jug1,jug2_capacity - jug2)
		new_jug1 = jug1 - amount_poured
		new_jug2 = jug2 + amount_poured
		return (new_jug1,new_jug2)
	elif jug2 > 0 and jug1 < jug1_capacity:
		amount_poured = min(jug2,jug1_capacity - jug1)
		new_jug1 = jug1 + amount_poured
		new_jug2 = jug2 - amount_poured
		return (new_jug1,new_jug2)
	return None

# Function to solve the water jug problem using depth-first search
def water_jug_dfs():
	visited = set()
	stack = deque()
	stack.append((initial_state,[])) # State and actions taken
	while stack:
		current_state,actions = stack.pop()
		if current_state[0] == target_volume or current_state[1] == target_volume:
			return actions
		visited.add(current_state)
		for action in [ \
			"Fill Jug 1","Fill Jug 2","Empty Jug 1","Empty Jug 2","Pour Jug 1 to Jug 2", \
			"Pour Jug 2 to Jug 1" \
		]:
			new_state = None
			if action == "Fill Jug 1":
				new_state = (jug1_capacity,current_state[1])
			elif action == "Fill Jug 2":
				new_state = (current_state[0],jug2_capacity)
			elif action == "Empty Jug 1":
				new_state = (0,current_state[1])
			elif action == "Empty Jug 2":
				new_state = (current_state[0],0)
			elif action == "Pour Jug 1 to Jug 2":
				new_state = pour(1,2,current_state)
			elif action == "Pour Jug 2 to Jug 1":
				new_state = pour(2,1,current_state)
			if new_state is not None and new_state not in visited:
				new_actions = actions + [action]
				stack.append((new_state,new_actions))
	return None

# Solve the water jug problem
solution = water_jug_dfs()
if solution:
	print("Solution Found:")
	for i,action in enumerate(solution,start=1):
		print(f"Step {i}: {action}")
else:
	print("No solution found")
