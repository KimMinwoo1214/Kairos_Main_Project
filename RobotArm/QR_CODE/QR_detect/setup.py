
from setuptools import setup

package_name = 'QR_detect'

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
    maintainer_email='er@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
	'web_pub = QR_detect.webcam_pub:main',
	'web_sub = QR_detect.webcam_sub:main',
	'qr_pub = QR_detect.qr_pub:main',
        ],
    },
)