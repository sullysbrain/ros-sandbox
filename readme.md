# ROS (Robotic Operating System) Sandbox Project

This is a sandboxed project folder for my work with ROS (the robotic operating system). Note, any references are to assume this is ROS2 and not ROS1 for dev purposes. The work done in the dev sandbox will eventually be used in the production repository for Project Samson.

## General Setup
The environment is being setup in Ubuntu 22.04 in a virtual machine on an M3 Max. I will be following this tutorial at least in the beginning:

[ROS2 Tutorial on Youtube](https://www.youtube.com/watch?v=Gg25GfA456o&list=PLLSegLrePWgJk6dfV-UXSh2TZ74wNntWt)

This video goes through the installation of ROS2 on Ubuntu. 

TODO: Setup for 4 Mecanum Wheel for navigation
TODO: Setup ROS2 with Docker for better containerization




## Framework Installation
Once you install ROS2, you must add the colcon autocomplete, then add ros, colcon, and the install to your bash. 
To install ROS2:
	- udo apt install ros-iron-desktop

To install the colcon:
	- sudo apt install python3-colcon-common-extensions

With vim, open ~/.bashrc and add these three lines:
	- source /opt/ros/iron/setup.bash
	- source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
	- source ~/ros2_ws/install/setup.bash

## Steps to Build Project
Create a ROS2 Package (inside the 'src' folder)
>> ros2 pkg create my_robot_controller --build-type ament_python  --dependencies rclpy

