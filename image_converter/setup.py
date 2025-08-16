from setuptools import find_packages, setup

package_name = 'image_converter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/image_conversion_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='varshith',
    maintainer_email='varshith@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['img_con_node = image_converter.image_conversion_node:main',
                            # 'key_controller = image_converter.key_control:main',
        ],
    },
)
