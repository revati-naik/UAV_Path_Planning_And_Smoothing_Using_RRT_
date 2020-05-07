from __future__ import division
import os
import cv2
import sys
import copy
import numpy as np
sys.dont_write_bytecode = True

# import rrt


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



# def testMain():
# 	pass


# if __name__ == '__main__':
# 	testMain()