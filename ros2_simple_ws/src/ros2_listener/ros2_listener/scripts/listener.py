#!/usr/bin/python
# -*- coding: utf-8 -*-

import rclpy
from std_msgs.msg import String


def callback(message):
    print( "ROS_2 listener listening to %s"% message.data)

def listener():
    rclpy.init()
    node = rclpy.create_node('ros2_listener')
    sub = node.create_subscription(String, 'ros2_topic',callback)
    while rclpy.ok():
        rclpy.spin_once(node)

if __name__ == '__main__':
    listener()


			