// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ros_bt_py_interfaces:msg/PingMsg.idl
// generated code does not contain a copyright notice

#ifndef ROS_BT_PY_INTERFACES__MSG__DETAIL__PING_MSG__STRUCT_HPP_
#define ROS_BT_PY_INTERFACES__MSG__DETAIL__PING_MSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ros_bt_py_interfaces__msg__PingMsg __attribute__((deprecated))
#else
# define DEPRECATED__ros_bt_py_interfaces__msg__PingMsg __declspec(deprecated)
#endif

namespace ros_bt_py_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct PingMsg_
{
  using Type = PingMsg_<ContainerAllocator>;

  explicit PingMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : timestamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->node_id = "";
    }
  }

  explicit PingMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : node_id(_alloc),
    timestamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->node_id = "";
    }
  }

  // field types and members
  using _node_id_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _node_id_type node_id;
  using _timestamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _timestamp_type timestamp;

  // setters for named parameter idiom
  Type & set__node_id(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->node_id = _arg;
    return *this;
  }
  Type & set__timestamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros_bt_py_interfaces::msg::PingMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros_bt_py_interfaces::msg::PingMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::msg::PingMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::msg::PingMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::msg::PingMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::msg::PingMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::msg::PingMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::msg::PingMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::msg::PingMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::msg::PingMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros_bt_py_interfaces__msg__PingMsg
    std::shared_ptr<ros_bt_py_interfaces::msg::PingMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros_bt_py_interfaces__msg__PingMsg
    std::shared_ptr<ros_bt_py_interfaces::msg::PingMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PingMsg_ & other) const
  {
    if (this->node_id != other.node_id) {
      return false;
    }
    if (this->timestamp != other.timestamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const PingMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PingMsg_

// alias to use template instance with default allocator
using PingMsg =
  ros_bt_py_interfaces::msg::PingMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ros_bt_py_interfaces

#endif  // ROS_BT_PY_INTERFACES__MSG__DETAIL__PING_MSG__STRUCT_HPP_