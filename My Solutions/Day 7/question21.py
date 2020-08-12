# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
# with a given steps. The trace of robot movement is shown as the following:
#
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after
# a sequence of movement and original point. If the distance is a float, then just print the nearest integer.

from math import sqrt

location = [0, 0]


def movement_side():
    try:
        location[1] += int(input('UP '))
        location[1] -= int(input('DOWN '))
    except TypeError:
        print('Please input a valid number')


def movement_up():
    try:
        location[0] += int(input('RIGHT '))
        location[0] -= int(input('LEFT '))
    except TypeError:
        print('Please input a valid number')


movement_up()
movement_side()

distance_traveled = round(sqrt((location[0] ** 2) + (location[1] ** 2)))
print(distance_traveled)
