from setuptools import setup

package_name = 'ros2_cv_webcam'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
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
            'img_publisher = ros2_cv_webcam.webcam_pub:main',
            'img_subscriber = ros2_cv_webcam.webcam_sub:main'
            'qr_detect = ros2_cv_webcam.qr_detect:main',
            ],
    },
)
