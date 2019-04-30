#!/usr/bin/python
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('ros1_topic', String, queue_size=10)
    rospy.init_node('talker_ros1')
    rate = rospy.Rate(10)
    i = 0
    while not rospy.is_shutdown():
        i += 1
        message = 'ROS_1 talker %d' % i
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


			