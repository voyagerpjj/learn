
#include <OpenCV_1.h>
#include <iostream>
#include <opencv2/core/hal/interface.h>
#include <opencv2/core/mat.hpp>
#include <opencv2/core/types.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/opencv.hpp>
void QuickDemo::ColorSpace_Demo(cv::Mat &image) {
  cv::Mat hsv, gray;
  cv::cvtColor(image, hsv, cv::COLOR_BGR2HSV);
}
void test_1(cv::Mat &src) {
  cv::Vec3b px_100 = src.at<cv::Vec3b>(100, 100);
  unsigned char blue = src.at<cv::Vec3b>(100, 100)[0];
  std::cout << "px_100 = " << px_100 << std::endl;
  src.at<cv::Vec3b>(600, 100) = cv::Vec3b(0, 0, 255);
  std::cout << "Blue = " << static_cast<int>(blue) << std::endl;
  std::vector<cv::Mat> channels; // 分离通道
  cv::split(src, channels[0]);
  cv::line(src, cv::Point(100, 100), cv::Point(500, 500), cv::Scalar(0, 0, 255),
           5, 8);
  auto font = cv::FONT_HERSHEY_SIMPLEX;
  cv::putText(src, "Hello OpenCV", cv::Point(10, 500), font, 3,
              cv::Scalar(0, 0, 255)); //添加文字
  cv::rectangle(src, cv::Point(200, 200), cv::Point(500, 500),
                cv::Scalar(255, 255, 0), 8); //画矩形
  // cv::Scalar表示颜色，cv::Point表示坐标
  // 显示图片
  cv::imshow("输入窗口", src);
  cv::waitKey(0);
  cv::destroyAllWindows();
}

void test_2() {

  // 创建三个单通道图像（假设它们已经被定义和初始化）
  cv::Mat channel1 = cv::Mat::zeros(480, 640, CV_8UC1); // 蓝色通道
  cv::Mat channel2 = cv::Mat::zeros(480, 640, CV_8UC1); // 绿色通道
  cv::Mat channel3 = cv::Mat::zeros(480, 640, CV_8UC1); // 红色通道

  // 填充通道数据（示例）
  channel1.setTo(cv::Scalar(255)); // 设置蓝色通道为最大值
  channel2.setTo(cv::Scalar(128)); // 设置绿色通道为中间值
  channel3.setTo(cv::Scalar(255)); // 设置红色通道为0

  // 创建一个 vector 来存储单通道图像
  std::vector<cv::Mat> channels = {channel1, channel2, channel3};

  // 合并通道
  cv::Mat mergedImage;
  cv::merge(channels, mergedImage);

  // 显示结果
  cv::imshow("Merged Image", mergedImage);
  cv::waitKey(0);
  cv::destroyAllWindows();

  cv::Mat mergedImage_chance;
  cv::cvtColor(mergedImage, mergedImage_chance,
               cv::COLOR_BGR2GRAY); //改为灰度空间
  cv::imshow("Merged Image Chance", mergedImage_chance);
  cv::waitKey(0);
  cv::destroyAllWindows(); // 关闭所有窗口

  cv::Mat mergedImage_add;
  cv::cvtColor(mergedImage_chance, mergedImage_chance,
               cv::COLOR_GRAY2BGR); //改为灰度空间
  cv::add(mergedImage, mergedImage_chance, mergedImage_add);
  cv::imshow("Merged Image add", mergedImage_add);
  cv::waitKey(0);
  cv::destroyAllWindows(); // 关闭所有窗口
}

int main(int argc, char **argv) {
  std::vector<cv::String> filenames;
  cv::String folder = "./test/*.jpg"; // 指定目录和文件类型（如 .jpg）

  // 使用 OpenCV 的 glob 函数获取目录中的所有图片文件
  cv::glob(folder, filenames);

  if (filenames.empty()) {
    printf("没有找到图片\n");
    return -1;
  }

  // 读取第一个图片
  cv::Mat src = cv::imread(filenames[0]);
  if (src.empty()) {
    printf("无法读取图片: %s\n", filenames[0].c_str());
    return -1;
  }
  std::cout << "img.size = " << src.size() << std::endl;
  std::cout << "img.channels = " << src.channels() << std::endl;
  std::cout << "img.type = " << src.type() << std::endl;
  // test_1(src);
  test_2();
  return 0;
}
