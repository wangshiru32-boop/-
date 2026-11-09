from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node


class TurtleCtrlNode(Node):

    def __init__(self):
        super().__init__('turtle_ctrl_node')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(0.5, self.publish_cmd_vel)

    def publish_cmd_vel(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Sending cmd_vel: linear.x={msg.linear.x}, angular.z={msg.angular.z}')


def main(args=None):
    rclpy.init(args=args)
    node = TurtleCtrlNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
