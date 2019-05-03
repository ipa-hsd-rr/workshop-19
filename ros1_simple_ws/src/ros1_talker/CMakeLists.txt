cmake_minimum_required(VERSION 2.8.3)
project(ros1_talker)

find_package(catkin REQUIRED COMPONENTS
)

#catkin_python_setup()

catkin_package()

catkin_install_python(PROGRAMS 
  scripts/talker
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)