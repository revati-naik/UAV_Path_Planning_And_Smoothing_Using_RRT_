from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
import node
import sys


def function(exploration_node_vector, goal_node, path_node_vector=None, step_size=None):

	fig, ax = plt.subplots()
	ax.set(xlim=(-5, 5), ylim=(-5, 5))
	ax.set_aspect('equal')

	circle_1 = plt.Circle((0, 0), 1, color='b')
	circle_2 = plt.Circle((-2, -3), 1, color='b')
	circle_3 = plt.Circle((2, -3), 1, color='b')
	circle_4 = plt.Circle((2, 3), 1, color='b')

	rectangle_1 = plt.Polygon([(-4.75, -0.75), (-3.25, -0.75), (-3.25, 0.75), (-4.75, 0.75)])
	rectangle_2 = plt.Polygon([(-2.75, 2.25), (-1.25, 2.25), (-1.25, 3.75), (-2.75, 3.75)])
	rectangle_3 = plt.Polygon([(4.75, -0.75), (3.25, -0.75), (3.25, 0.75), (4.75, 0.75)])

	ax.add_artist(circle_1)
	ax.add_artist(circle_2)
	ax.add_artist(circle_3)
	ax.add_artist(circle_4)
	ax.add_line(rectangle_1)
	ax.add_line(rectangle_2)
	ax.add_line(rectangle_3)

	# Adding the start node
	xs, ys = exploration_node_vector[0].getXYCoords()
	plt.plot(xs, ys, color='#EE82EE', marker='o', markersize=5)

	# Adding the goal node
	# xg, yg = path_node_vector[-1].getXYCoords()
	xg, yg = goal_node.getXYCoords()
	plt.plot(xg, yg, color='#7CFC00', marker='o', markersize=5)

	colors = ['red', 'pink', 'green', 'yellow']
	color_i = 0

	plt.ion()
	for node in exploration_node_vector:
		plt.gca().set_aspect('equal')
		plt.xlim(-5, 5)
		plt.ylim(-5, 5)
	
		plt.minorticks_on()
		plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
		plt.grid(which='minor', color='black')
		plt.title('Vector plot', fontsize=25)

		xy = node.getParentXYCoords()
		uv = node.getXYCoords()
		if xy is None or uv is None:
			continue

		x,y = xy
		u,v = uv
		u -= x
		v -= y
		# q = plt.quiver(x, y, u, v, units='xy', scale=1, width=1.5, headwidth=2, headlength=2, color=colors[color_i%len(colors)])
		q = plt.quiver(x, y, u, v, units='xy', scale=1, width=0.1, headwidth=0.1, headlength=0.1, color=colors[color_i%len(colors)])

		# plt.plot(x, y, 'rqo')	

		color_i += 1

		plt.show()
		plt.pause(0.1)
		# plt.ioff()
		# sys.exit(0)


	# for node in path_node_vector[:-1]:
	# 	plt.gca().set_aspect('equal')
	# 	plt.xlim(0, 300)
	# 	plt.ylim(0, 200)
	
	# 	plt.minorticks_on()
	# 	plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
	# 	plt.grid(which='minor', color='black')
	# 	plt.title('Vector plot', fontsize=25)

	# 	xy = node.getParentXYCoords()
	# 	uv = node.getXYCoords()
	# 	if xy is None or uv is None:
	# 		continue

	# 	x,y = xy
	# 	u,v = uv
	# 	u -= x
	# 	v -= y
	# 	q = plt.quiver(x, y, u, v, units='xy', scale=1, width=1.5, headwidth=2, headlength=2, color="black")

	# 	plt.show()
	# 	plt.pause(0.01)
	# plt.ioff()
	
	# plt.gca().set_aspect('equal')
	# plt.xlim(0, 300)
	# plt.ylim(0, 200)

	# plt.minorticks_on()
	# plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
	# plt.grid(which='minor', color='black')
	# plt.title('Vector plot', fontsize=25)

	# xy = path_node_vector[-1].getParentXYCoords()
	# uv = path_node_vector[-1].getXYCoords()
	# if xy is not None and uv is not None:
	# 	x,y = xy
	# 	u,v = uv
	# 	u -= x
	# 	v -= y
	# 	q = plt.quiver(x, y, u, v, units='xy', scale=1, width=1.5, headwidth=2, headlength=2, color="black")

	# plt.show()
