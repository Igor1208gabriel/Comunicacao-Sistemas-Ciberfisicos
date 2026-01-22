"Subscriber simples"
import sys
from rclpy.node import Node
import rclpy
from std_msgs.msg import String


class Publisher(Node):
    "Subscriber simples"

    def __init__(self, TopicName="topico"):
        super().__init__("subscriber_simples")
        self.sub = self.create_subscription(String, TopicName, self.hear, 10)

    def hear(self, message):
        "Publica mensagem que ouviu"
        self.get_logger().info(f"I Heard: {message.data}")


def main():
    "docstring"
    rclpy.init()
    if len(sys.argv) == 1:
        node = Publisher()
    elif len(sys.argv) == 2:
        node = Publisher(sys.argv[1])
    else:
        print("Usage: ros2 run <pkg> <node> <topic>")
        sys.exit()

    rclpy.spin(node)


if __name__ == "__main__":
    main()
