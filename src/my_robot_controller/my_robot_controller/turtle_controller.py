#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class TurtleControllerNode(Node):
    
    def __init__(self):
        super().__init__("turtle_controller")
        self.cmd_vel_publisher_ = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10)
        self.pose_subscriber_ = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10)
        
        self.get_logger().info("Turtle controller has been started.")

    def pose_callback(self, pose: Pose):
        cmd = Twist()
        
        l = 4.0
        a = 0.0

        if pose.x > 9.0:
            l = 1.0
            a = 1.2
        elif pose.x < 2.0:
            l = 1.0
            a = 1.2
        else:
            l = 4.0
            a = 0.0
    
        if pose.y < 2.0:
            l = 1.0
            a = 1.3
        elif pose.y > 9.0:
            l = 1.0
            a = 1.3
        cmd.linear.x = l
        cmd.angular.z = a

        self.cmd_vel_publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
