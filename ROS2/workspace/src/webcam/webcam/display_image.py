from rclpy.node import Node
import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 as cv
import sys


class DisplayCamera(Node):
    def __init__(self, TopicName="camera_raw"):
        super().__init__("display_camera")
        self.get_logger().info("Display_camera iniciado!")
        self.sub = self.create_subscription(Image, TopicName, self.Hear, 10)
        self.bridge = CvBridge()
        self.sub

    def Hear(self, message):
        self.get_logger().info("Eu ouvi hein...")
        photo = self.bridge.imgmsg_to_cv2(message)
        cv.imshow("imagem", photo)
        cv.waitKey(25)


def main():
    rclpy.init()
    if len(sys.argv) == 1:
        node = DisplayCamera()
    elif len(sys.argv) == 2:
        node = DisplayCamera(sys.argv[1])
    else:
        print("Usage: ros2 run <pkg> <node> <topicname>")
        exit()
    rclpy.spin(node)


if __name__ == "__main__":
    main()
