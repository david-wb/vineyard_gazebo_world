#!/bin/bash

DIR=$(dirname "$0")
cd $DIR/..

colcon build
source install/setup.bash
ros2 launch vineyard_gazebo_world small.launch.py