import numpy as np 
import copy
import sys

import node
import obstacles

pruned_path = []




def prunedPath(path, goal_node):
	path_length = len(path)
	j = path_length -1

	# Add the last node
	pruned_path.append(path[j])
	# print(pruned_path)
	# print(pruned_path[0].current_coords)

	# for j in range(0,)
	while (j!= 0):
		i = 0
		for i in range(0,j):
			# print(path[i].current_coords)
			# x1, y1 = path[i].current_coords
			# x2, y2 = path[j-1].current_coords
			x1, y1 = path[j]
			x2, y2 = path[i]
			print("x1, y1: ", x1, y1)
			print("x2, y2: ", x2, y2)
			status = isObstacleLine(np.array([x2, y2]), np.array([x1, y1]))
			print("status: ", status)
			if (status ==  False):
				print("i: ", i)
				pruned_path.append(path[i])
				j = copy.copy(i)
				print("j: ", j)

				if j == 0:
					break
	print("pruned_path: ", pruned_path)
	print("len(pruned_path): ", len(pruned_path))


def isObstacleLine(start, end):
	pts = np.linspace(0,1,num=100)
	obs = []

	for t in pts:

		eqn = t*start + (1-t)*end
		# print(eqn)
		obs.append(obstacles.withinObstacleSpace(point=eqn, radius=0, clearance=0))
	
	obs=np.array(obs)
	if np.any(obs):
		return True
	else:
		return False




def testMain():
	path = np.load('./path.npy', allow_pickle=True)
	# print(len(path))
	# path_new = [[-4,-4],[-2, -4], [0,-4], [0, -3]]
	# path_new = [[-4,-3],[-3,-4], [-2,-4.5], [-0.5,-4], [0,-2]]
	prunedPath(path=path, goal_node=path[-1].current_coords)
	

	# val = isObstacleLine(np.array([-0.5,-3]), np.array([-2,-4.2]))
	# print(val)
	# sys.exit(0)



if __name__ == '__main__':
	testMain()