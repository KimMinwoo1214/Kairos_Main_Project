from setuptools import setup
from setuptools import find_packages

package_name = 'lidar_cam'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='er',
    maintainer_email='ying.zhang@elephantrobotics.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fusion = lidar_cam.lidar_cam_fusion:main',
            'lidar_cam = lidar_cam.fusion_cam_lidar:main',
            'scan_data = lidar_cam.receive_scan:main',
	],
    },
)
