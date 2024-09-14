import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from vosk2cmd.config import *


class CustomNode(Node):

    def __init__(self):
        super().__init__(NodeName)
        self.sub = self.create_subscription(String, SubscriberName, self.callback, 10)
        self.pub = self.create_publisher(String, PublisherName, 10)


    def callback(self, data):
        if 'left' in data.data:
            pass
        # .......

        msg = String()
        msg.data = "GO_LEFT"
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = CustomNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()