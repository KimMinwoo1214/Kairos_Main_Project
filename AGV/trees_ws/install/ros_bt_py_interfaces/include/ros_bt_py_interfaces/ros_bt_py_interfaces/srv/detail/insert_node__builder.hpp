// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ros_bt_py_interfaces:srv/InsertNode.idl
// generated code does not contain a copyright notice

#ifndef ROS_BT_PY_INTERFACES__SRV__DETAIL__INSERT_NODE__BUILDER_HPP_
#define ROS_BT_PY_INTERFACES__SRV__DETAIL__INSERT_NODE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ros_bt_py_interfaces/srv/detail/insert_node__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ros_bt_py_interfaces
{

namespace srv
{

namespace builder
{

class Init_InsertNode_Request_node
{
public:
  explicit Init_InsertNode_Request_node(::ros_bt_py_interfaces::srv::InsertNode_Request & msg)
  : msg_(msg)
  {}
  ::ros_bt_py_interfaces::srv::InsertNode_Request node(::ros_bt_py_interfaces::srv::InsertNode_Request::_node_type arg)
  {
    msg_.node = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros_bt_py_interfaces::srv::InsertNode_Request msg_;
};

class Init_InsertNode_Request_previous_child_name
{
public:
  Init_InsertNode_Request_previous_child_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InsertNode_Request_node previous_child_name(::ros_bt_py_interfaces::srv::InsertNode_Request::_previous_child_name_type arg)
  {
    msg_.previous_child_name = std::move(arg);
    return Init_InsertNode_Request_node(msg_);
  }

private:
  ::ros_bt_py_interfaces::srv::InsertNode_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros_bt_py_interfaces::srv::InsertNode_Request>()
{
  return ros_bt_py_interfaces::srv::builder::Init_InsertNode_Request_previous_child_name();
}

}  // namespace ros_bt_py_interfaces


namespace ros_bt_py_interfaces
{

namespace srv
{

namespace builder
{

class Init_InsertNode_Response_error_message
{
public:
  explicit Init_InsertNode_Response_error_message(::ros_bt_py_interfaces::srv::InsertNode_Response & msg)
  : msg_(msg)
  {}
  ::ros_bt_py_interfaces::srv::InsertNode_Response error_message(::ros_bt_py_interfaces::srv::InsertNode_Response::_error_message_type arg)
  {
    msg_.error_message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros_bt_py_interfaces::srv::InsertNode_Response msg_;
};

class Init_InsertNode_Response_success
{
public:
  explicit Init_InsertNode_Response_success(::ros_bt_py_interfaces::srv::InsertNode_Response & msg)
  : msg_(msg)
  {}
  Init_InsertNode_Response_error_message success(::ros_bt_py_interfaces::srv::InsertNode_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_InsertNode_Response_error_message(msg_);
  }

private:
  ::ros_bt_py_interfaces::srv::InsertNode_Response msg_;
};

class Init_InsertNode_Response_actual_node_name
{
public:
  Init_InsertNode_Response_actual_node_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InsertNode_Response_success actual_node_name(::ros_bt_py_interfaces::srv::InsertNode_Response::_actual_node_name_type arg)
  {
    msg_.actual_node_name = std::move(arg);
    return Init_InsertNode_Response_success(msg_);
  }

private:
  ::ros_bt_py_interfaces::srv::InsertNode_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros_bt_py_interfaces::srv::InsertNode_Response>()
{
  return ros_bt_py_interfaces::srv::builder::Init_InsertNode_Response_actual_node_name();
}

}  // namespace ros_bt_py_interfaces

#endif  // ROS_BT_PY_INTERFACES__SRV__DETAIL__INSERT_NODE__BUILDER_HPP_
