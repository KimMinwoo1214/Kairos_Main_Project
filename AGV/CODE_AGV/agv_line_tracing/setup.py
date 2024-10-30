from setuptools import setup

package_name = 'agv_line_tracing'

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
            'pub = agv_line_tracing.yellow_pub2:main',
            'sub = agv_line_tracing.yellow_sub2:main',
            'tel = agv_line_tracing.teleop_agv:main',
            'con = agv_line_tracing.wheel_con:main',
            ],
    },
)
