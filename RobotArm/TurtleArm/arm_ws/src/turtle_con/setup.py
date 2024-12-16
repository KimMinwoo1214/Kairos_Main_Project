from setuptools import setup

package_name = 'turtle_con'

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
    maintainer='pi',
    maintainer_email='jdedu.kr@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'turtle_ros2_con = turtle_con.turtle_ros2_con:main',
        'with_qr = turtle_con.with_qr:main',
        'move_qr = turtle_con.move_qr:main',
        'qr_log = turtle_con.qr_log:main',
        ],
    },
)