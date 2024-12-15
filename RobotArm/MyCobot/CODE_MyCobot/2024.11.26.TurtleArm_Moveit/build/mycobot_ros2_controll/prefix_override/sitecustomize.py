import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/psy/2024.11.26.TurtleArm_Moveit/install/mycobot_ros2_controll'
