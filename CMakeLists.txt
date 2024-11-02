# CMake 最低版本号要求设置为 3.16
cmake_minimum_required(VERSION 3.16)
# 定义项目名称为 hello_word
project(hello_word)
# 在系统中查找 OpenCV 库。如果找到了 OpenCV，那么它会设置一些变量来指示OpenCV 的位置和版本。
# 如果找不到 OpenCV，可能会导致构建失败或者在后续的步骤中无法使用OpenCV。
find_package(OpenCV REQUIRED)
# 输出 OpenCV 版本，帮助调试
message(STATUS "OpenCV version: ${OpenCV_VERSION}")
message(STATUS "OpenCV include directories: ${OpenCV_INCLUDE_DIRS}")
message(STATUS "OpenCV libraries: ${OpenCV_LIBS}")
# 包含 OpenCV 的头文件目录
include_directories(${OpenCV_INCLUDE_DIRS})
# 将 inc 目录添加到项目的头文件搜索路径中
include_directories(inc)
# 使用 GLOB 命令来查找 src 目录下的所有文件，并将结果保存到 SRC 变量中，即 SRC=mian.cpp+func.cpp
# 使用 ** 通配符可以递归地搜索子目录下所有文件
file(GLOB SRC src/**)
# 打印输出 SRC 变量中的文件列表
# 这是一种调试信息，用于确认在构建过程中找到了哪些源文件
message(
 "src file: ${SRC}"
)
# add_executable 用于将 SRC 变量中的源文件编译成一个可执行文件
# 生成的可执行文件名称为${PROJECT_NAME}
add_executable(${PROJECT_NAME} ${SRC})
# 链接 OpenCV 库
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})
