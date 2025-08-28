from rclpy.node import Node
import rclpy
from std_msgs.msg import String
import sys

class Publisher(Node):

    def __init__(self, TopicName="topico", Message="O Igor é lindo e muito inteligente", TimerPeriod=1):
        super().__init__("publisher_simples")
        # self.get_logger().info(f"{TopicName} - {Message} - {TimerPeriod}")
        self.message = Message
        self.num = 0
        self.pub = self.create_publisher(String, TopicName, 10)
        self.create_timer(
            timer_period_sec=float(TimerPeriod), callback=self.Callback
        )

    def Callback(self):
        Message = self.message
        ToSend = String()
        if Message:
            ToSend.data = Message
            self.pub.publish(ToSend)
            self.get_logger().info(f"Enviei mensagem {self.num} - {Message}")
            self.num += 1


def main():
    rclpy.init()
    if len(sys.argv) == 1:
        node = Publisher()
    elif len(sys.argv) == 4:
        node = Publisher(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: my_node.py <topic> <message> <period>")
        exit()

    rclpy.spin(node)

if __name__ == "__main__":
    main()