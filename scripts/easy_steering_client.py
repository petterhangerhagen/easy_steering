#!/usr/bin/env python2

import rospy
import time

from ros_clients.msg import GeneralizedForce
from read_from_file import read_from_file

def callback(force):
	ctrl_pub = rospy.Publisher('force_control', GeneralizedForce, queue_size=10)

	force_output = GeneralizedForce(
        	x = force[0],
        	y = 0,
        	z = 0,
        	k = 0,
        	m = 0,
        	n = force[1]
	)
	ctrl_pub.publish(force_output)

def listener():
	while(True):
		time.sleep(5)
		force = read_from_file()
		callback(force)		

if __name__ == '__main__':
	rospy.init_node('easy_steering_node', anonymous=True)
	listener()



