from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """
    Lance turtlesim et les serveurs des deux services personnalises
    (count_turtles, distance_to_goal) d'un seul coup.
    """
    return LaunchDescription([
        Node(package='turtlesim', executable='turtlesim_node', name='turtlesim'),
        Node(package='td2_custom_nodes', executable='count_turtles', name='count_turtles'),
        Node(package='td2_custom_nodes', executable='distance_to_goal', name='distance_to_goal'),
    ])
