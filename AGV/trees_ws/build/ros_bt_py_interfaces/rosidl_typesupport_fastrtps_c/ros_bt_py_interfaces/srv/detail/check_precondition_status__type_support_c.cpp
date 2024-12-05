// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ros_bt_py_interfaces:srv/CheckPreconditionStatus.idl
// generated code does not contain a copyright notice
#include "ros_bt_py_interfaces/srv/detail/check_precondition_status__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ros_bt_py_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ros_bt_py_interfaces/srv/detail/check_precondition_status__struct.h"
#include "ros_bt_py_interfaces/srv/detail/check_precondition_status__functions.h"
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

#include "ros_bt_py_interfaces/msg/detail/capability_interface__functions.h"  // interface

// forward declare type support functions
size_t get_serialized_size_ros_bt_py_interfaces__msg__CapabilityInterface(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ros_bt_py_interfaces__msg__CapabilityInterface(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, CapabilityInterface)();


using _CheckPreconditionStatus_Request__ros_msg_type = ros_bt_py_interfaces__srv__CheckPreconditionStatus_Request;

static bool _CheckPreconditionStatus_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _CheckPreconditionStatus_Request__ros_msg_type * ros_message = static_cast<const _CheckPreconditionStatus_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: interface
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, CapabilityInterface
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->interface, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _CheckPreconditionStatus_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _CheckPreconditionStatus_Request__ros_msg_type * ros_message = static_cast<_CheckPreconditionStatus_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: interface
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, CapabilityInterface
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->interface))
    {
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t get_serialized_size_ros_bt_py_interfaces__srv__CheckPreconditionStatus_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _CheckPreconditionStatus_Request__ros_msg_type * ros_message = static_cast<const _CheckPreconditionStatus_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name interface

  current_alignment += get_serialized_size_ros_bt_py_interfaces__msg__CapabilityInterface(
    &(ros_message->interface), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _CheckPreconditionStatus_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ros_bt_py_interfaces__srv__CheckPreconditionStatus_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t max_serialized_size_ros_bt_py_interfaces__srv__CheckPreconditionStatus_Request(
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

  // member: interface
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_ros_bt_py_interfaces__msg__CapabilityInterface(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ros_bt_py_interfaces__srv__CheckPreconditionStatus_Request;
    is_plain =
      (
      offsetof(DataType, interface) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _CheckPreconditionStatus_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ros_bt_py_interfaces__srv__CheckPreconditionStatus_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_CheckPreconditionStatus_Request = {
  "ros_bt_py_interfaces::srv",
  "CheckPreconditionStatus_Request",
  _CheckPreconditionStatus_Request__cdr_serialize,
  _CheckPreconditionStatus_Request__cdr_deserialize,
  _CheckPreconditionStatus_Request__get_serialized_size,
  _CheckPreconditionStatus_Request__max_serialized_size
};

static rosidl_message_type_support_t _CheckPreconditionStatus_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_CheckPreconditionStatus_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, CheckPreconditionStatus_Request)() {
  return &_CheckPreconditionStatus_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "ros_bt_py_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/check_precondition_status__struct.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/check_precondition_status__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

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


using _CheckPreconditionStatus_Response__ros_msg_type = ros_bt_py_interfaces__srv__CheckPreconditionStatus_Response;

static bool _CheckPreconditionStatus_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _CheckPreconditionStatus_Response__ros_msg_type * ros_message = static_cast<const _CheckPreconditionStatus_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: available
  {
    cdr << (ros_message->available ? true : false);
  }

  return true;
}

static bool _CheckPreconditionStatus_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _CheckPreconditionStatus_Response__ros_msg_type * ros_message = static_cast<_CheckPreconditionStatus_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: available
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->available = tmp ? true : false;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t get_serialized_size_ros_bt_py_interfaces__srv__CheckPreconditionStatus_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _CheckPreconditionStatus_Response__ros_msg_type * ros_message = static_cast<const _CheckPreconditionStatus_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name available
  {
    size_t item_size = sizeof(ros_message->available);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _CheckPreconditionStatus_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ros_bt_py_interfaces__srv__CheckPreconditionStatus_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t max_serialized_size_ros_bt_py_interfaces__srv__CheckPreconditionStatus_Response(
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

  // member: available
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ros_bt_py_interfaces__srv__CheckPreconditionStatus_Response;
    is_plain =
      (
      offsetof(DataType, available) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _CheckPreconditionStatus_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ros_bt_py_interfaces__srv__CheckPreconditionStatus_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_CheckPreconditionStatus_Response = {
  "ros_bt_py_interfaces::srv",
  "CheckPreconditionStatus_Response",
  _CheckPreconditionStatus_Response__cdr_serialize,
  _CheckPreconditionStatus_Response__cdr_deserialize,
  _CheckPreconditionStatus_Response__get_serialized_size,
  _CheckPreconditionStatus_Response__max_serialized_size
};

static rosidl_message_type_support_t _CheckPreconditionStatus_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_CheckPreconditionStatus_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, CheckPreconditionStatus_Response)() {
  return &_CheckPreconditionStatus_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "ros_bt_py_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ros_bt_py_interfaces/srv/check_precondition_status.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t CheckPreconditionStatus__callbacks = {
  "ros_bt_py_interfaces::srv",
  "CheckPreconditionStatus",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, CheckPreconditionStatus_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, CheckPreconditionStatus_Response)(),
};

static rosidl_service_type_support_t CheckPreconditionStatus__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &CheckPreconditionStatus__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, CheckPreconditionStatus)() {
  return &CheckPreconditionStatus__handle;
}

#if defined(__cplusplus)
}
#endif
