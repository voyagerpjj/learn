
#include <OpenCV_1.h>
#include <iostream>
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
  cv::line(src, cv::Point(100, 100), cv::Point(500, 500), cv::Scalar(0, 0, 255),
           5, 8);
  auto font = cv::FONT_HERSHEY_SIMPLEX;
  cv::putText(src, "Hello OpenCV", cv::Point(10, 500), font, 3,
              cv::Scalar(0, 0, 255)); //添加文字
  cv::rectangle(src, cv::Point(200, 200), cv::Point(500, 500),
                cv::Scalar(255, 255, 0), 8); //画矩形
  // cv::Scalar表示颜色，cv::Point表示坐标
  // 显示图片
  imshow("输入窗口", src);
  cv::waitKey(0);
  cv::destroyAllWindows();
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
  test_1(src);
  return 0;
}
