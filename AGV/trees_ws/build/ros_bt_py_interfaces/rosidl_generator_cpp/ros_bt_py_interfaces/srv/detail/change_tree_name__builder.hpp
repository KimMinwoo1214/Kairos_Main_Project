// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ros_bt_py_interfaces:srv/ChangeTreeName.idl
// generated code does not contain a copyright notice

#ifndef ROS_BT_PY_INTERFACES__SRV__DETAIL__CHANGE_TREE_NAME__BUILDER_HPP_
#define ROS_BT_PY_INTERFACES__SRV__DETAIL__CHANGE_TREE_NAME__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ros_bt_py_interfaces/srv/detail/change_tree_name__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ros_bt_py_interfaces
{

namespace srv
{

namespace builder
{

class Init_ChangeTreeName_Request_name
{
public:
  Init_ChangeTreeName_Request_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ros_bt_py_interfaces::srv::ChangeTreeName_Request name(::ros_bt_py_interfaces::srv::ChangeTreeName_Request::_name_type arg)
  {
    msg_.name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros_bt_py_interfaces::srv::ChangeTreeName_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros_bt_py_interfaces::srv::ChangeTreeName_Request>()
{
  return ros_bt_py_interfaces::srv::builder::Init_ChangeTreeName_Request_name();
}

}  // namespace ros_bt_py_interfaces


namespace ros_bt_py_interfaces
{

namespace srv
{

namespace builder
{

class Init_ChangeTreeName_Response_error_message
{
public:
  explicit Init_ChangeTreeName_Response_error_message(::ros_bt_py_interfaces::srv::ChangeTreeName_Response & msg)
  : msg_(msg)
  {}
  ::ros_bt_py_interfaces::srv::ChangeTreeName_Response error_message(::ros_bt_py_interfaces::srv::ChangeTreeName_Response::_error_message_type arg)
  {
    msg_.error_message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros_bt_py_interfaces::srv::ChangeTreeName_Response msg_;
};

class Init_ChangeTreeName_Response_success
{
public:
  Init_ChangeTreeName_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ChangeTreeName_Response_error_message success(::ros_bt_py_interfaces::srv::ChangeTreeName_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_ChangeTreeName_Response_error_message(msg_);
  }

private:
  ::ros_bt_py_interfaces::srv::ChangeTreeName_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros_bt_py_interfaces::srv::ChangeTreeName_Response>()
{
  return ros_bt_py_interfaces::srv::builder::Init_ChangeTreeName_Response_success();
}

}  // namespace ros_bt_py_interfaces

#endif  // ROS_BT_PY_INTERFACES__SRV__DETAIL__CHANGE_TREE_NAME__BUILDER_HPP_