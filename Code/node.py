import sys
sys.dont_write_bytecode = True

class Node(object):

	def __init__(self,
				current_coords,
				parent_coords,
				distance):

		self.current_coords = current_coords
		self.parent_coords = parent_coords
		self.distance = distance

	def getXYCoords(self):
		if self.current_coords is not None:
			return (self.current_coords[0], self.current_coords[1])
		return None


	def getParentXYCoords(self):
		if self.parent_coords is not None:
			return (self.parent_coords[0], self.parent_coords[1])
		return None

	def printNode(self):
		print "Current_Coords:\t", self.current_coords
		print "Parent_Coords:\t", self.parent_coords
		print "Distance:\t", self.distance