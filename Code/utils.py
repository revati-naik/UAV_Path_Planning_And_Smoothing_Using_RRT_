from __future__ import division
import os
import cv2
import sys
import copy
import numpy as np
sys.dont_write_bytecode = True

import rrt


def euclideanDistance(point_1, point_2):
	"""
	To find the euclidean distance between two coordinates. 
	Used in the A_star algorithm.

	:param      point_1:  The state 1
	:type       point_1:  tuple
	:param      point_2:  The state 2
	:type       point_2:  tuple

	:returns:   Euclidean distance between the two states
	:rtype:     float
	"""
	return np.sqrt(((point_1[0] - point_2[0]) ** 2) + ((point_1[1] - point_2[1]) ** 2))

def goal_reached(current_node, goal_node, goal_reach_threshold):

	more_to_reach = euclideanDistance(current_node.current_coords, goal_node.current_coords)
	print("more_to_reach", more_to_reach)

	if more_to_reach <= goal_reach_threshold:
		return True
	else:
		return False



# def findInHeap(node, node_list):
# 	"""
# 	Finds a node in heap based on only the current coordinate values.

# 	:param      node:       The node to be searched
# 	:type       node:       Node
# 	:param      node_list:  The search space
# 	:type       node_list:  list of Nodes

# 	:returns:   index position of where the node is found (-1 if not found)
# 	:rtype:     int
# 	"""
# 	node_list_coords = [item[1].current_coords for item in node_list]
# 	if node.current_coords in node_list_coords:
# 		return node_list_coords.index(node.current_coords)
# 	return -1


# def orientationBin(angle, bin_size):
# 	"""
# 	Returns the bin for the given angle

# 	:param      angle:     The angle
# 	:type       angle:     float
# 	:param      bin_size:  The bin size
# 	:type       bin_size:  float

# 	:returns:   The bin to which the angle belongs in the visited dictionary
# 	:rtype:     float
# 	"""
# 	return (((angle % 360) // bin_size) * bin_size)


# def getKey(x, y, theta):
# 	"""
# 	Gets the key for the given tuple

# 	:param      x:      X - coordinate
# 	:type       x:      number
# 	:param      y:      Y - coordinate
# 	:type       y:      number
# 	:param      theta:  The orientation
# 	:type       theta:  number

# 	:returns:   The key.
# 	:rtype:     tuple
# 	"""
# 	x_new = int(np.floor(x*10))/10
# 	y_new = int(np.floor(y*10))/10
# 	t_bin = orientationBin(theta, a_star.THETA_BIN_SIZE)

# 	return ((x_new, y_new, t_bin))



# def testMain():
# 	pass


# if __name__ == '__main__':
# 	testMain()