#!/usr/bin/env python2

import rospy
import time

from ros_clients.msg import GeneralizedForce
from read_from_file import read_from_file

def callback(force):
	ctrl_pub = rospy.Publisher('force_control', GeneralizedForce, queue_size=10)

	force_output = GeneralizedForce(
        	x = force[1],
        	y = 0,
        	z = 0,
        	k = 0,
        	m = 0,
        	n = force[2]
	)
	ctrl_pub.publish(force_output)

def listener():
	force = read_from_file()
	while(force[0] == "run"):
		time.sleep(5)
		force = read_from_file()
		callback(force)	
def listener():
	while(True):
		time.sleep(5)  # making the while-loop run every 5 seconds
		force = read_from_file() 
		# reading from forces.txt where the first line indicate run, stop or error, 
		# the second line indicate the force in x-direction and
		# the third line indicate the rotation force, which makes the vessel turn
		if (force[0] != 'run'):
			if (force[0] == 'stop'):
				force = ['stop',0,0]
			else:
				print("Error")
				break
		callback(force)
		print(force)		

if __name__ == '__main__':
	rospy.init_node('easy_steering_node', anonymous=True)
	listener()



