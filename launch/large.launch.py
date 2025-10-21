from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    pkg_share = get_package_share_directory("vineyard_gazebo_world")
    world_file = os.path.join(pkg_share, "worlds", "large.world")

    GZ_SIM_SYSTEM_PLUGIN_PATH = os.environ.get("GZ_SIM_SYSTEM_PLUGIN_PATH", "")
    gazebo = ExecuteProcess(
        cmd=["gz", "sim", "-r", "--render-engine", "ogre2", "-v", "4", world_file],
        output="screen",
        additional_env={
            "GZ_SIM_SYSTEM_PLUGIN_PATH": f"/opt/ros/jazzy/lib:{GZ_SIM_SYSTEM_PLUGIN_PATH}"
        },
    )

    return LaunchDescription([gazebo])
