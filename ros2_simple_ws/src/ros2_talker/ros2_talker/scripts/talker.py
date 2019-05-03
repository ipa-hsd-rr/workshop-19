#!/usr/bin/python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ros2_talker(Node):
    def __init__(self):
        super().__init__('ros2_talker')
        self.i = 0
        self.pub = self.create_publisher(String, 'subject_topic')
        timer_period = 0.1        #Set the publishing rate
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        message = String()
        self.i += 1
        message.data = 'ROS_2 talker talking %d'% self.i
        self.get_logger().info(message.data)
        self.pub.publish(message) 


def main():
    rclpy.init()
    node = ros2_talker()         #create node
    rclpy.spin(node)
    node.destroy_node()     #destructor
    rclpy.shutdown()        #shutdown node


if __name__ == '__main__':
    main()
