from setuptools import setup
from glob import glob
import os

package_name = 'ros2_cv_webcam'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Add the launch directory to the package
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
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
            'img_publisher = ros2_cv_webcam.webcam_pub:main',
            'img_subscriber = ros2_cv_webcam.webcam_sub:main',
            'myagv_pubic = ros2_cv_webcam.myagv_pub:main',
            'myagv_subsc = ros2_cv_webcam.myagv_sub:main',
            'qr_cam = ros2_cv_webcam.qr_cam:main',
            'yolo_cam = ros2_cv_webcam.yolo_cam:main',
            'detection = ros2_cv_webcam.detection:main',
   	    'test = ros2_cv_webcam.web_test:main',
        ],
    },
)

