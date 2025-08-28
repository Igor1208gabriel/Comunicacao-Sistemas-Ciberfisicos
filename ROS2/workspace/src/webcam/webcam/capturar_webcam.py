from rclpy.node import Node
import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 as cv
import sys


class PublisherCamera(Node):
    def __init__(
        self,
        VideoCapture=0,
        TopicName="camera_raw",
        TimerPeriod=1 / 30,
    ):
        super().__init__("leitor_camera")
        self.get_logger().info("Leitor_camera iniciado!")
        self.cam = cv.VideoCapture(VideoCapture)
        self.pub = self.create_publisher(Image, TopicName, 10)
        self.bridge = CvBridge()
        self.create_timer(timer_period_sec=float(TimerPeriod), callback=self.Callback)

    def Callback(self):
        _, img = self.cam.read()
        if _:
            ToSend = self.bridge.cv2_to_imgmsg(img)
            self.pub.publish(ToSend)
            self.get_logger().info("mandei uma foto ein olha lá")
        else:
            self.cam.set(cv.CAP_PROP_POS_FRAMES, 0)


def main():
    rclpy.init()
    if len(sys.argv) == 1:
        node = PublisherCamera()
    elif len(sys.argv) == 4:
        node = PublisherCamera(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ros2 run <pkg> <node> <videocapture>, <topicname>, <timerperiod>")
        exit()
    rclpy.spin(node)


if __name__ == "__main__":
    main()
