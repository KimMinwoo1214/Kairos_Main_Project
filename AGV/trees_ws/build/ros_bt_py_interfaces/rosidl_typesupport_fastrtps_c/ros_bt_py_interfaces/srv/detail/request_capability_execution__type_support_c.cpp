// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ros_bt_py_interfaces:srv/RequestCapabilityExecution.idl
// generated code does not contain a copyright notice
#include "ros_bt_py_interfaces/srv/detail/request_capability_execution__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ros_bt_py_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ros_bt_py_interfaces/srv/detail/request_capability_execution__struct.h"
#include "ros_bt_py_interfaces/srv/detail/request_capability_execution__functions.h"
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

#include "ros_bt_py_interfaces/msg/detail/capability_interface__functions.h"  // capability
#include "rosidl_runtime_c/string.h"  // implementation_tags_dict, node_id
#include "rosidl_runtime_c/string_functions.h"  // implementation_tags_dict, node_id

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


using _RequestCapabilityExecution_Request__ros_msg_type = ros_bt_py_interfaces__srv__RequestCapabilityExecution_Request;

static bool _RequestCapabilityExecution_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _RequestCapabilityExecution_Request__ros_msg_type * ros_message = static_cast<const _RequestCapabilityExecution_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: capability
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, CapabilityInterface
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->capability, cdr))
    {
      return false;
    }
  }

  // Field name: node_id
  {
    const rosidl_runtime_c__String * str = &ros_message->node_id;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: require_local_execution
  {
    cdr << (ros_message->require_local_execution ? true : false);
  }

  // Field name: implementation_tags_dict
  {
    const rosidl_runtime_c__String * str = &ros_message->implementation_tags_dict;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _RequestCapabilityExecution_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _RequestCapabilityExecution_Request__ros_msg_type * ros_message = static_cast<_RequestCapabilityExecution_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: capability
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, CapabilityInterface
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->capability))
    {
      return false;
    }
  }

  // Field name: node_id
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->node_id.data) {
      rosidl_runtime_c__String__init(&ros_message->node_id);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->node_id,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'node_id'\n");
      return false;
    }
  }

  // Field name: require_local_execution
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->require_local_execution = tmp ? true : false;
  }

  // Field name: implementation_tags_dict
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->implementation_tags_dict.data) {
      rosidl_runtime_c__String__init(&ros_message->implementation_tags_dict);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->implementation_tags_dict,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'implementation_tags_dict'\n");
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t get_serialized_size_ros_bt_py_interfaces__srv__RequestCapabilityExecution_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _RequestCapabilityExecution_Request__ros_msg_type * ros_message = static_cast<const _RequestCapabilityExecution_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name capability

  current_alignment += get_serialized_size_ros_bt_py_interfaces__msg__CapabilityInterface(
    &(ros_message->capability), current_alignment);
  // field.name node_id
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->node_id.size + 1);
  // field.name require_local_execution
  {
    size_t item_size = sizeof(ros_message->require_local_execution);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name implementation_tags_dict
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->implementation_tags_dict.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _RequestCapabilityExecution_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ros_bt_py_interfaces__srv__RequestCapabilityExecution_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t max_serialized_size_ros_bt_py_interfaces__srv__RequestCapabilityExecution_Request(
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

  // member: capability
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
  // member: node_id
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: require_local_execution
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: implementation_tags_dict
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ros_bt_py_interfaces__srv__RequestCapabilityExecution_Request;
    is_plain =
      (
      offsetof(DataType, implementation_tags_dict) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _RequestCapabilityExecution_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ros_bt_py_interfaces__srv__RequestCapabilityExecution_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_RequestCapabilityExecution_Request = {
  "ros_bt_py_interfaces::srv",
  "RequestCapabilityExecution_Request",
  _RequestCapabilityExecution_Request__cdr_serialize,
  _RequestCapabilityExecution_Request__cdr_deserialize,
  _RequestCapabilityExecution_Request__get_serialized_size,
  _RequestCapabilityExecution_Request__max_serialized_size
};

static rosidl_message_type_support_t _RequestCapabilityExecution_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_RequestCapabilityExecution_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, RequestCapabilityExecution_Request)() {
  return &_RequestCapabilityExecution_Request__type_support;
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
// #include "ros_bt_py_interfaces/srv/detail/request_capability_execution__struct.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/request_capability_execution__functions.h"
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

// already included above
// #include "rosidl_runtime_c/string.h"  // error_message, implementation_name, remote_mission_controller_topic
// already included above
// #include "rosidl_runtime_c/string_functions.h"  // error_message, implementation_name, remote_mission_controller_topic

// forward declare type support functions


using _RequestCapabilityExecution_Response__ros_msg_type = ros_bt_py_interfaces__srv__RequestCapabilityExecution_Response;

static bool _RequestCapabilityExecution_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _RequestCapabilityExecution_Response__ros_msg_type * ros_message = static_cast<const _RequestCapabilityExecution_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    cdr << (ros_message->success ? true : false);
  }

  // Field name: error_message
  {
    const rosidl_runtime_c__String * str = &ros_message->error_message;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: execute_local
  {
    cdr << (ros_message->execute_local ? true : false);
  }

  // Field name: implementation_name
  {
    const rosidl_runtime_c__String * str = &ros_message->implementation_name;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: remote_mission_controller_topic
  {
    const rosidl_runtime_c__String * str = &ros_message->remote_mission_controller_topic;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _RequestCapabilityExecution_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _RequestCapabilityExecution_Response__ros_msg_type * ros_message = static_cast<_RequestCapabilityExecution_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->success = tmp ? true : false;
  }

  // Field name: error_message
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->error_message.data) {
      rosidl_runtime_c__String__init(&ros_message->error_message);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->error_message,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'error_message'\n");
      return false;
    }
  }

  // Field name: execute_local
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->execute_local = tmp ? true : false;
  }

  // Field name: implementation_name
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->implementation_name.data) {
      rosidl_runtime_c__String__init(&ros_message->implementation_name);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->implementation_name,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'implementation_name'\n");
      return false;
    }
  }

  // Field name: remote_mission_controller_topic
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->remote_mission_controller_topic.data) {
      rosidl_runtime_c__String__init(&ros_message->remote_mission_controller_topic);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->remote_mission_controller_topic,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'remote_mission_controller_topic'\n");
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t get_serialized_size_ros_bt_py_interfaces__srv__RequestCapabilityExecution_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _RequestCapabilityExecution_Response__ros_msg_type * ros_message = static_cast<const _RequestCapabilityExecution_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name success
  {
    size_t item_size = sizeof(ros_message->success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name error_message
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->error_message.size + 1);
  // field.name execute_local
  {
    size_t item_size = sizeof(ros_message->execute_local);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name implementation_name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->implementation_name.size + 1);
  // field.name remote_mission_controller_topic
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->remote_mission_controller_topic.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _RequestCapabilityExecution_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ros_bt_py_interfaces__srv__RequestCapabilityExecution_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t max_serialized_size_ros_bt_py_interfaces__srv__RequestCapabilityExecution_Response(
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

  // member: success
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: error_message
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: execute_local
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: implementation_name
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: remote_mission_controller_topic
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ros_bt_py_interfaces__srv__RequestCapabilityExecution_Response;
    is_plain =
      (
      offsetof(DataType, remote_mission_controller_topic) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _RequestCapabilityExecution_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ros_bt_py_interfaces__srv__RequestCapabilityExecution_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_RequestCapabilityExecution_Response = {
  "ros_bt_py_interfaces::srv",
  "RequestCapabilityExecution_Response",
  _RequestCapabilityExecution_Response__cdr_serialize,
  _RequestCapabilityExecution_Response__cdr_deserialize,
  _RequestCapabilityExecution_Response__get_serialized_size,
  _RequestCapabilityExecution_Response__max_serialized_size
};

static rosidl_message_type_support_t _RequestCapabilityExecution_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_RequestCapabilityExecution_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, RequestCapabilityExecution_Response)() {
  return &_RequestCapabilityExecution_Response__type_support;
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
#include "ros_bt_py_interfaces/srv/request_capability_execution.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t RequestCapabilityExecution__callbacks = {
  "ros_bt_py_interfaces::srv",
  "RequestCapabilityExecution",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, RequestCapabilityExecution_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, RequestCapabilityExecution_Response)(),
};

static rosidl_service_type_support_t RequestCapabilityExecution__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &RequestCapabilityExecution__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, RequestCapabilityExecution)() {
  return &RequestCapabilityExecution__handle;
}

#if defined(__cplusplus)
}
#endif