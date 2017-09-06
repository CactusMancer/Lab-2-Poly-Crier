#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + ": I heard %s.", msg.data)

rospy.init_node("poly_Listener")

sub = rospy.Subscriber("names",String,callback)

rospy.spin()
