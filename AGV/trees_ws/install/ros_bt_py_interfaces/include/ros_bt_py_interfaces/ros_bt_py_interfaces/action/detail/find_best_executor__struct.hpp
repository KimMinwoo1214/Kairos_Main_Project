// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ros_bt_py_interfaces:action/FindBestExecutor.idl
// generated code does not contain a copyright notice

#ifndef ROS_BT_PY_INTERFACES__ACTION__DETAIL__FIND_BEST_EXECUTOR__STRUCT_HPP_
#define ROS_BT_PY_INTERFACES__ACTION__DETAIL__FIND_BEST_EXECUTOR__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'tree'
#include "ros_bt_py_interfaces/msg/detail/tree__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_Goal __attribute__((deprecated))
#else
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_Goal __declspec(deprecated)
#endif

namespace ros_bt_py_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct FindBestExecutor_Goal_
{
  using Type = FindBestExecutor_Goal_<ContainerAllocator>;

  explicit FindBestExecutor_Goal_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : tree(_init)
  {
    (void)_init;
  }

  explicit FindBestExecutor_Goal_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : tree(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _tree_type =
    ros_bt_py_interfaces::msg::Tree_<ContainerAllocator>;
  _tree_type tree;

  // setters for named parameter idiom
  Type & set__tree(
    const ros_bt_py_interfaces::msg::Tree_<ContainerAllocator> & _arg)
  {
    this->tree = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_Goal
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_Goal
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FindBestExecutor_Goal_ & other) const
  {
    if (this->tree != other.tree) {
      return false;
    }
    return true;
  }
  bool operator!=(const FindBestExecutor_Goal_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FindBestExecutor_Goal_

// alias to use template instance with default allocator
using FindBestExecutor_Goal =
  ros_bt_py_interfaces::action::FindBestExecutor_Goal_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace ros_bt_py_interfaces


#ifndef _WIN32
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_Result __attribute__((deprecated))
#else
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_Result __declspec(deprecated)
#endif

namespace ros_bt_py_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct FindBestExecutor_Result_
{
  using Type = FindBestExecutor_Result_<ContainerAllocator>;

  explicit FindBestExecutor_Result_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->local_is_best = false;
      this->best_executor_namespace = "";
    }
  }

  explicit FindBestExecutor_Result_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : best_executor_namespace(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->local_is_best = false;
      this->best_executor_namespace = "";
    }
  }

  // field types and members
  using _local_is_best_type =
    bool;
  _local_is_best_type local_is_best;
  using _best_executor_namespace_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _best_executor_namespace_type best_executor_namespace;

  // setters for named parameter idiom
  Type & set__local_is_best(
    const bool & _arg)
  {
    this->local_is_best = _arg;
    return *this;
  }
  Type & set__best_executor_namespace(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->best_executor_namespace = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_Result
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_Result
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FindBestExecutor_Result_ & other) const
  {
    if (this->local_is_best != other.local_is_best) {
      return false;
    }
    if (this->best_executor_namespace != other.best_executor_namespace) {
      return false;
    }
    return true;
  }
  bool operator!=(const FindBestExecutor_Result_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FindBestExecutor_Result_

// alias to use template instance with default allocator
using FindBestExecutor_Result =
  ros_bt_py_interfaces::action::FindBestExecutor_Result_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace ros_bt_py_interfaces


#ifndef _WIN32
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_Feedback __attribute__((deprecated))
#else
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_Feedback __declspec(deprecated)
#endif

namespace ros_bt_py_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct FindBestExecutor_Feedback_
{
  using Type = FindBestExecutor_Feedback_<ContainerAllocator>;

  explicit FindBestExecutor_Feedback_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit FindBestExecutor_Feedback_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _checked_namespaces_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _checked_namespaces_type checked_namespaces;

  // setters for named parameter idiom
  Type & set__checked_namespaces(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->checked_namespaces = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_Feedback
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_Feedback
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FindBestExecutor_Feedback_ & other) const
  {
    if (this->checked_namespaces != other.checked_namespaces) {
      return false;
    }
    return true;
  }
  bool operator!=(const FindBestExecutor_Feedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FindBestExecutor_Feedback_

// alias to use template instance with default allocator
using FindBestExecutor_Feedback =
  ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace ros_bt_py_interfaces


// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'goal'
#include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_SendGoal_Request __attribute__((deprecated))
#else
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_SendGoal_Request __declspec(deprecated)
#endif

namespace ros_bt_py_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct FindBestExecutor_SendGoal_Request_
{
  using Type = FindBestExecutor_SendGoal_Request_<ContainerAllocator>;

  explicit FindBestExecutor_SendGoal_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    goal(_init)
  {
    (void)_init;
  }

  explicit FindBestExecutor_SendGoal_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    goal(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _goal_type =
    ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator>;
  _goal_type goal;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__goal(
    const ros_bt_py_interfaces::action::FindBestExecutor_Goal_<ContainerAllocator> & _arg)
  {
    this->goal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_SendGoal_Request
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_SendGoal_Request
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FindBestExecutor_SendGoal_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->goal != other.goal) {
      return false;
    }
    return true;
  }
  bool operator!=(const FindBestExecutor_SendGoal_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FindBestExecutor_SendGoal_Request_

// alias to use template instance with default allocator
using FindBestExecutor_SendGoal_Request =
  ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace ros_bt_py_interfaces


// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_SendGoal_Response __attribute__((deprecated))
#else
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_SendGoal_Response __declspec(deprecated)
#endif

namespace ros_bt_py_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct FindBestExecutor_SendGoal_Response_
{
  using Type = FindBestExecutor_SendGoal_Response_<ContainerAllocator>;

  explicit FindBestExecutor_SendGoal_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  explicit FindBestExecutor_SendGoal_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  // field types and members
  using _accepted_type =
    bool;
  _accepted_type accepted;
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;

  // setters for named parameter idiom
  Type & set__accepted(
    const bool & _arg)
  {
    this->accepted = _arg;
    return *this;
  }
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_SendGoal_Response
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_SendGoal_Response
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FindBestExecutor_SendGoal_Response_ & other) const
  {
    if (this->accepted != other.accepted) {
      return false;
    }
    if (this->stamp != other.stamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const FindBestExecutor_SendGoal_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FindBestExecutor_SendGoal_Response_

// alias to use template instance with default allocator
using FindBestExecutor_SendGoal_Response =
  ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace ros_bt_py_interfaces
{

namespace action
{

struct FindBestExecutor_SendGoal
{
  using Request = ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request;
  using Response = ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response;
};

}  // namespace action

}  // namespace ros_bt_py_interfaces


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_GetResult_Request __attribute__((deprecated))
#else
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_GetResult_Request __declspec(deprecated)
#endif

namespace ros_bt_py_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct FindBestExecutor_GetResult_Request_
{
  using Type = FindBestExecutor_GetResult_Request_<ContainerAllocator>;

  explicit FindBestExecutor_GetResult_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init)
  {
    (void)_init;
  }

  explicit FindBestExecutor_GetResult_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_GetResult_Request
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_GetResult_Request
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FindBestExecutor_GetResult_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const FindBestExecutor_GetResult_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FindBestExecutor_GetResult_Request_

// alias to use template instance with default allocator
using FindBestExecutor_GetResult_Request =
  ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace ros_bt_py_interfaces


// Include directives for member types
// Member 'result'
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_GetResult_Response __attribute__((deprecated))
#else
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_GetResult_Response __declspec(deprecated)
#endif

namespace ros_bt_py_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct FindBestExecutor_GetResult_Response_
{
  using Type = FindBestExecutor_GetResult_Response_<ContainerAllocator>;

  explicit FindBestExecutor_GetResult_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  explicit FindBestExecutor_GetResult_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  // field types and members
  using _status_type =
    int8_t;
  _status_type status;
  using _result_type =
    ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator>;
  _result_type result;

  // setters for named parameter idiom
  Type & set__status(
    const int8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__result(
    const ros_bt_py_interfaces::action::FindBestExecutor_Result_<ContainerAllocator> & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_GetResult_Response
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_GetResult_Response
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FindBestExecutor_GetResult_Response_ & other) const
  {
    if (this->status != other.status) {
      return false;
    }
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const FindBestExecutor_GetResult_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FindBestExecutor_GetResult_Response_

// alias to use template instance with default allocator
using FindBestExecutor_GetResult_Response =
  ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace ros_bt_py_interfaces
{

namespace action
{

struct FindBestExecutor_GetResult
{
  using Request = ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request;
  using Response = ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response;
};

}  // namespace action

}  // namespace ros_bt_py_interfaces


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'feedback'
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_FeedbackMessage __attribute__((deprecated))
#else
# define DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_FeedbackMessage __declspec(deprecated)
#endif

namespace ros_bt_py_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct FindBestExecutor_FeedbackMessage_
{
  using Type = FindBestExecutor_FeedbackMessage_<ContainerAllocator>;

  explicit FindBestExecutor_FeedbackMessage_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    feedback(_init)
  {
    (void)_init;
  }

  explicit FindBestExecutor_FeedbackMessage_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    feedback(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _feedback_type =
    ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator>;
  _feedback_type feedback;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__feedback(
    const ros_bt_py_interfaces::action::FindBestExecutor_Feedback_<ContainerAllocator> & _arg)
  {
    this->feedback = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_FeedbackMessage
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros_bt_py_interfaces__action__FindBestExecutor_FeedbackMessage
    std::shared_ptr<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FindBestExecutor_FeedbackMessage_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->feedback != other.feedback) {
      return false;
    }
    return true;
  }
  bool operator!=(const FindBestExecutor_FeedbackMessage_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FindBestExecutor_FeedbackMessage_

// alias to use template instance with default allocator
using FindBestExecutor_FeedbackMessage =
  ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace ros_bt_py_interfaces

#include "action_msgs/srv/cancel_goal.hpp"
#include "action_msgs/msg/goal_info.hpp"
#include "action_msgs/msg/goal_status_array.hpp"

namespace ros_bt_py_interfaces
{

namespace action
{

struct FindBestExecutor
{
  /// The goal message defined in the action definition.
  using Goal = ros_bt_py_interfaces::action::FindBestExecutor_Goal;
  /// The result message defined in the action definition.
  using Result = ros_bt_py_interfaces::action::FindBestExecutor_Result;
  /// The feedback message defined in the action definition.
  using Feedback = ros_bt_py_interfaces::action::FindBestExecutor_Feedback;

  struct Impl
  {
    /// The send_goal service using a wrapped version of the goal message as a request.
    using SendGoalService = ros_bt_py_interfaces::action::FindBestExecutor_SendGoal;
    /// The get_result service using a wrapped version of the result message as a response.
    using GetResultService = ros_bt_py_interfaces::action::FindBestExecutor_GetResult;
    /// The feedback message with generic fields which wraps the feedback message.
    using FeedbackMessage = ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage;

    /// The generic service to cancel a goal.
    using CancelGoalService = action_msgs::srv::CancelGoal;
    /// The generic message for the status of a goal.
    using GoalStatusMessage = action_msgs::msg::GoalStatusArray;
  };
};

typedef struct FindBestExecutor FindBestExecutor;

}  // namespace action

}  // namespace ros_bt_py_interfaces

#endif  // ROS_BT_PY_INTERFACES__ACTION__DETAIL__FIND_BEST_EXECUTOR__STRUCT_HPP_
