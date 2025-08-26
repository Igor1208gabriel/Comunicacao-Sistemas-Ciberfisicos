import sys
from rclpy.node import Node
import rclpy
from std_msgs.msg import String


class Publisher(Node):

    def __init__(self, TopicName="topico"):
        super().__init__("subscriber_simples")
        self.sub = self.create_subscription(String, TopicName, self.Hear, 10)
        self.sub

    def Hear(self, message):
        self.get_logger().info(f"I Heard: {message.data}")


def main():
    rclpy.init()
    if len(sys.argv) == 1:
        node = Publisher()
    elif len(sys.argv) == 2:
        node = Publisher(sys.argv[1])
    else:
        print("Usage: my_node.py <topic>")
        exit()

    rclpy.spin(node)


if __name__ == "__main__":
    main()
