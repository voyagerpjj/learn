#include "rclcpp/rclcpp.hpp"
#include "rclcpp_components/register_node_macro.hpp"
#include "std_msgs/msg/string.hpp"

class SubscriberNode : public rclcpp::Node {
public:
  SubscriberNode(const rclcpp::NodeOptions &options)
      : Node("subscriber_node", options) {
    subscription_ = this->create_subscription<std_msgs::msg::String>(
        "topic_name", 10,
        std::bind(&SubscriberNode::callback, this, std::placeholders::_1));
  }

private:
  void callback(const std_msgs::msg::String::SharedPtr msg) const {
    RCLCPP_INFO(this->get_logger(), "Received: '%s'", msg->data.c_str());
  }

  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

// 注册节点作为组件
RCLCPP_COMPONENTS_REGISTER_NODE(SubscriberNode)
