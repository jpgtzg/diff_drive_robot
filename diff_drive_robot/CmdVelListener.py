# Written by Juan Pablo Gutiérrez
# 29 05 2025

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class CmdVelListener(Node):
    def __init__(self):
        super().__init__('cmd_vel_listener')
        self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)
        self.get_logger().info('CmdVelListener has been started.')

    def cmd_vel_callback(self, msg : Twist):
        self.get_logger().info('Received a message: \n Linear: \n x = {} \n y = {} \n z = {} \n\n Angular: \n x = {} \n y = {} \n z = {}'.format(msg.linear.x , msg.linear.y, msg.linear.z, msg.angular.x, msg.angular.y, msg.angular.z))
        
def main(args=None):
    rclpy.init(args=args)

    cmdvel_listener = CmdVelListener()

    rclpy.spin(cmdvel_listener)

    cmdvel_listener.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
