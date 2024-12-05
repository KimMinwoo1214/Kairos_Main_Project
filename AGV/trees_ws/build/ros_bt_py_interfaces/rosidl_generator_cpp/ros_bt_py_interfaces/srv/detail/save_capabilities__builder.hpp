// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ros_bt_py_interfaces:srv/SaveCapabilities.idl
// generated code does not contain a copyright notice

#ifndef ROS_BT_PY_INTERFACES__SRV__DETAIL__SAVE_CAPABILITIES__BUILDER_HPP_
#define ROS_BT_PY_INTERFACES__SRV__DETAIL__SAVE_CAPABILITIES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ros_bt_py_interfaces/srv/detail/save_capabilities__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ros_bt_py_interfaces
{

namespace srv
{

namespace builder
{

class Init_SaveCapabilities_Request_package
{
public:
  Init_SaveCapabilities_Request_package()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ros_bt_py_interfaces::srv::SaveCapabilities_Request package(::ros_bt_py_interfaces::srv::SaveCapabilities_Request::_package_type arg)
  {
    msg_.package = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros_bt_py_interfaces::srv::SaveCapabilities_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros_bt_py_interfaces::srv::SaveCapabilities_Request>()
{
  return ros_bt_py_interfaces::srv::builder::Init_SaveCapabilities_Request_package();
}

}  // namespace ros_bt_py_interfaces


namespace ros_bt_py_interfaces
{

namespace srv
{

namespace builder
{

class Init_SaveCapabilities_Response_error_message
{
public:
  explicit Init_SaveCapabilities_Response_error_message(::ros_bt_py_interfaces::srv::SaveCapabilities_Response & msg)
  : msg_(msg)
  {}
  ::ros_bt_py_interfaces::srv::SaveCapabilities_Response error_message(::ros_bt_py_interfaces::srv::SaveCapabilities_Response::_error_message_type arg)
  {
    msg_.error_message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros_bt_py_interfaces::srv::SaveCapabilities_Response msg_;
};

class Init_SaveCapabilities_Response_success
{
public:
  Init_SaveCapabilities_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SaveCapabilities_Response_error_message success(::ros_bt_py_interfaces::srv::SaveCapabilities_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_SaveCapabilities_Response_error_message(msg_);
  }

private:
  ::ros_bt_py_interfaces::srv::SaveCapabilities_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros_bt_py_interfaces::srv::SaveCapabilities_Response>()
{
  return ros_bt_py_interfaces::srv::builder::Init_SaveCapabilities_Response_success();
}

}  // namespace ros_bt_py_interfaces

#endif  // ROS_BT_PY_INTERFACES__SRV__DETAIL__SAVE_CAPABILITIES__BUILDER_HPP_
