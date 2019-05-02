from setuptools import setup
from setuptools import find_packages

package_name = 'ros2_listener'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    author='Ragesh Ramachandran',
    author_email='ragesh.ramachandran@ipa.fraunhofer.de',
    maintainer='',
    maintainer_email='',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Package containing ros2 python talker.',
    license='Apache License, Version 2.0',
    test_suite='test',
    entry_points={
        'console_scripts': ['listener = ros2_listener.scripts.listener:main'], #folder_name.node_name:name_of_main_fun
    },
)