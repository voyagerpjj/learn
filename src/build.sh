#!/bin/bash

# 设置build目录的路径
BUILD_DIR="../build"

# 检查命令行参数
if [ $# -eq 1 ]; then
    choice=$1
else
    # 提示用户选择操作
    echo "请选择操作:"
    echo "1. 删除build目录并重新构建"
    echo "2. 直接编译（如果已有build目录）"
    read -p "输入选项 [1 或 2]: " choice
fi

# 根据用户的选择执行相应操作
if [ "$choice" == "1" ]; then
    echo "删除 $BUILD_DIR 目录..."
    rm -rf $BUILD_DIR
    mkdir $BUILD_DIR
    cd $BUILD_DIR
    echo "重新生成构建文件..."
    cmake -DCMAKE_RUNTIME_OUTPUT_DIRECTORY="../" ..
    echo "开始编译..."
    make
elif [ "$choice" == "2" ]; then
    if [ -d "$BUILD_DIR" ]; then
        cd $BUILD_DIR
        echo "开始编译..."
        make
    else
        echo "$BUILD_DIR 目录不存在，请先选择选项 1 来创建构建文件。"
    fi
else
    echo "无效选项，请选择 1 或 2。"
fi
