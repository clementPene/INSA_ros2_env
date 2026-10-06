import rclpy
from rclpy.node import Node

from td2_custom_interfaces.srv import CountTurtles


class CountTurtlesService(Node):
    """
    Service CountTurtles : compte les tortues actuellement vivantes en
    interrogeant le graphe ROS depuis le code (on regarde tous les
    topics /pose).
    """

    def __init__(self):
        super().__init__('count_turtles_service')
        self.srv = self.create_service(CountTurtles, 'count_turtles', self.callback)

    def callback(self, request, response):
        names_and_types = self.get_topic_names_and_types()
        turtles = [name for name, _ in names_and_types if name.endswith('/pose')]
        response.count = len(turtles)
        self.get_logger().info(
            'count_turtles: %d tortue(s) -> %s' % (response.count, turtles))
        return response


def main(args=None):
    rclpy.init(args=args)
    node = CountTurtlesService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
