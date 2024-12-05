// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ros_bt_py_interfaces:action/FindBestExecutor.idl
// generated code does not contain a copyright notice

#ifndef ROS_BT_PY_INTERFACES__ACTION__DETAIL__FIND_BEST_EXECUTOR__TRAITS_HPP_
#define ROS_BT_PY_INTERFACES__ACTION__DETAIL__FIND_BEST_EXECUTOR__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'tree'
#include "ros_bt_py_interfaces/msg/detail/tree__traits.hpp"

namespace ros_bt_py_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const FindBestExecutor_Goal & msg,
  std::ostream & out)
{
  out << "{";
  // member: tree
  {
    out << "tree: ";
    to_flow_style_yaml(msg.tree, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FindBestExecutor_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: tree
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tree:\n";
    to_block_style_yaml(msg.tree, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FindBestExecutor_Goal & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use ros_bt_py_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ros_bt_py_interfaces::action::FindBestExecutor_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros_bt_py_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros_bt_py_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const ros_bt_py_interfaces::action::FindBestExecutor_Goal & msg)
{
  return ros_bt_py_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<ros_bt_py_interfaces::action::FindBestExecutor_Goal>()
{
  return "ros_bt_py_interfaces::action::FindBestExecutor_Goal";
}

template<>
inline const char * name<ros_bt_py_interfaces::action::FindBestExecutor_Goal>()
{
  return "ros_bt_py_interfaces/action/FindBestExecutor_Goal";
}

template<>
struct has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_Goal>
  : std::integral_constant<bool, has_fixed_size<ros_bt_py_interfaces::msg::Tree>::value> {};

template<>
struct has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_Goal>
  : std::integral_constant<bool, has_bounded_size<ros_bt_py_interfaces::msg::Tree>::value> {};

template<>
struct is_message<ros_bt_py_interfaces::action::FindBestExecutor_Goal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace ros_bt_py_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const FindBestExecutor_Result & msg,
  std::ostream & out)
{
  out << "{";
  // member: local_is_best
  {
    out << "local_is_best: ";
    rosidl_generator_traits::value_to_yaml(msg.local_is_best, out);
    out << ", ";
  }

  // member: best_executor_namespace
  {
    out << "best_executor_namespace: ";
    rosidl_generator_traits::value_to_yaml(msg.best_executor_namespace, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FindBestExecutor_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: local_is_best
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "local_is_best: ";
    rosidl_generator_traits::value_to_yaml(msg.local_is_best, out);
    out << "\n";
  }

  // member: best_executor_namespace
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "best_executor_namespace: ";
    rosidl_generator_traits::value_to_yaml(msg.best_executor_namespace, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FindBestExecutor_Result & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use ros_bt_py_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ros_bt_py_interfaces::action::FindBestExecutor_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros_bt_py_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros_bt_py_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const ros_bt_py_interfaces::action::FindBestExecutor_Result & msg)
{
  return ros_bt_py_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<ros_bt_py_interfaces::action::FindBestExecutor_Result>()
{
  return "ros_bt_py_interfaces::action::FindBestExecutor_Result";
}

template<>
inline const char * name<ros_bt_py_interfaces::action::FindBestExecutor_Result>()
{
  return "ros_bt_py_interfaces/action/FindBestExecutor_Result";
}

template<>
struct has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_Result>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_Result>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ros_bt_py_interfaces::action::FindBestExecutor_Result>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace ros_bt_py_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const FindBestExecutor_Feedback & msg,
  std::ostream & out)
{
  out << "{";
  // member: checked_namespaces
  {
    if (msg.checked_namespaces.size() == 0) {
      out << "checked_namespaces: []";
    } else {
      out << "checked_namespaces: [";
      size_t pending_items = msg.checked_namespaces.size();
      for (auto item : msg.checked_namespaces) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FindBestExecutor_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: checked_namespaces
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.checked_namespaces.size() == 0) {
      out << "checked_namespaces: []\n";
    } else {
      out << "checked_namespaces:\n";
      for (auto item : msg.checked_namespaces) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FindBestExecutor_Feedback & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use ros_bt_py_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ros_bt_py_interfaces::action::FindBestExecutor_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros_bt_py_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros_bt_py_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const ros_bt_py_interfaces::action::FindBestExecutor_Feedback & msg)
{
  return ros_bt_py_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<ros_bt_py_interfaces::action::FindBestExecutor_Feedback>()
{
  return "ros_bt_py_interfaces::action::FindBestExecutor_Feedback";
}

template<>
inline const char * name<ros_bt_py_interfaces::action::FindBestExecutor_Feedback>()
{
  return "ros_bt_py_interfaces/action/FindBestExecutor_Feedback";
}

template<>
struct has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_Feedback>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_Feedback>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ros_bt_py_interfaces::action::FindBestExecutor_Feedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'goal'
#include "ros_bt_py_interfaces/action/detail/find_best_executor__traits.hpp"

namespace ros_bt_py_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const FindBestExecutor_SendGoal_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: goal
  {
    out << "goal: ";
    to_flow_style_yaml(msg.goal, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FindBestExecutor_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: goal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal:\n";
    to_block_style_yaml(msg.goal, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FindBestExecutor_SendGoal_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use ros_bt_py_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros_bt_py_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros_bt_py_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request & msg)
{
  return ros_bt_py_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request>()
{
  return "ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request";
}

template<>
inline const char * name<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request>()
{
  return "ros_bt_py_interfaces/action/FindBestExecutor_SendGoal_Request";
}

template<>
struct has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace ros_bt_py_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const FindBestExecutor_SendGoal_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: accepted
  {
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << ", ";
  }

  // member: stamp
  {
    out << "stamp: ";
    to_flow_style_yaml(msg.stamp, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FindBestExecutor_SendGoal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: accepted
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << "\n";
  }

  // member: stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stamp:\n";
    to_block_style_yaml(msg.stamp, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FindBestExecutor_SendGoal_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use ros_bt_py_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros_bt_py_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros_bt_py_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response & msg)
{
  return ros_bt_py_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response>()
{
  return "ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response";
}

template<>
inline const char * name<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response>()
{
  return "ros_bt_py_interfaces/action/FindBestExecutor_SendGoal_Response";
}

template<>
struct has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal>()
{
  return "ros_bt_py_interfaces::action::FindBestExecutor_SendGoal";
}

template<>
inline const char * name<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal>()
{
  return "ros_bt_py_interfaces/action/FindBestExecutor_SendGoal";
}

template<>
struct has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request>::value &&
    has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request>::value &&
    has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response>::value
  >
{
};

template<>
struct is_service<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal>
  : std::true_type
{
};

template<>
struct is_service_request<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"

namespace ros_bt_py_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const FindBestExecutor_GetResult_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FindBestExecutor_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FindBestExecutor_GetResult_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use ros_bt_py_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros_bt_py_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros_bt_py_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request & msg)
{
  return ros_bt_py_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request>()
{
  return "ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request";
}

template<>
inline const char * name<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request>()
{
  return "ros_bt_py_interfaces/action/FindBestExecutor_GetResult_Request";
}

template<>
struct has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'result'
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__traits.hpp"

namespace ros_bt_py_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const FindBestExecutor_GetResult_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << ", ";
  }

  // member: result
  {
    out << "result: ";
    to_flow_style_yaml(msg.result, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FindBestExecutor_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }

  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result:\n";
    to_block_style_yaml(msg.result, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FindBestExecutor_GetResult_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use ros_bt_py_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros_bt_py_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros_bt_py_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response & msg)
{
  return ros_bt_py_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response>()
{
  return "ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response";
}

template<>
inline const char * name<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response>()
{
  return "ros_bt_py_interfaces/action/FindBestExecutor_GetResult_Response";
}

template<>
struct has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_Result>::value> {};

template<>
struct has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_Result>::value> {};

template<>
struct is_message<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ros_bt_py_interfaces::action::FindBestExecutor_GetResult>()
{
  return "ros_bt_py_interfaces::action::FindBestExecutor_GetResult";
}

template<>
inline const char * name<ros_bt_py_interfaces::action::FindBestExecutor_GetResult>()
{
  return "ros_bt_py_interfaces/action/FindBestExecutor_GetResult";
}

template<>
struct has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request>::value &&
    has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request>::value &&
    has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response>::value
  >
{
};

template<>
struct is_service<ros_bt_py_interfaces::action::FindBestExecutor_GetResult>
  : std::true_type
{
};

template<>
struct is_service_request<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request>
  : std::true_type
{
};

template<>
struct is_service_response<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'feedback'
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__traits.hpp"

namespace ros_bt_py_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const FindBestExecutor_FeedbackMessage & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: feedback
  {
    out << "feedback: ";
    to_flow_style_yaml(msg.feedback, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FindBestExecutor_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: feedback
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "feedback:\n";
    to_block_style_yaml(msg.feedback, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FindBestExecutor_FeedbackMessage & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use ros_bt_py_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros_bt_py_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros_bt_py_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage & msg)
{
  return ros_bt_py_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage>()
{
  return "ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage";
}

template<>
inline const char * name<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage>()
{
  return "ros_bt_py_interfaces/action/FindBestExecutor_FeedbackMessage";
}

template<>
struct has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<ros_bt_py_interfaces::action::FindBestExecutor_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<ros_bt_py_interfaces::action::FindBestExecutor_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits


namespace rosidl_generator_traits
{

template<>
struct is_action<ros_bt_py_interfaces::action::FindBestExecutor>
  : std::true_type
{
};

template<>
struct is_action_goal<ros_bt_py_interfaces::action::FindBestExecutor_Goal>
  : std::true_type
{
};

template<>
struct is_action_result<ros_bt_py_interfaces::action::FindBestExecutor_Result>
  : std::true_type
{
};

template<>
struct is_action_feedback<ros_bt_py_interfaces::action::FindBestExecutor_Feedback>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits


#endif  // ROS_BT_PY_INTERFACES__ACTION__DETAIL__FIND_BEST_EXECUTOR__TRAITS_HPP_
