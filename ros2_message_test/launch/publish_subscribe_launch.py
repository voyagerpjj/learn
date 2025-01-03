import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNode, ComposableNodeContainer

def generate_launch_description():
    container = ComposableNodeContainer(
        name='publish_subscribe_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',  # 内置的容器可执行文件
        composable_node_descriptions=[
            ComposableNode(
                package='ros2_message_test_my',
                plugin='ros2_message_test_my::PublisherNode',  # 注册的类名
                name='Publish',
            ),
            ComposableNode(
                package='ros2_message_test_my',
                plugin='ros2_message_test_my::SubscriberNode',  # 注册的类名
                name='Subscriber',
            ),
        ],
        output='screen',
    )

    return LaunchDescription([container])
