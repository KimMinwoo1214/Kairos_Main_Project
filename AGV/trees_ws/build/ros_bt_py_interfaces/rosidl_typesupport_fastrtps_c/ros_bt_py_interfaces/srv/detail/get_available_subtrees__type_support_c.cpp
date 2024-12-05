// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ros_bt_py_interfaces:srv/GetAvailableSubtrees.idl
// generated code does not contain a copyright notice
#include "ros_bt_py_interfaces/srv/detail/get_available_subtrees__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ros_bt_py_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ros_bt_py_interfaces/srv/detail/get_available_subtrees__struct.h"
#include "ros_bt_py_interfaces/srv/detail/get_available_subtrees__functions.h"
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

#include "rosidl_runtime_c/string.h"  // subtree_paths
#include "rosidl_runtime_c/string_functions.h"  // subtree_paths

// forward declare type support functions


using _GetAvailableSubtrees_Request__ros_msg_type = ros_bt_py_interfaces__srv__GetAvailableSubtrees_Request;

static bool _GetAvailableSubtrees_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _GetAvailableSubtrees_Request__ros_msg_type * ros_message = static_cast<const _GetAvailableSubtrees_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: subtree_paths
  {
    size_t size = ros_message->subtree_paths.size;
    auto array_ptr = ros_message->subtree_paths.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      const rosidl_runtime_c__String * str = &array_ptr[i];
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
  }

  return true;
}

static bool _GetAvailableSubtrees_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _GetAvailableSubtrees_Request__ros_msg_type * ros_message = static_cast<_GetAvailableSubtrees_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: subtree_paths
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->subtree_paths.data) {
      rosidl_runtime_c__String__Sequence__fini(&ros_message->subtree_paths);
    }
    if (!rosidl_runtime_c__String__Sequence__init(&ros_message->subtree_paths, size)) {
      fprintf(stderr, "failed to create array for field 'subtree_paths'");
      return false;
    }
    auto array_ptr = ros_message->subtree_paths.data;
    for (size_t i = 0; i < size; ++i) {
      std::string tmp;
      cdr >> tmp;
      auto & ros_i = array_ptr[i];
      if (!ros_i.data) {
        rosidl_runtime_c__String__init(&ros_i);
      }
      bool succeeded = rosidl_runtime_c__String__assign(
        &ros_i,
        tmp.c_str());
      if (!succeeded) {
        fprintf(stderr, "failed to assign string into field 'subtree_paths'\n");
        return false;
      }
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t get_serialized_size_ros_bt_py_interfaces__srv__GetAvailableSubtrees_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _GetAvailableSubtrees_Request__ros_msg_type * ros_message = static_cast<const _GetAvailableSubtrees_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name subtree_paths
  {
    size_t array_size = ros_message->subtree_paths.size;
    auto array_ptr = ros_message->subtree_paths.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        (array_ptr[index].size + 1);
    }
  }

  return current_alignment - initial_alignment;
}

static uint32_t _GetAvailableSubtrees_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ros_bt_py_interfaces__srv__GetAvailableSubtrees_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t max_serialized_size_ros_bt_py_interfaces__srv__GetAvailableSubtrees_Request(
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

  // member: subtree_paths
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

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
    using DataType = ros_bt_py_interfaces__srv__GetAvailableSubtrees_Request;
    is_plain =
      (
      offsetof(DataType, subtree_paths) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _GetAvailableSubtrees_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ros_bt_py_interfaces__srv__GetAvailableSubtrees_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_GetAvailableSubtrees_Request = {
  "ros_bt_py_interfaces::srv",
  "GetAvailableSubtrees_Request",
  _GetAvailableSubtrees_Request__cdr_serialize,
  _GetAvailableSubtrees_Request__cdr_deserialize,
  _GetAvailableSubtrees_Request__get_serialized_size,
  _GetAvailableSubtrees_Request__max_serialized_size
};

static rosidl_message_type_support_t _GetAvailableSubtrees_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_GetAvailableSubtrees_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, GetAvailableSubtrees_Request)() {
  return &_GetAvailableSubtrees_Request__type_support;
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
// #include "ros_bt_py_interfaces/srv/detail/get_available_subtrees__struct.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/get_available_subtrees__functions.h"
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

#include "ros_bt_py_interfaces/msg/detail/node__functions.h"  // available_subtree_nodes
// already included above
// #include "rosidl_runtime_c/string.h"  // error_message
// already included above
// #include "rosidl_runtime_c/string_functions.h"  // error_message

// forward declare type support functions
size_t get_serialized_size_ros_bt_py_interfaces__msg__Node(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ros_bt_py_interfaces__msg__Node(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, Node)();


using _GetAvailableSubtrees_Response__ros_msg_type = ros_bt_py_interfaces__srv__GetAvailableSubtrees_Response;

static bool _GetAvailableSubtrees_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _GetAvailableSubtrees_Response__ros_msg_type * ros_message = static_cast<const _GetAvailableSubtrees_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: available_subtree_nodes
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, Node
      )()->data);
    size_t size = ros_message->available_subtree_nodes.size;
    auto array_ptr = ros_message->available_subtree_nodes.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_serialize(
          &array_ptr[i], cdr))
      {
        return false;
      }
    }
  }

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

  return true;
}

static bool _GetAvailableSubtrees_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _GetAvailableSubtrees_Response__ros_msg_type * ros_message = static_cast<_GetAvailableSubtrees_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: available_subtree_nodes
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, Node
      )()->data);
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->available_subtree_nodes.data) {
      ros_bt_py_interfaces__msg__Node__Sequence__fini(&ros_message->available_subtree_nodes);
    }
    if (!ros_bt_py_interfaces__msg__Node__Sequence__init(&ros_message->available_subtree_nodes, size)) {
      fprintf(stderr, "failed to create array for field 'available_subtree_nodes'");
      return false;
    }
    auto array_ptr = ros_message->available_subtree_nodes.data;
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_deserialize(
          cdr, &array_ptr[i]))
      {
        return false;
      }
    }
  }

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

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t get_serialized_size_ros_bt_py_interfaces__srv__GetAvailableSubtrees_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _GetAvailableSubtrees_Response__ros_msg_type * ros_message = static_cast<const _GetAvailableSubtrees_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name available_subtree_nodes
  {
    size_t array_size = ros_message->available_subtree_nodes.size;
    auto array_ptr = ros_message->available_subtree_nodes.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += get_serialized_size_ros_bt_py_interfaces__msg__Node(
        &array_ptr[index], current_alignment);
    }
  }
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

  return current_alignment - initial_alignment;
}

static uint32_t _GetAvailableSubtrees_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ros_bt_py_interfaces__srv__GetAvailableSubtrees_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t max_serialized_size_ros_bt_py_interfaces__srv__GetAvailableSubtrees_Response(
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

  // member: available_subtree_nodes
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_ros_bt_py_interfaces__msg__Node(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }
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

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ros_bt_py_interfaces__srv__GetAvailableSubtrees_Response;
    is_plain =
      (
      offsetof(DataType, error_message) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _GetAvailableSubtrees_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ros_bt_py_interfaces__srv__GetAvailableSubtrees_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_GetAvailableSubtrees_Response = {
  "ros_bt_py_interfaces::srv",
  "GetAvailableSubtrees_Response",
  _GetAvailableSubtrees_Response__cdr_serialize,
  _GetAvailableSubtrees_Response__cdr_deserialize,
  _GetAvailableSubtrees_Response__get_serialized_size,
  _GetAvailableSubtrees_Response__max_serialized_size
};

static rosidl_message_type_support_t _GetAvailableSubtrees_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_GetAvailableSubtrees_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, GetAvailableSubtrees_Response)() {
  return &_GetAvailableSubtrees_Response__type_support;
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
#include "ros_bt_py_interfaces/srv/get_available_subtrees.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t GetAvailableSubtrees__callbacks = {
  "ros_bt_py_interfaces::srv",
  "GetAvailableSubtrees",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, GetAvailableSubtrees_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, GetAvailableSubtrees_Response)(),
};

static rosidl_service_type_support_t GetAvailableSubtrees__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &GetAvailableSubtrees__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, GetAvailableSubtrees)() {
  return &GetAvailableSubtrees__handle;
}

#if defined(__cplusplus)
}
#endif
