import sys
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import matplotlib.pyplot as plt


def withinObstacleSpace(point, radius, clearance):

    x = point[0]
    y = point[1]

    flag = False 
    point = Point(x, y)

    # creating rectangles
    rectangle_1 = Polygon([(-4.75, -0.75), (-3.25, -0.75), (-3.25, 0.75), (-4.75, 0.75)])
    rectangle_2 = Polygon([(-2.75, 2.25), (-1.25, 2.25), (-1.25, 3.75), (-2.75, 3.75)])
    rectangle_3 = Polygon([(4.75, -0.75), (3.25, -0.75), (3.25, 0.75), (4.75, 0.75)])

    if point.distance(rectangle_1) <= radius + clearance:
        flag = True 

    if point.distance(rectangle_2) <= radius + clearance:
        flag = True 

    if point.distance(rectangle_3) <= radius + clearance:
        flag = True 

    # creating circles
    p1 = Point(0, 0)
    circle_1 = p1.buffer(1.0)
    p2 = Point(-2, -3)
    circle_2 = p2.buffer(1.0)
    p3 = Point(2, -3)
    circle_3 = p3.buffer(1.0)
    p4 = Point(2, 3)
    circle_4 = p4.buffer(1.0)

    if point.distance(circle_1) <= radius + clearance:
        flag = True
    if point.distance(circle_2) <= radius + clearance:
        flag = True
    if point.distance(circle_3) <= radius + clearance:
        flag = True
    if point.distance(circle_4) <= radius + clearance:
        flag = True

    return flag


def withinObstacleSpaceFake((x, y), radius, clearance):
    """
    Always returns False. Only used for debugging purposes.

    :param      (x,y)):     Point to be checked
    :type       (x,y)):     tuple of (x,y) coordinates
    :param      radius:     The robot radius
    :type       radius:     float
    :param      clearance:  The robot clearance from objects
    :type       clearance:  float
    :param      plotter:    The plotter for visualization
    :type       plotter:    matplotlib.pyplot

    :returns:   Always False
    :rtype:     boolean
    """
    return False


def generateMap(plotter=plt):
    """
    Genarting the map for the obstacle space

    :param      plotter:  The plotter
    :type       plotter:  matplotlib.pyplot
    """
    circle_1 = plt.Circle((0, 0), 1, color='b')
    circle_2 = plt.Circle((-2, -3), 1, color='b')
    circle_3 = plt.Circle((2, -3), 1, color='b')
    circle_4 = plt.Circle((2, 3), 1, color='b')

    rectangle_1 = plt.Polygon([(-4.75, -0.75), (-3.25, -0.75), (-3.25, 0.75), (-4.75, 0.75)])
    rectangle_2 = plt.Polygon([(-2.75, 2.25), (-1.25, 2.25), (-1.25, 3.75), (-2.75, 3.75)])
    rectangle_3 = plt.Polygon([(4.75, -0.75), (3.25, -0.75), (3.25, 0.75), (4.75, 0.75)])

    plotter.add_artist(circle_1)
    plotter.add_artist(circle_2)
    plotter.add_artist(circle_3)
    plotter.add_artist(circle_4)
    plotter.add_line(rectangle_1)
    plotter.add_line(rectangle_2)
    plotter.add_line(rectangle_3)


def testMain():
    # x = float(sys.argv[1])
    # y = float(sys.argv[2])

    fig, ax = plt.subplots()
    ax.set(xlim=(-5, 5), ylim=(-5, 5))
    ax.set_aspect('equal')
    # ax.plot([x], [y], color="black", marker="+", markersize=3)

    # print(withinObstacleSpace((x, y), 0.105, 0.2, plotter=ax))
    generateMap(ax)

    plt.show()


if __name__ == '__main__':
    testMain()
