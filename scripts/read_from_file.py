#!/usr/bin/env python2

import rospy

filename = "/home/petter/catkin_ws/src/easy_steering/scripts/forces.txt"

#filename = ('forces.txt')
def read_from_file():
    f = open(filename, "r")

    force = list()
    list1 = f.readlines()
    for i in range(len(list1)):
        size = len(list1[i])
        list1[i] = list1[i][:size - 1]
        force.append(int(list1[i]))
    print(force)
    return force
