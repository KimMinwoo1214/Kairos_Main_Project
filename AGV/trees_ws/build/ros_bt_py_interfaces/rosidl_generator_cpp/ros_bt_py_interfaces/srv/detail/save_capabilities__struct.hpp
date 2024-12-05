// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ros_bt_py_interfaces:srv/SaveCapabilities.idl
// generated code does not contain a copyright notice

#ifndef ROS_BT_PY_INTERFACES__SRV__DETAIL__SAVE_CAPABILITIES__STRUCT_HPP_
#define ROS_BT_PY_INTERFACES__SRV__DETAIL__SAVE_CAPABILITIES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__ros_bt_py_interfaces__srv__SaveCapabilities_Request __attribute__((deprecated))
#else
# define DEPRECATED__ros_bt_py_interfaces__srv__SaveCapabilities_Request __declspec(deprecated)
#endif

namespace ros_bt_py_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SaveCapabilities_Request_
{
  using Type = SaveCapabilities_Request_<ContainerAllocator>;

  explicit SaveCapabilities_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->package = "";
    }
  }

  explicit SaveCapabilities_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : package(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->package = "";
    }
  }

  // field types and members
  using _package_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _package_type package;

  // setters for named parameter idiom
  Type & set__package(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->package = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros_bt_py_interfaces::srv::SaveCapabilities_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros_bt_py_interfaces::srv::SaveCapabilities_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::srv::SaveCapabilities_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::srv::SaveCapabilities_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros_bt_py_interfaces__srv__SaveCapabilities_Request
    std::shared_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros_bt_py_interfaces__srv__SaveCapabilities_Request
    std::shared_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SaveCapabilities_Request_ & other) const
  {
    if (this->package != other.package) {
      return false;
    }
    return true;
  }
  bool operator!=(const SaveCapabilities_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SaveCapabilities_Request_

// alias to use template instance with default allocator
using SaveCapabilities_Request =
  ros_bt_py_interfaces::srv::SaveCapabilities_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ros_bt_py_interfaces


#ifndef _WIN32
# define DEPRECATED__ros_bt_py_interfaces__srv__SaveCapabilities_Response __attribute__((deprecated))
#else
# define DEPRECATED__ros_bt_py_interfaces__srv__SaveCapabilities_Response __declspec(deprecated)
#endif

namespace ros_bt_py_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SaveCapabilities_Response_
{
  using Type = SaveCapabilities_Response_<ContainerAllocator>;

  explicit SaveCapabilities_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->error_message = "";
    }
  }

  explicit SaveCapabilities_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : error_message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->error_message = "";
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _error_message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _error_message_type error_message;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__error_message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->error_message = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros_bt_py_interfaces::srv::SaveCapabilities_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros_bt_py_interfaces::srv::SaveCapabilities_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::srv::SaveCapabilities_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::srv::SaveCapabilities_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros_bt_py_interfaces__srv__SaveCapabilities_Response
    std::shared_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros_bt_py_interfaces__srv__SaveCapabilities_Response
    std::shared_ptr<ros_bt_py_interfaces::srv::SaveCapabilities_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SaveCapabilities_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->error_message != other.error_message) {
      return false;
    }
    return true;
  }
  bool operator!=(const SaveCapabilities_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SaveCapabilities_Response_

// alias to use template instance with default allocator
using SaveCapabilities_Response =
  ros_bt_py_interfaces::srv::SaveCapabilities_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ros_bt_py_interfaces

namespace ros_bt_py_interfaces
{

namespace srv
{

struct SaveCapabilities
{
  using Request = ros_bt_py_interfaces::srv::SaveCapabilities_Request;
  using Response = ros_bt_py_interfaces::srv::SaveCapabilities_Response;
};

}  // namespace srv

}  // namespace ros_bt_py_interfaces

#endif  // ROS_BT_PY_INTERFACES__SRV__DETAIL__SAVE_CAPABILITIES__STRUCT_HPP_
