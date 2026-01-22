"Docstring"
from setuptools import find_packages, setup

PACKAGE_NAME = 'webcamRaspi'

setup(
    name=PACKAGE_NAME,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + PACKAGE_NAME]),
        ('share/' + PACKAGE_NAME, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'cam_node = webcamRaspi.usb_cam:main',
            'display_node = webcamRaspi.img_display:main',
            'img_filter = webcamRaspi.img_filter:main',
            'color_tracker = webcamRaspi.color_tracker:main',
            'pos2cmd_vel = webcamRaspi.pos_to_cmd_vel:main',
        ],
    },
)
