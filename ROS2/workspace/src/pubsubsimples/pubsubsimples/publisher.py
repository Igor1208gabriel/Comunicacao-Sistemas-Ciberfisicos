"Classe de Publisher simples"
import sys
from rclpy.node import Node
import rclpy
from std_msgs.msg import String


class Publisher(Node):
    "Classe de Publisher simples"

    def __init__(
        self,
        TopicName="topico",
        Message="O Igor é lindo e muito inteligente",
        TimerPeriod=1,
    ):
        super().__init__("publisher_simples")
        # self.get_logger().info(f"{TopicName} - {Message} - {TimerPeriod}")
        self.message = Message
        self.num = 0
        self.pub = self.create_publisher(String, TopicName, 10)
        self.create_timer(timer_period_sec=float(
            TimerPeriod), callback=self.callback)

    def callback(self):
        "Função para enviar a cada tick do timer"
        message = self.message
        to_send = String()
        if message:
            to_send.data = message
            self.pub.publish(to_send)
            self.get_logger().info(f"Enviei mensagem {self.num} - {message}")
            self.num += 1


def main():
    "docstring da função"
    rclpy.init()
    if len(sys.argv) == 1:
        node = Publisher()
    elif len(sys.argv) == 4:
        node = Publisher(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ros2 run <pkg> <node> <topic> <message> <period>")
        sys.exit()

    rclpy.spin(node)


if __name__ == "__main__":
    main()
