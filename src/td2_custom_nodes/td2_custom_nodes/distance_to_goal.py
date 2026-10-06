import math

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

from td2_custom_interfaces.srv import DistanceToGoal


class DistanceToGoalService(Node):
    """
    Service DistanceToGoal :
    on s'abonne a /turtle1/pose, et le service repond distance + angle
    vers le point demande.
    """

    def __init__(self):
        super().__init__('distance_to_goal_service')
        self.pose = None
        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10)
        self.srv = self.create_service(DistanceToGoal, 'distance_to_goal', self.callback)

    def pose_callback(self, msg):
        self.pose = msg

    def callback(self, request, response):
        if self.pose is None:
            self.get_logger().warn(
                'distance_to_goal: aucune pose recue pour l\'instant '
                '(turtlesim est-il lance ?)')
            response.distance = -1.0
            response.angle = 0.0
            return response

        dx = request.x - self.pose.x
        dy = request.y - self.pose.y
        angle_to_goal = math.atan2(dy, dx)
        angle_error = angle_to_goal - self.pose.theta
        angle_error = math.atan2(math.sin(angle_error), math.cos(angle_error))

        response.distance = math.hypot(dx, dy)
        response.angle = angle_error
        return response


def main(args=None):
    rclpy.init(args=args)
    node = DistanceToGoalService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
