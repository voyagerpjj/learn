#include "rclcpp/rclcpp.hpp"
#include "rclcpp_components/register_node_macro.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

class PublisherNode : public rclcpp::Node {
public:
  PublisherNode(const rclcpp::NodeOptions &options)
      : Node("publisher_node", options) {
    publisher_ =
        this->create_publisher<std_msgs::msg::String>("topic_name", 10);
    timer_ = this->create_wall_timer(
        1ms, std::bind(&PublisherNode::publish_message, this));
  }

private:
  void publish_message() {
    auto message = std_msgs::msg::String();
    message.data = "Hello from publisher!";
    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
    publisher_->publish(message);
  }

  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
};

// 注册节点作为组件
RCLCPP_COMPONENTS_REGISTER_NODE(PublisherNode)
