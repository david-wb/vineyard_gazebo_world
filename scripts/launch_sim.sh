#!/bin/bash

DIR=$(dirname "$0")
cd $DIR/..

colcon build
source install/setup.bash
export GZ_SIM_RESOURCE_PATH=$PWD/models:$$GZ_SIM_RESOURCE_PATH
ros2 launch vineyard_gazebo_world small.launch.py