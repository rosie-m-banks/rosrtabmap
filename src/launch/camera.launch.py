import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from launch_ros.descriptions import ComposableNode
from launch_ros.actions import ComposableNodeContainer, LoadComposableNodes, Node


def launch_setup(context, *args, **kwargs):
    log_level = 'info'
    if(context.environment.get('DEPTHAI_DEBUG')=='1'):
        log_level='debug'

    urdf_launch_dir = os.path.join(get_package_share_directory('depthai_descriptions'), 'launch')
    
    params_file = LaunchConfiguration("params_file")
    camera_model = LaunchConfiguration('camera_model',  default = 'OAK-D')

    name = LaunchConfiguration('name').perform(context)

    parent_frame = LaunchConfiguration('parent_frame',  default = 'oak-d-base-frame')
    cam_pos_x    = LaunchConfiguration('cam_pos_x',     default = '0.0')
    cam_pos_y    = LaunchConfiguration('cam_pos_y',     default = '0.0')
    cam_pos_z    = LaunchConfiguration('cam_pos_z',     default = '0.0')
    cam_roll     = LaunchConfiguration('cam_roll',      default = '0.0')
    cam_pitch    = LaunchConfiguration('cam_pitch',     default = '0.0')
    cam_yaw      = LaunchConfiguration('cam_yaw',       default = '0.0')
    
    namespace = name

    return [
            Node(
                condition=IfCondition(LaunchConfiguration("use_rviz").perform(context)),
                package="rviz2",
                executable="rviz2",
                name="rviz2",
                output="log",
                arguments=["-d", LaunchConfiguration("rviz_config")],
            ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(urdf_launch_dir, 'urdf_launch.py')),
            launch_arguments={'tf_prefix': name,
                              'camera_model': camera_model,
                              'base_frame': name,
                              'parent_frame': parent_frame,
                              'cam_pos_x': cam_pos_x,
                              'cam_pos_y': cam_pos_y,
                              'cam_pos_z': cam_pos_z,
                              'cam_roll': cam_roll,
                              'cam_pitch': cam_pitch,
                              'cam_yaw': cam_yaw}.items()),

        ComposableNodeContainer(
            name=name+"_container",
            namespace="",
            package="rclcpp_components",
            executable="component_container",
            composable_node_descriptions=[
                    ComposableNode(
                        package="depthai_ros_driver",
                        plugin="depthai_ros_driver::Camera",
                        namespace=namespace,
                        name="camera",
                        parameters=[params_file],
                    ),
                    ComposableNode(
                        package='rtabmap_sync',
                        plugin='rtabmap_sync::RGBDSync',
                        name=f'rgbd_sync',
                        namespace=namespace,
                        parameters=[{"approx_sync": True}],
                        remappings=[
                            ("rgb/image", "camera/rgb/image_rect"),
                            ("rgb/camera_info", "camera/rgb/camera_info"),
                            ("depth/image", "camera/stereo/image_raw"),
                        ],
                    ),

            ],
            arguments=['--ros-args', '--log-level', log_level],
            output="both",
        ),
        
        LoadComposableNodes(
            condition=IfCondition(LaunchConfiguration("rectify_rgb")),
            target_container=name+"_container",
            composable_node_descriptions=[
                ComposableNode(
                    package="image_proc",
                    plugin="image_proc::RectifyNode",
                    name="rectify_color_node",
                    namespace=namespace,
                    remappings=[('image', 'camera/rgb/image_raw'),
                                ('camera_info', 'camera/rgb/camera_info'),
                                ('image_rect', 'camera/rgb/image_rect'),
                                ('image_rect/compressed', 'camera/rgb/image_rect/compressed'),
                                ('image_rect/compressedDepth', 'camera/rgb/image_rect/compressedDepth'),
                                ('image_rect/theora', 'camera/rgb/image_rect/theora')]
                )
            ]
        ),
    ]


def generate_launch_description():
    try:
        depthai_prefix = get_package_share_directory("depthai_ros_driver")

        declared_arguments = [
            DeclareLaunchArgument("name", default_value="oakx"),
            DeclareLaunchArgument("parent_frame", default_value="oak-d-base-frame"),
            DeclareLaunchArgument("cam_pos_x", default_value="0.0"),
            DeclareLaunchArgument("cam_pos_y", default_value="0.0"),
            DeclareLaunchArgument("cam_pos_z", default_value="0.0"),
            DeclareLaunchArgument("cam_roll", default_value="0.0"),
            DeclareLaunchArgument("cam_pitch", default_value="0.0"),
            DeclareLaunchArgument("cam_yaw", default_value="0.0"),
            DeclareLaunchArgument("params_file", default_value=os.path.join(depthai_prefix, 'config', 'camera.yaml')),
            DeclareLaunchArgument("use_rviz", default_value='false'),
            DeclareLaunchArgument("rviz_config", default_value=os.path.join(depthai_prefix, "config", "rviz", "rgbd.rviz")),
            DeclareLaunchArgument("rectify_rgb", default_value="True"),
        ]

        return LaunchDescription(
            declared_arguments + [OpaqueFunction(function=launch_setup)]
        )
    except Exception:
        import traceback
        print(traceback.format_exc())
        raise

