#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from random import randint

names = ["Dean", "Jon", "Vamsi"]

rospy.init_node("poly_Chatter")

pub = rospy.Publisher("names",String)

rate = rospy.Rate(21)

while not rospy.is_shutdown():
    index = randint(0,2)
    pub.publish(names[index])
    rate.sleep()
