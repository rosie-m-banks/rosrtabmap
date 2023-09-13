// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_msgs:srv/GetFromRio.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSGS__SRV__DETAIL__GET_FROM_RIO__BUILDER_HPP_
#define CUSTOM_MSGS__SRV__DETAIL__GET_FROM_RIO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_msgs/srv/detail/get_from_rio__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_msgs
{

namespace srv
{

namespace builder
{

class Init_GetFromRio_Request_a
{
public:
  Init_GetFromRio_Request_a()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_msgs::srv::GetFromRio_Request a(::custom_msgs::srv::GetFromRio_Request::_a_type arg)
  {
    msg_.a = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_msgs::srv::GetFromRio_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_msgs::srv::GetFromRio_Request>()
{
  return custom_msgs::srv::builder::Init_GetFromRio_Request_a();
}

}  // namespace custom_msgs


namespace custom_msgs
{

namespace srv
{

namespace builder
{

class Init_GetFromRio_Response_c
{
public:
  explicit Init_GetFromRio_Response_c(::custom_msgs::srv::GetFromRio_Response & msg)
  : msg_(msg)
  {}
  ::custom_msgs::srv::GetFromRio_Response c(::custom_msgs::srv::GetFromRio_Response::_c_type arg)
  {
    msg_.c = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_msgs::srv::GetFromRio_Response msg_;
};

class Init_GetFromRio_Response_b
{
public:
  Init_GetFromRio_Response_b()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetFromRio_Response_c b(::custom_msgs::srv::GetFromRio_Response::_b_type arg)
  {
    msg_.b = std::move(arg);
    return Init_GetFromRio_Response_c(msg_);
  }

private:
  ::custom_msgs::srv::GetFromRio_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_msgs::srv::GetFromRio_Response>()
{
  return custom_msgs::srv::builder::Init_GetFromRio_Response_b();
}

}  // namespace custom_msgs

#endif  // CUSTOM_MSGS__SRV__DETAIL__GET_FROM_RIO__BUILDER_HPP_
