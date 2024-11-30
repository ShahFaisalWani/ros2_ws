from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os 
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    params_file = LaunchConfiguration('slam_params_file', default=os.path.join(os.path.join(get_package_share_directory('robot'), 'config/mapper_params_online_async.yaml')))

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('slam_toolbox'), 'launch/online_async_launch.py')
            ),
            # launch_arguments={'slam_params_file': params_file}.items() 
        )
    ])
