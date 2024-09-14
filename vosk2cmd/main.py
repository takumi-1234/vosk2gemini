import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from vosk2cmd.Command import Command
from vosk2cmd.Logger import Logger
from vosk2cmd.config import *


class CustomNode(Node):

    def __init__(self):
        super().__init__(NodeName)
        self.sub = self.create_subscription(String, SubscriberName, self.callback, 10)
        self.pub = self.create_publisher(String, PublisherName, 10)


    def publish_cmd(self, cmd):
        """
        publish current command every second
        """
        msg = String()
        msg.data = cmd
        self.pub.publish(msg)

        if Verbose: Logger.success(f'({ PublisherName }) Published: { msg.data }')


    def callback(self, data):
        msg = data.data
        if Verbose: Logger.info(msg)

        if 'stop' in msg:
            self.publish_cmd(Command.STOP)
        elif 'turn left' in msg:
            self.publish_cmd(Command.TURN_LEFT)
        elif 'turn right' in msg:
            self.publish_cmd(Command.TURN_RIGHT)
        elif 'go left' in msg:
            self.publish_cmd(Command.GO_LEFT)
        elif 'go right' in msg:
            self.publish_cmd(Command.GO_RIGHT)
        elif 'go forward' in msg:
            self.publish_cmd(Command.GO_FORWARD)
        elif 'go backward' in msg:
            self.publish_cmd(Command.GO_BACKWARD)


def main(args=None):
    rclpy.init(args=args)

    node = CustomNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()