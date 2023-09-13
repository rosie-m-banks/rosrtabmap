// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_msgs:msg/Pose3D.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSGS__MSG__DETAIL__POSE3_D__BUILDER_HPP_
#define CUSTOM_MSGS__MSG__DETAIL__POSE3_D__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_msgs/msg/detail/pose3_d__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_msgs
{

namespace msg
{

namespace builder
{

class Init_Pose3D_w
{
public:
  explicit Init_Pose3D_w(::custom_msgs::msg::Pose3D & msg)
  : msg_(msg)
  {}
  ::custom_msgs::msg::Pose3D w(::custom_msgs::msg::Pose3D::_w_type arg)
  {
    msg_.w = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_msgs::msg::Pose3D msg_;
};

class Init_Pose3D_z
{
public:
  explicit Init_Pose3D_z(::custom_msgs::msg::Pose3D & msg)
  : msg_(msg)
  {}
  Init_Pose3D_w z(::custom_msgs::msg::Pose3D::_z_type arg)
  {
    msg_.z = std::move(arg);
    return Init_Pose3D_w(msg_);
  }

private:
  ::custom_msgs::msg::Pose3D msg_;
};

class Init_Pose3D_y
{
public:
  explicit Init_Pose3D_y(::custom_msgs::msg::Pose3D & msg)
  : msg_(msg)
  {}
  Init_Pose3D_z y(::custom_msgs::msg::Pose3D::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Pose3D_z(msg_);
  }

private:
  ::custom_msgs::msg::Pose3D msg_;
};

class Init_Pose3D_x
{
public:
  Init_Pose3D_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Pose3D_y x(::custom_msgs::msg::Pose3D::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Pose3D_y(msg_);
  }

private:
  ::custom_msgs::msg::Pose3D msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_msgs::msg::Pose3D>()
{
  return custom_msgs::msg::builder::Init_Pose3D_x();
}

}  // namespace custom_msgs

#endif  // CUSTOM_MSGS__MSG__DETAIL__POSE3_D__BUILDER_HPP_
