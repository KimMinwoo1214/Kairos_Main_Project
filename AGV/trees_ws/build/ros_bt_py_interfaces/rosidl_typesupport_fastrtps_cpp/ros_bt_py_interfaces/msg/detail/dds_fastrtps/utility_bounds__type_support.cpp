// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from ros_bt_py_interfaces:msg/UtilityBounds.idl
// generated code does not contain a copyright notice
#include "ros_bt_py_interfaces/msg/detail/utility_bounds__rosidl_typesupport_fastrtps_cpp.hpp"
#include "ros_bt_py_interfaces/msg/detail/utility_bounds__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace ros_bt_py_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
cdr_serialize(
  const ros_bt_py_interfaces::msg::UtilityBounds & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: can_execute
  cdr << (ros_message.can_execute ? true : false);
  // Member: has_upper_bound_success
  cdr << (ros_message.has_upper_bound_success ? true : false);
  // Member: upper_bound_success
  cdr << ros_message.upper_bound_success;
  // Member: has_lower_bound_success
  cdr << (ros_message.has_lower_bound_success ? true : false);
  // Member: lower_bound_success
  cdr << ros_message.lower_bound_success;
  // Member: has_upper_bound_failure
  cdr << (ros_message.has_upper_bound_failure ? true : false);
  // Member: upper_bound_failure
  cdr << ros_message.upper_bound_failure;
  // Member: has_lower_bound_failure
  cdr << (ros_message.has_lower_bound_failure ? true : false);
  // Member: lower_bound_failure
  cdr << ros_message.lower_bound_failure;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ros_bt_py_interfaces::msg::UtilityBounds & ros_message)
{
  // Member: can_execute
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.can_execute = tmp ? true : false;
  }

  // Member: has_upper_bound_success
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.has_upper_bound_success = tmp ? true : false;
  }

  // Member: upper_bound_success
  cdr >> ros_message.upper_bound_success;

  // Member: has_lower_bound_success
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.has_lower_bound_success = tmp ? true : false;
  }

  // Member: lower_bound_success
  cdr >> ros_message.lower_bound_success;

  // Member: has_upper_bound_failure
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.has_upper_bound_failure = tmp ? true : false;
  }

  // Member: upper_bound_failure
  cdr >> ros_message.upper_bound_failure;

  // Member: has_lower_bound_failure
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.has_lower_bound_failure = tmp ? true : false;
  }

  // Member: lower_bound_failure
  cdr >> ros_message.lower_bound_failure;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
get_serialized_size(
  const ros_bt_py_interfaces::msg::UtilityBounds & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: can_execute
  {
    size_t item_size = sizeof(ros_message.can_execute);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: has_upper_bound_success
  {
    size_t item_size = sizeof(ros_message.has_upper_bound_success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: upper_bound_success
  {
    size_t item_size = sizeof(ros_message.upper_bound_success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: has_lower_bound_success
  {
    size_t item_size = sizeof(ros_message.has_lower_bound_success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: lower_bound_success
  {
    size_t item_size = sizeof(ros_message.lower_bound_success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: has_upper_bound_failure
  {
    size_t item_size = sizeof(ros_message.has_upper_bound_failure);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: upper_bound_failure
  {
    size_t item_size = sizeof(ros_message.upper_bound_failure);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: has_lower_bound_failure
  {
    size_t item_size = sizeof(ros_message.has_lower_bound_failure);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: lower_bound_failure
  {
    size_t item_size = sizeof(ros_message.lower_bound_failure);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
max_serialized_size_UtilityBounds(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: can_execute
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: has_upper_bound_success
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: upper_bound_success
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: has_lower_bound_success
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: lower_bound_success
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: has_upper_bound_failure
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: upper_bound_failure
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: has_lower_bound_failure
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: lower_bound_failure
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ros_bt_py_interfaces::msg::UtilityBounds;
    is_plain =
      (
      offsetof(DataType, lower_bound_failure) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _UtilityBounds__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ros_bt_py_interfaces::msg::UtilityBounds *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _UtilityBounds__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ros_bt_py_interfaces::msg::UtilityBounds *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _UtilityBounds__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ros_bt_py_interfaces::msg::UtilityBounds *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _UtilityBounds__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_UtilityBounds(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _UtilityBounds__callbacks = {
  "ros_bt_py_interfaces::msg",
  "UtilityBounds",
  _UtilityBounds__cdr_serialize,
  _UtilityBounds__cdr_deserialize,
  _UtilityBounds__get_serialized_size,
  _UtilityBounds__max_serialized_size
};

static rosidl_message_type_support_t _UtilityBounds__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_UtilityBounds__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace ros_bt_py_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_ros_bt_py_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<ros_bt_py_interfaces::msg::UtilityBounds>()
{
  return &ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::_UtilityBounds__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, msg, UtilityBounds)() {
  return &ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::_UtilityBounds__handle;
}

#ifdef __cplusplus
}
#endif
