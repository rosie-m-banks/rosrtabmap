import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import ComposableNodeContainer, LoadComposableNodes, Node
from launch_ros.descriptions import ComposableNode
from pathlib import Path
from dataclasses import dataclass
import math

@dataclass
class CameraDef:
    name: str
    model: str
    x: float
    y: float
    z: float
    roll: float
    pitch: float
    yaw: float


def launch_setup(context, *args, **kwargs):
    name = LaunchConfiguration('name').perform(context)
    

    params_file= LaunchConfiguration("params_file")
    params_shared = {
        "frame_id": name,
        "subscribe_rgbd": True,
        "subscribe_odom_info": True,
        "approx_sync": True,
        "Rtabmap/DetectionRate": "3.5", #TODO: play around with this
    }
    
    remappingsViz = [
        ("rgb/image", name+"/rgb/image_rect"),
        ("rgb/camera_info", name+"/rgb/camera_info"),
        ("depth/image", name+"/stereo/image_raw"),
    ]



    camera_launch = [
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource("camera_example.launch.py"),
            launch_arguments={"name": name,
                              "params_file": params_file}.items()),
    ]

    return camera_launch + [
        LoadComposableNodes(
             target_container=name+"_container",
            composable_node_descriptions=[
                ComposableNode(
                    package='rtabmap_odom',
                    plugin='rtabmap_odom::RGBDOdometry',
                    name='rgbd_odometry',
                    parameters=[params_shared],
                    remappings=remappingsViz,
                ),
            ],
        ),

        # LoadComposableNodes(
        #     target_container="rtab_container",
        #     composable_node_descriptions=[
        #         ComposableNode(
        #             package='rtabmap_sync',
        #             plugin='rtabmap_sync::RGBDXSync',
        #             name='rgbdx_sync',
        #             parameters=[params_shared, {"rgbd_cameras": len(cameras)}],
        #             remappings=remappings,
        #         ),
        #     ],
        # ),

        LoadComposableNodes(
            target_container=name+"_container",
            composable_node_descriptions=[
                ComposableNode(
                    package='rtabmap_slam',
                    plugin='rtabmap_slam::CoreWrapper',
                    name='rtabmap',
                    parameters=[params_shared],
                    remappings=remappingsViz,
                ),
            ],
        ),

        Node(
            package="rtabmap_viz",
            executable="rtabmap_viz",
            output="screen",
            parameters=[params_shared],
            remappings=remappingsViz,
        ),

    ]


def generate_launch_description():
    try:
        depthai_prefix = get_package_share_directory("depthai_ros_driver")

        declared_arguments = [
            DeclareLaunchArgument("name", default_value="oak"),
            DeclareLaunchArgument("params_file", default_value=str(Path(depthai_prefix, "config", 'camera.yaml'))),
            DeclareLaunchArgument("rectify_rgb", default_value="True"),
        ]

        return LaunchDescription(
            declared_arguments + [OpaqueFunction(function=launch_setup)]
        )
    except Exception:
        import traceback
        print(traceback.format_exc())
        raise

if __name__ == '__main__':
    generate_launch_description()