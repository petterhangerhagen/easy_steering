#!/usr/bin/env python2

import rospy

from ros_clients.msg import GeneralizedForce

def callback():
	ctrl_pub = rospy.Publisher('force_control', GeneralizedForce, queue_size=10)

	force_output = GeneralizedForce(
        	x = -200,
        	y = 0,
        	z = 0,
        	k = 0,
        	m = 0,
        	n = 100
	)
	ctrl_pub.publish(force_output)

if __name__ == '__main__':
	rospy.init_node('easy_steering_node', anonymous=True)

	while(True):
		callback()
