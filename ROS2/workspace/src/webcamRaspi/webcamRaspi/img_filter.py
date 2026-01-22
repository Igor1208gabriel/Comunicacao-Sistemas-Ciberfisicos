# PARA aplicar máscara de CV
"Docstring"
import sys
from rclpy.node import Node
import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
# import cv2 as cv


class ImageFilter(Node):
    "Docstring"

    def __init__(self, TopicPub="camera_filtered", TopicSub="camera_raw"):
        super().__init__("display_camera")
        self.get_logger().info("Display_camera iniciado!")
        self.sub = self.create_subscription(Image, TopicSub, self.hear, 10)
        self.pub = self.create_publisher(Image, TopicPub, 10)
        self.bridge = CvBridge()

    def publish_imagem(self, imagem):
        "Docstring"
        self.get_logger().info("Vou mandar aqui olha")
        self.pub.publish(imagem)

    def hear(self, message):
        "Docstring"
        self.get_logger().info("Eu ouvi hein...")
        photo = self.bridge.imgmsg_to_cv2(message)

        # APLICAR FILTRO DE IMAGEM
        tratada = Image()
        self.publish_imagem(tratada)


def main():
    "Docstring"
    rclpy.init()
    if len(sys.argv) == 1:
        node = ImageFilter()
    elif len(sys.argv) == 2:
        node = ImageFilter(sys.argv[1])
    else:
        print("Usage: ros2 run <pkg> <node> <topicpub> <topicsub>")
        sys.exit()
    rclpy.spin(node)


if __name__ == "__main__":
    main()
