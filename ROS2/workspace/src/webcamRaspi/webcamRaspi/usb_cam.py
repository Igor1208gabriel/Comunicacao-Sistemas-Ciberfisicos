"Docstring"

import sys
from rclpy.node import Node
import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 as cv


class PublisherCamera(Node):
    "Docstring"

    def __init__(
        self,
        VideoCapture=0,
        TopicName="camera_raw",
        TimerPeriod=1 / 10,
    ):
        super().__init__("cam_node")
        self.get_logger().info("cam_node iniciado!")
        self.cam = cv.VideoCapture(VideoCapture)
        self.pub = self.create_publisher(Image, TopicName, 10)
        self.bridge = CvBridge()
        self.create_timer(timer_period_sec=float(
            TimerPeriod), callback=self.callback)

    def callback(self):
        "Docstring"
        _, img = self.cam.read()
        if _:
            to_send = self.bridge.cv2_to_imgmsg(img)
            self.pub.publish(to_send)
            self.get_logger().info("mandei uma foto ein olha lá")
        else:
            self.cam.set(cv.CAP_PROP_POS_FRAMES, 0)


def main():
    "Docstring"

    rclpy.init()
    if len(sys.argv) == 1:
        node = PublisherCamera()
    elif len(sys.argv) == 4:
        node = PublisherCamera(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ros2 run <pkg> <node> <videocapture>, <topicname>, <timerperiod>")
        sys.exit()
    rclpy.spin(node)


if __name__ == "__main__":
    main()
