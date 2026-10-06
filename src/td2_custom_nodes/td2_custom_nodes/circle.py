import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class Circle(Node):
    """
    Fait decrire un cercle a turtle1, avec le
    rayon en parametre ROS au lieu d'une valeur codée en dur, reglable
    via "--ros-args -p" ou "ros2 param set" a chaud.

    Meme principe que "ros2 topic pub -r 10 /turtle1/cmd_vel ..." au
    TD1, mais republie depuis un node Python plutot que depuis la ligne
    de commande.

    "radius" correspond au rayon du cercle effectue.
    La vitesse angulaire est deduite en interne
    (angular.z = linear_speed / radius).
    """

    def __init__(self):
        super().__init__('circle')
        self.declare_parameter('radius', 2.0)
        self.declare_parameter('linear_speed', 2.0)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.1  # 10 Hz, comme "-r 10" au TD1
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        radius = self.get_parameter('radius').value
        linear_speed = self.get_parameter('linear_speed').value

        msg = Twist()
        msg.linear.x = linear_speed
        if radius != 0.0:
            msg.angular.z = linear_speed / radius
        else:
            self.get_logger().warn(
                'radius=0 : division par zero evitee, angular.z force a 0 '
                '(la tortue avance tout droit au lieu de tourner en rond)')
            msg.angular.z = 0.0
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = Circle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
