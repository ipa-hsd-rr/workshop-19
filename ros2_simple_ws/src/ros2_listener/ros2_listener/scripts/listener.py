#!/usr/bin/python

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ros2_listener(Node):
    def __init__(self):
        super().__init__('ros2_listener')
        self.sub = self.create_subscription(String, 'subject_topic', self.callback)

    def callback(self, message):
        self.get_logger().info( "ROS_2 listener listening to %s"% message.data)

def main():
    rclpy.init()
    node = ros2_listener()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
