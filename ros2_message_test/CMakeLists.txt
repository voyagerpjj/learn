cmake_minimum_required(VERSION 3.5)
project(ros2_message_test_my)

# 查找 ROS 2 依赖
find_package(ament_cmake REQUIRED)  # 查找ament_cmake
find_package(ament_cmake_auto REQUIRED)  # 查找ament_cmake
find_package(rclcpp REQUIRED)  # 查找rclcpp
find_package(rclcpp_components REQUIRED)  # 查找rclcpp_components
find_package(Threads REQUIRED)
ament_auto_find_build_dependencies()

# 设置 CMAKE_PREFIX_PATH，帮助 CMake 查找 ROS 2 库
set(CMAKE_PREFIX_PATH "/opt/ros/foxy" ${CMAKE_PREFIX_PATH})

# 初始化 CMake 编译器和标准
set(CMAKE_C_COMPILER "gcc")
set(CMAKE_CXX_COMPILER "clang++")
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 查找源文件
file(GLOB SRC src/*.cpp)
message("src file: ${SRC}")

# 添加共享库（动态库）
ament_auto_add_library(${PROJECT_NAME} SHARED DIRECTORY src)

target_link_libraries(${PROJECT_NAME}
  ${OpenCV_LIBS}
  rclcpp::rclcpp
)

# 注册组件节点
rclcpp_components_register_node(${PROJECT_NAME}
  PLUGIN "${PROJECT_NAME}::SubscriberNode"
  EXECUTABLE ${PROJECT_NAME}_subscriber
)

rclcpp_components_register_node(${PROJECT_NAME}
  PLUGIN "${PROJECT_NAME}::PublisherNode"
  EXECUTABLE ${PROJECT_NAME}_publisher
)

# 自动打包
ament_auto_package(INSTALL_TO_SHARE)
