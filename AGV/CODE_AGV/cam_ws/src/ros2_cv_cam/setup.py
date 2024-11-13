from setuptools import find_packages, setup

package_name = 'ros2_cv_cam'

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
    maintainer='kmw',
    maintainer_email='werkm1214@hanyang.ac.kr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
	'cam_sub = ros2_cv_cam.cam_sub:main',
	'img_sub = ros2_cv_cam.img_sub:main',
	'qr_detect = ros2_cv_cam.qr_detect:main',
        ],
    },
)
