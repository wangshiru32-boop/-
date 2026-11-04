import rclpy
from rclpy.node import Node


class MySecondNode(Node):

    def __init__(self):
        super().__init__('my_second_node')
        self.get_logger().info('Hi from my_package (my_second_node).')


def main(args=None):
    rclpy.init(args=args)
    node = MySecondNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
