# TODO Procura por uma cor, dá a posição do objeto de saída
from rclpy.node import Node
import rclpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from cv_bridge import CvBridge
import cv2 as cv
import sys


class ColorTracker(Node):
    def __init__(self, TopicPub="pos", TopicSub="image_filtered"):
        super().__init__("display_camera")
        self.get_logger().info("Display_camera iniciado!")
        self.sub = self.create_subscription(Image, TopicSub, self.Hear, 10)
        self.pub = self.create_publisher(Point, TopicPub, 10)
        self.bridge = CvBridge()
        self.sub

    def Hear(self, message):
        self.get_logger().info("Eu ouvi hein...")
        photo = self.bridge.imgmsg_to_cv2(message)

        # APLICAR ALGORITMO PARA ENCONTRAR A COR
        position = Point()
        self.pub.publish(position)

    def Publish(self, position):
        self.get_logger().info("Vou mandar aqui olha")
        self.pub.publish(position)


def main():
    rclpy.init()
    if len(sys.argv) == 1:
        node = ColorTracker()
    elif len(sys.argv) == 2:
        node = ColorTracker(sys.argv[1])
    else:
        print("Usage: ros2 run <pkg> <node> <topicname>")
        exit()
    rclpy.spin(node)


if __name__ == "__main__":
    main()
