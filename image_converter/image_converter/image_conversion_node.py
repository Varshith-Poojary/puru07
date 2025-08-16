#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_srvs.srv import SetBool
from cv_bridge import CvBridge
import cv2

class ImageConversionNode(Node):
    def __init__(self):
        super().__init__('image_conversion_node')

        # Parameters
        self.mode = 2  # Default mode: Color
        self.bridge = CvBridge()

        # Subscriber
        self.subscriber = self.create_subscription(
            Image,
            '/image_raw',  # Input topic from usb_cam
            self.image_callback,
            10
        )

        # Publisher
        self.publisher = self.create_publisher(
            Image,
            '/processed_image',  # Output topic
            10
        )

        # Service
        self.service = self.create_service(
            SetBool,
            'set_greyscale_mode',
            self.set_mode_callback
        )

        self.get_logger().info("Image Conversion Node started. Mode: Color")

    def set_mode_callback(self, request, response):
        if request.data:  # True → Grayscale
            self.mode = 1
            response.success = True
            response.message = "Mode set to Grayscale"
        else:  # False → Color
            self.mode = 2
            response.success = True
            response.message = "Mode set to Color"

        self.get_logger().info(response.message)
        return response

    def image_callback(self, msg):
        # Convert ROS Image to OpenCV
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Process image based on mode
        if self.mode == 1:
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_GRAY2BGR)

        # Publish processed image
        out_msg = self.bridge.cv2_to_imgmsg(cv_image, encoding='bgr8')
        self.publisher.publish(out_msg)

def main(args=None):
    rclpy.init(args=args)
    node = ImageConversionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
