import math

import rclpy
import rclpy.task
from rclpy.action import ActionServer
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

from td2_custom_interfaces.action import GoToPoint


class GoToPointActionServer(Node):
    """
    Action GoToPoint : envoie la tortue vers un point donne, avec un
    retour de progression (feedback) pendant le trajet.
    """

    def __init__(self):
        super().__init__('go_to_point_action_server')
        self._action_server = ActionServer(
            self, GoToPoint, 'go_to_point', self.execute_callback)
        self.pose = None
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_sub = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10)

    def pose_callback(self, msg):
        self.pose = msg

    async def _sleep(self, seconds):
        """Point d'attente compatible avec les coroutines rclpy."""
        future = rclpy.task.Future()
        timer = self.create_timer(seconds, lambda: self._resolve(future, timer))
        await future

    def _resolve(self, future, timer):
        timer.cancel()
        if not future.done():
            future.set_result(None)

    async def execute_callback(self, goal_handle):
        self.get_logger().info(
            'Executing goal: (%.2f, %.2f)' % (goal_handle.request.x, goal_handle.request.y))
        feedback_msg = GoToPoint.Feedback()
        goal_x, goal_y = goal_handle.request.x, goal_handle.request.y
        tolerance, kp_linear, kp_angular = 0.1, 1.5, 6.0

        while self.pose is None:
            await self._sleep(0.05)

        while True:
            dx, dy = goal_x - self.pose.x, goal_y - self.pose.y
            distance = math.hypot(dx, dy)
            feedback_msg.distance_remaining = distance
            goal_handle.publish_feedback(feedback_msg)

            if distance < tolerance:
                break

            angle_to_goal = math.atan2(dy, dx)
            angle_error = angle_to_goal - self.pose.theta
            angle_error = math.atan2(math.sin(angle_error), math.cos(angle_error))

            cmd = Twist()
            cmd.linear.x = kp_linear * distance
            cmd.angular.z = kp_angular * angle_error
            self.cmd_pub.publish(cmd)

            await self._sleep(0.05)

        self.cmd_pub.publish(Twist())  # stop
        goal_handle.succeed()

        result = GoToPoint.Result()
        result.success = True
        result.final_x = self.pose.x
        result.final_y = self.pose.y
        return result


def main(args=None):
    rclpy.init(args=args)
    node = GoToPointActionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
