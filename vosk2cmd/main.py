import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from vosk2cmd.Command import Command
from vosk2cmd.Logger import Logger
from vosk2cmd.config import *

import google.generativeai as genai
import os

# Google Generative AIの設定
os.environ["API_KEY"] = 'AIzaSyA-U5pwi5Zu9p4qyk6hwBI3mzYsIA9WzIw'
genai.configure(api_key=os.environ["API_KEY"])
gemini_pro = genai.GenerativeModel("gemini-pro")

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
        # 半角の空白で単語数の判別を実施しているので日本語の場合は変更の必要あり
        elif msg.count(" ") > 5:
            # トピックから受け取ったメッセージを取得
            prompt = msg
            self.get_logger().info(f'Received message: "{prompt}"')

            # Google Geminiにプロンプトとして送信
            try:
                response = gemini_pro.generate_content(prompt)
                print("AI Response:", response.text)
            except Exception as e:
                print(f"Failed to get response from AI: {e}")


def main(args=None):
    rclpy.init(args=args)

    node = CustomNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()