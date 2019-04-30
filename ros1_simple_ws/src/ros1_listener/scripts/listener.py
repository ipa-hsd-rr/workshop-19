#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(message):
    rospy.loginfo( "ROS_1 listener listening to %s", message.data)
    
def listener():
    rospy.init_node('listener_ros1')
    rospy.Subscriber("ros1_topic", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()