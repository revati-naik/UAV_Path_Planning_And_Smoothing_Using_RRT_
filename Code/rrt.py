import numpy as np 
import random 
import heapq
import matplotlib.pyplot as plt
import math

import node 
import obstacles
import utils 
import univ
import path_pruning


import sys
sys.dont_write_bytecode = True

X_LIM = (-5,5)
Y_LIM = (-5,5)

MAX_ITER = 50000
STEP_SIZE = 0.1
GOAL_REACH_THRESH = 0.1	

def rrt(start_coords, goal_coords, radius, clearance):

	x_start, y_start = start_coords
	x_goal, y_goal = goal_coords

	start_node = node.Node(current_coords=start_coords, parent_coords=None, distance=None)
	goal_node = node.Node(current_coords=goal_coords, parent_coords=None, distance=None)

	print(start_node.printNode())
	print(goal_node.printNode())

	tree = []
	path = []

	# tree.append(start_node)
	tree.append([0, start_node.current_coords, (0,0)])


	N = 0
	while(N<MAX_ITER):
		print("N:", N)
		x_random = (np.random.uniform(X_LIM[0],X_LIM[1]), np.random.uniform(Y_LIM[0],Y_LIM[1]))
		# print("x_random", x_random)
	    ##########################################
	    #put a check if x_random is repeated
	    ##########################################
		# print("<<<<<<<<<<<<Before updating the distance<<<<")
		# print("tree", tree)

		# print("<<<<<<<<<<<<After updating the distance<<<<<")
		for i in tree:
		# while True:
			distance = utils.euclideanDistance(point_1=i[1], point_2=x_random)
			i[0] = distance
			# print("tree", i)

		heapq.heapify(tree)

		# Finding the node in the tree which is the nearest to the x_random
		min_node = heapq.heappop(tree)


		# print("len(tree)", len(tree))
		heapq.heappush(tree, [min_node[0], min_node[1], min_node[2]])
		# sys.exit(0)

		# print("min node", min_node)
		# print("next_node", next_node)
		# print("distance", distance)
		# path.append(add_node)
		# tree.append([min_node[0], x_random, min_node[1]])
		# print("<<<<<<<<<<<After apending the latest x random<<<<<")
		# print("tree", tree)

		# if the random node is within the step size
		if min_node[0] <= STEP_SIZE:

			# create a node with this value and add it to the path 
			obstacle_status = obstacles.withinObstacleSpace(point=min_node[1], radius=radius, clearance=clearance)
			if (obstacle_status == False):
				add_node = node.Node(current_coords=x_random, parent_coords=min_node[1], distance=min_node[0])
				path.append(add_node)
				# print("<<<<<<<<<<<<<_before<<<<<<<<<,")
				# print("len(tree)", len(tree))
				heapq.heappush(tree,[add_node.distance, add_node.current_coords, add_node.parent_coords])
				# print("<<<<<<<<<<<<after<<<<<<<<<<,")
				# print("len(tree)", len(tree))
				# tree.append([add_node.distance, add_node.current_coords, add_node.parent_coords])

		else:
			# Find an intermediate point in between a and b
			x1, y1 = min_node[1]
			x2, y2 = x_random

			slope = (y2 - y1) / (x2 - x1)
			theta = math.atan(slope)

			x_near = (x1 + (STEP_SIZE * math.cos(theta)), y1 + (STEP_SIZE * math.sin(theta)))

			obstacle_status = obstacles.withinObstacleSpace(point=min_node[1], radius=radius, clearance=clearance)
			if (obstacle_status == False):
				add_node = node.Node(current_coords=x_near, parent_coords=min_node[1], distance=STEP_SIZE)
				# print("<<<<<<<<<<<<<_before<<<<<<<<<,")
				# print("len(tree)", len(tree))
				path.append(add_node)
				heapq.heappush(tree,[add_node.distance, add_node.current_coords, add_node.parent_coords])
				# print("<<<<<<<<<<<<<_before<<<<<<<<<,")
				# print("len(tree)", len(tree))
				
				# tree.append([add_node.distance, add_node.current_coords, add_node.parent_coords])



		goal_status = utils.goal_reached(current_node=add_node, goal_node=goal_node, goal_reach_threshold=GOAL_REACH_THRESH)
		if (goal_status):
			print("Reached Goal!")
			return path, goal_node
			# break


		
		N += 1
		# print("-------------------")
		# print(path)
	return path, goal_node



def testMain():

	x_start, y_start = (-4,-4)
	x_goal, y_goal = (0,-4)
	start_coords = (x_start, y_start)
	goal_coords = (x_goal, y_goal)
	radius = 0.1
	clearance = 0.1

	path, goal_node = rrt(start_coords=start_coords, goal_coords=goal_coords, radius=radius, clearance=clearance)
	# print(path)
	# np.save("../Paths/path.npy", path)
	# np.save("./path.npy", path)
	# sys.exit(0)

	univ.function(exploration_node_vector=path, goal_node=goal_node, path_node_vector=None, step_size=None)
	path_pruning.prunedPath(path=path, goal_node=goal_node)

if __name__ == '__main__':
	testMain()
