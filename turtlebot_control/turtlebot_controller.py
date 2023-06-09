import random

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class TurtlebotControl(Node):
    def __init__(self):
        super().__init__('turtlebot_controller')

        self.declare_parameter('speed', 1.0)
        self.declare_parameter('omega', 20.0)

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription_ = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        ranges = msg.ranges
        front_distance = ranges[0]
        front_right_distance = ranges[5]
        front_left_distance = ranges[-5]
        self.get_logger().info("Distance: " + str(front_distance))

        if front_distance < 1.8 or front_left_distance < 1.8 or front_right_distance < 1.8:  # Adjust this threshold based on the desired stopping distance
            self.avoid_robot()
        else:
            self.move_robot()

    def avoid_robot(self):
        new_msg = Twist()
        new_msg.linear.x = 0.1  # Set linear velocity to stop
        new_msg.angular.z = 0.3

        self.publisher_.publish(new_msg)
        self.get_logger().info("Avoiding object")

    def move_robot(self):
        new_msg = Twist()
        new_msg.linear.x = 0.1  # Set linear velocity
        new_msg.angular.z = 0.0  # Set angular velocity

        self.publisher_.publish(new_msg)

def main(args=None):
    rclpy.init(args=args)
    tc = TurtlebotControl()
    rclpy.spin(tc)
    tc.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
