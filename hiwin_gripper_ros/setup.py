from setuptools import setup

package_name = 'hiwin_gripper_ros'

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
    maintainer='iclab_luis',
    maintainer_email='iclab_luis@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hiwin_gripper_service = hiwin_gripper_ros.hiwin_gripper_service:main'
        ],
    },
)
