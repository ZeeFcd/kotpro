# Tutorial for the simulator
https://ros2-industrial-workshop.readthedocs.io/en/latest/_source/navigation/ROS2-Turtlebot.html


# Starting the Simulator
First we need start the gazebo 3D environment
open a terminal and type the following:

```
export ROS_DOMAIN_ID=0
```

```
source  /opt/ros/foxy/setup.bash
source  install/setup.bash
```

```
export TURTLEBOT3_MODEL=burger
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:`ros2 pkg \
prefix turtlebot3_gazebo \
`/share/turtlebot3_gazebo/models/
```

```
ros2 launch turtlebot3_gazebo <world-to-launch>
```

# Move turtlebot

Mount your workspace src path where you downloaded the package into, and run the script.
```
cd ~/<insert workspace here>/src
ros2 run turtlebot_control turtlebot_controller
```
