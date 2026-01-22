"Docstring"
import sys
from rclpy.node import Node
import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 as cv


class DisplayCamera(Node):
    "Docstring"

    def __init__(self, TopicName):
        super().__init__("display_camera")
        self.get_logger().info("Display_camera iniciado!")
        self.sub = self.create_subscription(Image, TopicName, self.hear, 10)
        self.bridge = CvBridge()

    def hear(self, message):
        "Docstring"
        self.get_logger().info("Eu ouvi hein...")
        photo = self.bridge.imgmsg_to_cv2(message)
        cv.imshow("imagem", photo)
        cv.waitKey(25)


def main():
    "Docstring"
    rclpy.init()
    if len(sys.argv) != 2:
        print("Usage: ros2 run <pkg> <node> <topicname>")
        sys.exit()
    else:
        node = DisplayCamera(sys.argv[1])
    rclpy.spin(node)


if __name__ == "__main__":
    main()
