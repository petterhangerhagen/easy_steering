#!/usr/bin/env python2

import rospy

filename = "/home/petter/catkin_ws/src/easy_steering/scripts/forces.txt"

def read_from_file():
    f = open(filename, "r")
    force = []
    temp = f.readlines()
    for i in range(3):
        temp[i] = temp[i][:-1]
    force.append((temp[0]))
    force.append(int(temp[1]))
    force.append(int(temp[2]))
    return force





