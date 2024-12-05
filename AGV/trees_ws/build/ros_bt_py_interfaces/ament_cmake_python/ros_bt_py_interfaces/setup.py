from setuptools import find_packages
from setuptools import setup

setup(
    name='ros_bt_py_interfaces',
    version='0.1.1',
    packages=find_packages(
        include=('ros_bt_py_interfaces', 'ros_bt_py_interfaces.*')),
)
