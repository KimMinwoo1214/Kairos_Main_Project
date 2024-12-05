// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ros_bt_py_interfaces:srv/SaveTree.idl
// generated code does not contain a copyright notice
#include "ros_bt_py_interfaces/srv/detail/save_tree__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ros_bt_py_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ros_bt_py_interfaces/srv/detail/save_tree__struct.h"
#include "ros_bt_py_interfaces/srv/detail/save_tree__functions.h"
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

#include "ros_bt_py_interfaces/msg/detail/tree__functions.h"  // tree
#include "rosidl_runtime_c/string.h"  // filepath, storage_path
#include "rosidl_runtime_c/string_functions.h"  // filepath, storage_path

// forward declare type support functions
size_t get_serialized_size_ros_bt_py_interfaces__msg__Tree(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ros_bt_py_interfaces__msg__Tree(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, Tree)();


using _SaveTree_Request__ros_msg_type = ros_bt_py_interfaces__srv__SaveTree_Request;

static bool _SaveTree_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _SaveTree_Request__ros_msg_type * ros_message = static_cast<const _SaveTree_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: storage_path
  {
    const rosidl_runtime_c__String * str = &ros_message->storage_path;
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

  // Field name: filepath
  {
    const rosidl_runtime_c__String * str = &ros_message->filepath;
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

  // Field name: tree
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, Tree
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->tree, cdr))
    {
      return false;
    }
  }

  // Field name: allow_overwrite
  {
    cdr << (ros_message->allow_overwrite ? true : false);
  }

  // Field name: allow_rename
  {
    cdr << (ros_message->allow_rename ? true : false);
  }

  return true;
}

static bool _SaveTree_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _SaveTree_Request__ros_msg_type * ros_message = static_cast<_SaveTree_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: storage_path
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->storage_path.data) {
      rosidl_runtime_c__String__init(&ros_message->storage_path);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->storage_path,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'storage_path'\n");
      return false;
    }
  }

  // Field name: filepath
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->filepath.data) {
      rosidl_runtime_c__String__init(&ros_message->filepath);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->filepath,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'filepath'\n");
      return false;
    }
  }

  // Field name: tree
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, Tree
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->tree))
    {
      return false;
    }
  }

  // Field name: allow_overwrite
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->allow_overwrite = tmp ? true : false;
  }

  // Field name: allow_rename
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->allow_rename = tmp ? true : false;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t get_serialized_size_ros_bt_py_interfaces__srv__SaveTree_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _SaveTree_Request__ros_msg_type * ros_message = static_cast<const _SaveTree_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name storage_path
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->storage_path.size + 1);
  // field.name filepath
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->filepath.size + 1);
  // field.name tree

  current_alignment += get_serialized_size_ros_bt_py_interfaces__msg__Tree(
    &(ros_message->tree), current_alignment);
  // field.name allow_overwrite
  {
    size_t item_size = sizeof(ros_message->allow_overwrite);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name allow_rename
  {
    size_t item_size = sizeof(ros_message->allow_rename);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _SaveTree_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ros_bt_py_interfaces__srv__SaveTree_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t max_serialized_size_ros_bt_py_interfaces__srv__SaveTree_Request(
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

  // member: storage_path
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
  // member: filepath
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
  // member: tree
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_ros_bt_py_interfaces__msg__Tree(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }
  // member: allow_overwrite
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: allow_rename
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
    using DataType = ros_bt_py_interfaces__srv__SaveTree_Request;
    is_plain =
      (
      offsetof(DataType, allow_rename) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _SaveTree_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ros_bt_py_interfaces__srv__SaveTree_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_SaveTree_Request = {
  "ros_bt_py_interfaces::srv",
  "SaveTree_Request",
  _SaveTree_Request__cdr_serialize,
  _SaveTree_Request__cdr_deserialize,
  _SaveTree_Request__get_serialized_size,
  _SaveTree_Request__max_serialized_size
};

static rosidl_message_type_support_t _SaveTree_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_SaveTree_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, SaveTree_Request)() {
  return &_SaveTree_Request__type_support;
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
// #include "ros_bt_py_interfaces/srv/detail/save_tree__struct.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/save_tree__functions.h"
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
// #include "rosidl_runtime_c/string.h"  // error_message, file_path
// already included above
// #include "rosidl_runtime_c/string_functions.h"  // error_message, file_path

// forward declare type support functions


using _SaveTree_Response__ros_msg_type = ros_bt_py_interfaces__srv__SaveTree_Response;

static bool _SaveTree_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _SaveTree_Response__ros_msg_type * ros_message = static_cast<const _SaveTree_Response__ros_msg_type *>(untyped_ros_message);
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

  // Field name: file_path
  {
    const rosidl_runtime_c__String * str = &ros_message->file_path;
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

static bool _SaveTree_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _SaveTree_Response__ros_msg_type * ros_message = static_cast<_SaveTree_Response__ros_msg_type *>(untyped_ros_message);
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

  // Field name: file_path
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->file_path.data) {
      rosidl_runtime_c__String__init(&ros_message->file_path);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->file_path,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'file_path'\n");
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t get_serialized_size_ros_bt_py_interfaces__srv__SaveTree_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _SaveTree_Response__ros_msg_type * ros_message = static_cast<const _SaveTree_Response__ros_msg_type *>(untyped_ros_message);
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
  // field.name file_path
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->file_path.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _SaveTree_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ros_bt_py_interfaces__srv__SaveTree_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t max_serialized_size_ros_bt_py_interfaces__srv__SaveTree_Response(
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
  // member: file_path
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
    using DataType = ros_bt_py_interfaces__srv__SaveTree_Response;
    is_plain =
      (
      offsetof(DataType, file_path) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _SaveTree_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ros_bt_py_interfaces__srv__SaveTree_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_SaveTree_Response = {
  "ros_bt_py_interfaces::srv",
  "SaveTree_Response",
  _SaveTree_Response__cdr_serialize,
  _SaveTree_Response__cdr_deserialize,
  _SaveTree_Response__get_serialized_size,
  _SaveTree_Response__max_serialized_size
};

static rosidl_message_type_support_t _SaveTree_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_SaveTree_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, SaveTree_Response)() {
  return &_SaveTree_Response__type_support;
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
#include "ros_bt_py_interfaces/srv/save_tree.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t SaveTree__callbacks = {
  "ros_bt_py_interfaces::srv",
  "SaveTree",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, SaveTree_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, SaveTree_Response)(),
};

static rosidl_service_type_support_t SaveTree__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &SaveTree__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, srv, SaveTree)() {
  return &SaveTree__handle;
}

#if defined(__cplusplus)
}
#endif
