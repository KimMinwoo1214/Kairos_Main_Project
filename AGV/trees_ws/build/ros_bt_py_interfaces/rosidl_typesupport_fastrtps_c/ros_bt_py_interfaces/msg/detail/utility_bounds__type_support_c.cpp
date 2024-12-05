// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ros_bt_py_interfaces:msg/UtilityBounds.idl
// generated code does not contain a copyright notice
#include "ros_bt_py_interfaces/msg/detail/utility_bounds__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ros_bt_py_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ros_bt_py_interfaces/msg/detail/utility_bounds__struct.h"
#include "ros_bt_py_interfaces/msg/detail/utility_bounds__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _UtilityBounds__ros_msg_type = ros_bt_py_interfaces__msg__UtilityBounds;

static bool _UtilityBounds__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _UtilityBounds__ros_msg_type * ros_message = static_cast<const _UtilityBounds__ros_msg_type *>(untyped_ros_message);
  // Field name: can_execute
  {
    cdr << (ros_message->can_execute ? true : false);
  }

  // Field name: has_upper_bound_success
  {
    cdr << (ros_message->has_upper_bound_success ? true : false);
  }

  // Field name: upper_bound_success
  {
    cdr << ros_message->upper_bound_success;
  }

  // Field name: has_lower_bound_success
  {
    cdr << (ros_message->has_lower_bound_success ? true : false);
  }

  // Field name: lower_bound_success
  {
    cdr << ros_message->lower_bound_success;
  }

  // Field name: has_upper_bound_failure
  {
    cdr << (ros_message->has_upper_bound_failure ? true : false);
  }

  // Field name: upper_bound_failure
  {
    cdr << ros_message->upper_bound_failure;
  }

  // Field name: has_lower_bound_failure
  {
    cdr << (ros_message->has_lower_bound_failure ? true : false);
  }

  // Field name: lower_bound_failure
  {
    cdr << ros_message->lower_bound_failure;
  }

  return true;
}

static bool _UtilityBounds__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _UtilityBounds__ros_msg_type * ros_message = static_cast<_UtilityBounds__ros_msg_type *>(untyped_ros_message);
  // Field name: can_execute
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->can_execute = tmp ? true : false;
  }

  // Field name: has_upper_bound_success
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->has_upper_bound_success = tmp ? true : false;
  }

  // Field name: upper_bound_success
  {
    cdr >> ros_message->upper_bound_success;
  }

  // Field name: has_lower_bound_success
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->has_lower_bound_success = tmp ? true : false;
  }

  // Field name: lower_bound_success
  {
    cdr >> ros_message->lower_bound_success;
  }

  // Field name: has_upper_bound_failure
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->has_upper_bound_failure = tmp ? true : false;
  }

  // Field name: upper_bound_failure
  {
    cdr >> ros_message->upper_bound_failure;
  }

  // Field name: has_lower_bound_failure
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->has_lower_bound_failure = tmp ? true : false;
  }

  // Field name: lower_bound_failure
  {
    cdr >> ros_message->lower_bound_failure;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t get_serialized_size_ros_bt_py_interfaces__msg__UtilityBounds(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _UtilityBounds__ros_msg_type * ros_message = static_cast<const _UtilityBounds__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name can_execute
  {
    size_t item_size = sizeof(ros_message->can_execute);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name has_upper_bound_success
  {
    size_t item_size = sizeof(ros_message->has_upper_bound_success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name upper_bound_success
  {
    size_t item_size = sizeof(ros_message->upper_bound_success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name has_lower_bound_success
  {
    size_t item_size = sizeof(ros_message->has_lower_bound_success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name lower_bound_success
  {
    size_t item_size = sizeof(ros_message->lower_bound_success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name has_upper_bound_failure
  {
    size_t item_size = sizeof(ros_message->has_upper_bound_failure);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name upper_bound_failure
  {
    size_t item_size = sizeof(ros_message->upper_bound_failure);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name has_lower_bound_failure
  {
    size_t item_size = sizeof(ros_message->has_lower_bound_failure);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name lower_bound_failure
  {
    size_t item_size = sizeof(ros_message->lower_bound_failure);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _UtilityBounds__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ros_bt_py_interfaces__msg__UtilityBounds(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t max_serialized_size_ros_bt_py_interfaces__msg__UtilityBounds(
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

  // member: can_execute
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: has_upper_bound_success
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: upper_bound_success
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: has_lower_bound_success
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: lower_bound_success
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: has_upper_bound_failure
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: upper_bound_failure
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: has_lower_bound_failure
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: lower_bound_failure
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
    using DataType = ros_bt_py_interfaces__msg__UtilityBounds;
    is_plain =
      (
      offsetof(DataType, lower_bound_failure) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _UtilityBounds__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ros_bt_py_interfaces__msg__UtilityBounds(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_UtilityBounds = {
  "ros_bt_py_interfaces::msg",
  "UtilityBounds",
  _UtilityBounds__cdr_serialize,
  _UtilityBounds__cdr_deserialize,
  _UtilityBounds__get_serialized_size,
  _UtilityBounds__max_serialized_size
};

static rosidl_message_type_support_t _UtilityBounds__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_UtilityBounds,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, UtilityBounds)() {
  return &_UtilityBounds__type_support;
}

#if defined(__cplusplus)
}
#endif
