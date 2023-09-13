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
    depthai_prefix = Path(__file__).parent
    
    cameras = [
        CameraDef(name="oak0",
                  model="OAK-D-S2",
                  x= 0.0,
                  y = 0.0,
                  z = 0.0,
                  pitch = 0.0,
                  roll = 0.0,
                  yaw = 0.0),
        CameraDef(name="oak1",
                  model="OAK-D-LITE",
                  x= 0.0,
                  y = 0.0,
                  z = 0.0,
                  pitch = 0.0,
                  roll = 0.0,
                  yaw = math.pi),
    ]
    

    params_file= LaunchConfiguration("params_file")
    params_shared = {
        "frame_id": name,
        "subscribe_rgbd": True,
        "subscribe_odom_info": True,
        "approx_sync": True,
        "Rtabmap/DetectionRate": "3.5", #TODO: play around with this
    }
    parameters = [
        {
            **params_shared,
            "rgbd_cameras": 0,
        }
    ]

    

    remappings = [
         (f"rgbd_image{i}", camera.name + "/rgbd_image")
         for i, camera in enumerate(cameras)
    ]

    camera_launch = [
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(str(depthai_prefix / "camera.launch.py")),
            launch_arguments={
                "name": camera.name,
                'cam_pos_x': str(camera.x),
                'cam_pos_y':str(camera.y),
                'cam_pos_z':str(camera.z),
                'cam_roll':str(camera.roll),
                'cam_pitch':str(camera.pitch),
                'cam_yaw':str(camera.yaw),
                'camera_model':camera.model,
                "params_file": params_file
            }.items())
        for camera in cameras
    ]

    return camera_launch + [
        ComposableNodeContainer(
            name="rtab_container",
            namespace="",
            package="rclcpp_components",
            executable="component_container",
            # target_container="rtab_container",
            composable_node_descriptions=[
                ComposableNode(
                    package='rtabmap_odom',
                    plugin='rtabmap_odom::RGBDOdometry',
                    name='rgbd_odometry',
                    parameters=[params_shared, {"rgbd_cameras": len(cameras)}],
                    remappings=remappings,
                ),
            ],
        ),

        LoadComposableNodes(
            target_container="rtab_container",
            composable_node_descriptions=[
                ComposableNode(
                    package='rtabmap_sync',
                    plugin='rtabmap_sync::RGBDXSync',
                    name='rgbdx_sync',
                    parameters=[params_shared, {"rgbd_cameras": len(cameras)}],
                    remappings=remappings,
                ),
            ],
        ),

        LoadComposableNodes(
            target_container="rtab_container",
            composable_node_descriptions=[
                ComposableNode(
                    package='rtabmap_slam',
                    plugin='rtabmap_slam::CoreWrapper',
                    name='rtabmap',
                    parameters=[params_shared, {"rgbd_cameras": 0}],
                    # remappings=remappings,
                ),
            ],
        ),

        Node(
            package="rtabmap_viz",
            executable="rtabmap_viz",
            output="screen",
            parameters=parameters,
            remappings=remappings,
        ),
    ]


def generate_launch_description():
    try:
        depthai_prefix = Path(__file__).parent

        declared_arguments = [
            DeclareLaunchArgument("name", default_value="oaktyg"),
            DeclareLaunchArgument("params_file", default_value=str(Path(depthai_prefix, "..", "config", 'camera.yaml'))),
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