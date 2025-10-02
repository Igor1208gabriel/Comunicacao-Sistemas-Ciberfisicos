from rclpy.node import Node
import rclpy
from std_msgs.msg import String
import sys


class Confuso(Node):

    def __init__(
        self,
        TopicName="topico",
        TimerPeriod=1,
    ):
        super().__init__("Confuso_simples")
        self.num = 0
        self.pub = self.create_publisher(String, TopicName, 10)
        self.sub = self.create_subscription(String, TopicName, self.Hear, 10)

        self.sub
        self.create_timer(timer_period_sec=float(TimerPeriod), callback=self.Callback)

    def Hear(self, message):
        self.get_logger().info(f"I Heard: {message.data}")

    def Callback(self):
        Message = self.num
        ToSend = String()
        if Message:
            ToSend.data = Message
            self.get_logger().info(f"I Published: {Message}")
            self.pub.publish(ToSend)
            self.num += 1


def main():
    rclpy.init()
    node = Confuso()
    rclpy.spin(node)


if __name__ == "__main__":
    main()
