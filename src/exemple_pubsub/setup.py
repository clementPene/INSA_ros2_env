from setuptools import find_packages, setup

package_name = 'exemple_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cpene',
    maintainer_email='pene.clement@gmail.com',
    description='Exemple de reference (pas a modifier) : un publisher et un subscriber minimaux, talker/listener',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'talker = exemple_pubsub.publisher_member_function:main',
            'listener = exemple_pubsub.subscriber_member_function:main',
        ],
    },
)
