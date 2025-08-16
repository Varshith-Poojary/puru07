from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        # USB camera node
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam',
            parameters=[{
                'video_device': '/dev/video0',
                'image_width': 640,
                'image_height': 480,
                'pixel_format': 'yuyv',
                'io_method': 'mmap'
            }],
            output='screen'
        ),

        # Image conversion node
        Node(
            package='image_converter',
            executable='img_con_node',
            name='image_conversion',
            parameters=[{
                'input_topic': '/image_raw',
                'output_topic': '/processed_image'
            }],
            output='screen'
        ),

        # # key control node
        # Node(
        #     package='image_converter',
        #     executable='key_controller',
        #     name='key_control',
        #     output='screen'
        # )
    ])
