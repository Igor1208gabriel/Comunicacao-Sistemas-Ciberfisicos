"Docstring"
import sys
from rclpy.node import Node
import rclpy
from geometry_msgs.msg import Point, Twist


class Pos2CmdVel(Node):
    "Docstring"

    def __init__(self, topic_pub="cmd_vel", topic_sub="posicao"):
        super().__init__("pos2cmd_vel")

        self.get_logger().info("Nó pos2cmd_vel iniciado!")

        # Assina posição do objeto
        self.sub = self.create_subscription(
            Point, topic_sub, self.hear, 10
        )

        # Publica velocidade
        self.pub = self.create_publisher(
            Twist, topic_pub, 10
        )

    def hear(self, message: Point):
        "Docstring"

        self.get_logger().info(f"Recebi posição x={message.x}, y={message.y}")

        # Aqui você implementa seu controle real
        twist = Twist()

        # EXEMPLO: se o objeto está à esquerda → gira para a esquerda
        if message.x < -0.1:
            twist.angular.z = +0.3
        elif message.x > 0.1:
            twist.angular.z = -0.3
        else:
            twist.angular.z = 0.0

        # EXEMPLO: avança dependendo da distância Y
        twist.linear.x = max(0.0, 0.5 - abs(message.y))

        self.pub.publish(twist)

    def publish(self, twist):
        "Docstring"
        self.pub.publish(twist)


def main():
    "Docstring"
    rclpy.init()
    if len(sys.argv) == 1:
        node = Pos2CmdVel()
    elif len(sys.argv) == 3:
        node = Pos2CmdVel(sys.argv[1], sys.argv[2])
    else:
        print("Usage: ros2 run webcamRaspi pos2cmd_vel <topic_pub> <topic_sub>")
        sys.exit()
    rclpy.spin(node)


if __name__ == "__main__":
    main()
