#!/usr/bin/python
import rclpy
import rclpy.logging
from std_msgs.msg import String
from time import sleep

def talker():
    rclpy.init()
    node = rclpy.create_node('talker_ros2')
    pub = node.create_publisher(String, 'ros2_topic')
    message = String()
    i = 0
    while rclpy.ok():
        i += 1
        message.data = 'ROS_2 talker talking %d'% i
        print(message.data)
        pub.publish(message)
        sleep(1)

if __name__ == '__main__':
    talker()
   
