from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    usb_cam = Node(
        package='webcamRaspi',
        executable='cam_node',
        name='usb_cam',
        arguments=['0', 'camera_raw', '0.1'],
    )

    img_display1 = Node(
        package='webcamRaspi',
        executable='display_node',
        name='img_display1',
        arguments=['camera_raw']
    )

    img_filter = Node(
        package='webcamRaspi',
        executable='img_filter',
        name='img_filter',
        arguments=['camera_filtered', 'camera_raw']
    )

    img_display2 = Node(
        package='webcamRaspi',
        executable='display_node',
        name='img_display2',
        arguments=['camera_filtered']
    )

    color_tracker = Node(
        package='webcamRaspi',
        executable='color_tracker',
        name='color_tracker',
        arguments=['pos_color', 'camera_filtered']
    )

    pos2cmd_vel = Node(
        package='webcamRaspi',
        executable='pos2cmd_vel',
        name='pos2cmd_vel',
        arguments=['cmd_vel', 'pos_color']
    )

    return LaunchDescription([
        usb_cam,
        img_display1,
        img_filter,
        img_display2,
        color_tracker,
        pos2cmd_vel
    ])
