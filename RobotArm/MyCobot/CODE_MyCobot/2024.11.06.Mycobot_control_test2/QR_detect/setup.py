
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
	'image_pub = QR_detect.image_pub:main',
    'image_pub_hs = QR_detect.image_pub_hs:main',
	'image_sub = QR_detect.image_sub:main',
        ],
    },
)
