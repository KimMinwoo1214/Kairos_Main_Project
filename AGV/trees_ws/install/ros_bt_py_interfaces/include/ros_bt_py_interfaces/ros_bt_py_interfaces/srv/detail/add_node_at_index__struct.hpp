// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ros_bt_py_interfaces:srv/AddNodeAtIndex.idl
// generated code does not contain a copyright notice

#ifndef ROS_BT_PY_INTERFACES__SRV__DETAIL__ADD_NODE_AT_INDEX__STRUCT_HPP_
#define ROS_BT_PY_INTERFACES__SRV__DETAIL__ADD_NODE_AT_INDEX__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'node'
#include "ros_bt_py_interfaces/msg/detail/node__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ros_bt_py_interfaces__srv__AddNodeAtIndex_Request __attribute__((deprecated))
#else
# define DEPRECATED__ros_bt_py_interfaces__srv__AddNodeAtIndex_Request __declspec(deprecated)
#endif

namespace ros_bt_py_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AddNodeAtIndex_Request_
{
  using Type = AddNodeAtIndex_Request_<ContainerAllocator>;

  explicit AddNodeAtIndex_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : node(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->parent_name = "";
      this->allow_rename = false;
      this->new_child_index = 0l;
    }
  }

  explicit AddNodeAtIndex_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : parent_name(_alloc),
    node(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->parent_name = "";
      this->allow_rename = false;
      this->new_child_index = 0l;
    }
  }

  // field types and members
  using _parent_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _parent_name_type parent_name;
  using _node_type =
    ros_bt_py_interfaces::msg::Node_<ContainerAllocator>;
  _node_type node;
  using _allow_rename_type =
    bool;
  _allow_rename_type allow_rename;
  using _new_child_index_type =
    int32_t;
  _new_child_index_type new_child_index;

  // setters for named parameter idiom
  Type & set__parent_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->parent_name = _arg;
    return *this;
  }
  Type & set__node(
    const ros_bt_py_interfaces::msg::Node_<ContainerAllocator> & _arg)
  {
    this->node = _arg;
    return *this;
  }
  Type & set__allow_rename(
    const bool & _arg)
  {
    this->allow_rename = _arg;
    return *this;
  }
  Type & set__new_child_index(
    const int32_t & _arg)
  {
    this->new_child_index = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros_bt_py_interfaces::srv::AddNodeAtIndex_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros_bt_py_interfaces::srv::AddNodeAtIndex_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::srv::AddNodeAtIndex_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::srv::AddNodeAtIndex_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros_bt_py_interfaces__srv__AddNodeAtIndex_Request
    std::shared_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros_bt_py_interfaces__srv__AddNodeAtIndex_Request
    std::shared_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AddNodeAtIndex_Request_ & other) const
  {
    if (this->parent_name != other.parent_name) {
      return false;
    }
    if (this->node != other.node) {
      return false;
    }
    if (this->allow_rename != other.allow_rename) {
      return false;
    }
    if (this->new_child_index != other.new_child_index) {
      return false;
    }
    return true;
  }
  bool operator!=(const AddNodeAtIndex_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AddNodeAtIndex_Request_

// alias to use template instance with default allocator
using AddNodeAtIndex_Request =
  ros_bt_py_interfaces::srv::AddNodeAtIndex_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ros_bt_py_interfaces


#ifndef _WIN32
# define DEPRECATED__ros_bt_py_interfaces__srv__AddNodeAtIndex_Response __attribute__((deprecated))
#else
# define DEPRECATED__ros_bt_py_interfaces__srv__AddNodeAtIndex_Response __declspec(deprecated)
#endif

namespace ros_bt_py_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AddNodeAtIndex_Response_
{
  using Type = AddNodeAtIndex_Response_<ContainerAllocator>;

  explicit AddNodeAtIndex_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->actual_node_name = "";
      this->error_message = "";
    }
  }

  explicit AddNodeAtIndex_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : actual_node_name(_alloc),
    error_message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->actual_node_name = "";
      this->error_message = "";
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _actual_node_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _actual_node_name_type actual_node_name;
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
  Type & set__actual_node_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->actual_node_name = _arg;
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
    ros_bt_py_interfaces::srv::AddNodeAtIndex_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros_bt_py_interfaces::srv::AddNodeAtIndex_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::srv::AddNodeAtIndex_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::srv::AddNodeAtIndex_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros_bt_py_interfaces__srv__AddNodeAtIndex_Response
    std::shared_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros_bt_py_interfaces__srv__AddNodeAtIndex_Response
    std::shared_ptr<ros_bt_py_interfaces::srv::AddNodeAtIndex_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AddNodeAtIndex_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->actual_node_name != other.actual_node_name) {
      return false;
    }
    if (this->error_message != other.error_message) {
      return false;
    }
    return true;
  }
  bool operator!=(const AddNodeAtIndex_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AddNodeAtIndex_Response_

// alias to use template instance with default allocator
using AddNodeAtIndex_Response =
  ros_bt_py_interfaces::srv::AddNodeAtIndex_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ros_bt_py_interfaces

namespace ros_bt_py_interfaces
{

namespace srv
{

struct AddNodeAtIndex
{
  using Request = ros_bt_py_interfaces::srv::AddNodeAtIndex_Request;
  using Response = ros_bt_py_interfaces::srv::AddNodeAtIndex_Response;
};

}  // namespace srv

}  // namespace ros_bt_py_interfaces

#endif  // ROS_BT_PY_INTERFACES__SRV__DETAIL__ADD_NODE_AT_INDEX__STRUCT_HPP_
