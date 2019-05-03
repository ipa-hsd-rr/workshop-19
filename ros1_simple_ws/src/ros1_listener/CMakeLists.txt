cmake_minimum_required(VERSION 2.8.3)
project(ros1_listener)

find_package(catkin REQUIRED COMPONENTS
)

catkin_python_setup()

catkin_package()

catkin_install_python(PROGRAMS 
  scripts/listener
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)