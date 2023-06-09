from setuptools import setup
import os
from glob import glob

package_name = 'turtlebot_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name),
         glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amongus',
    maintainer_email='zoltan.zeef@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'my_node = turtlebot_control.my_node:main',
            'turtlebot_controller = turtlebot_control.turtlebot_controller:main'
        ],
    },
)
