import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'td2_custom_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cpene',
    maintainer_email='pene.clement@gmail.com',
    description='Solution TD2 : defi circle, services CountTurtles/DistanceToGoal, action GoToPoint',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'circle = td2_custom_nodes.circle:main',
            'count_turtles = td2_custom_nodes.count_turtles:main',
            'distance_to_goal = td2_custom_nodes.distance_to_goal:main',
            'go_to_point_server = td2_custom_nodes.go_to_point_server:main',
            'go_to_point_client = td2_custom_nodes.go_to_point_client:main',
        ],
    },
)
