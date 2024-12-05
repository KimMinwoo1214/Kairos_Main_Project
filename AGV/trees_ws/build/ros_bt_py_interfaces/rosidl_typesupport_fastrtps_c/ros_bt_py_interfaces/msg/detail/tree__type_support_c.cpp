// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ros_bt_py_interfaces:msg/Tree.idl
// generated code does not contain a copyright notice
#include "ros_bt_py_interfaces/msg/detail/tree__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ros_bt_py_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ros_bt_py_interfaces/msg/detail/tree__struct.h"
#include "ros_bt_py_interfaces/msg/detail/tree__functions.h"
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

#include "ros_bt_py_interfaces/msg/detail/node__functions.h"  // nodes
#include "ros_bt_py_interfaces/msg/detail/node_data_location__functions.h"  // public_node_data
#include "ros_bt_py_interfaces/msg/detail/node_data_wiring__functions.h"  // data_wirings
#include "rosidl_runtime_c/string.h"  // name, path, root_name, state
#include "rosidl_runtime_c/string_functions.h"  // name, path, root_name, state

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
size_t get_serialized_size_ros_bt_py_interfaces__msg__NodeDataLocation(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ros_bt_py_interfaces__msg__NodeDataLocation(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, NodeDataLocation)();
size_t get_serialized_size_ros_bt_py_interfaces__msg__NodeDataWiring(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ros_bt_py_interfaces__msg__NodeDataWiring(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, NodeDataWiring)();


using _Tree__ros_msg_type = ros_bt_py_interfaces__msg__Tree;

static bool _Tree__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Tree__ros_msg_type * ros_message = static_cast<const _Tree__ros_msg_type *>(untyped_ros_message);
  // Field name: name
  {
    const rosidl_runtime_c__String * str = &ros_message->name;
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

  // Field name: path
  {
    const rosidl_runtime_c__String * str = &ros_message->path;
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

  // Field name: root_name
  {
    const rosidl_runtime_c__String * str = &ros_message->root_name;
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

  // Field name: nodes
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, Node
      )()->data);
    size_t size = ros_message->nodes.size;
    auto array_ptr = ros_message->nodes.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_serialize(
          &array_ptr[i], cdr))
      {
        return false;
      }
    }
  }

  // Field name: data_wirings
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, NodeDataWiring
      )()->data);
    size_t size = ros_message->data_wirings.size;
    auto array_ptr = ros_message->data_wirings.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_serialize(
          &array_ptr[i], cdr))
      {
        return false;
      }
    }
  }

  // Field name: tick_frequency_hz
  {
    cdr << ros_message->tick_frequency_hz;
  }

  // Field name: state
  {
    const rosidl_runtime_c__String * str = &ros_message->state;
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

  // Field name: public_node_data
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, NodeDataLocation
      )()->data);
    size_t size = ros_message->public_node_data.size;
    auto array_ptr = ros_message->public_node_data.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_serialize(
          &array_ptr[i], cdr))
      {
        return false;
      }
    }
  }

  return true;
}

static bool _Tree__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Tree__ros_msg_type * ros_message = static_cast<_Tree__ros_msg_type *>(untyped_ros_message);
  // Field name: name
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->name.data) {
      rosidl_runtime_c__String__init(&ros_message->name);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->name,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'name'\n");
      return false;
    }
  }

  // Field name: path
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->path.data) {
      rosidl_runtime_c__String__init(&ros_message->path);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->path,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'path'\n");
      return false;
    }
  }

  // Field name: root_name
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->root_name.data) {
      rosidl_runtime_c__String__init(&ros_message->root_name);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->root_name,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'root_name'\n");
      return false;
    }
  }

  // Field name: nodes
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, Node
      )()->data);
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->nodes.data) {
      ros_bt_py_interfaces__msg__Node__Sequence__fini(&ros_message->nodes);
    }
    if (!ros_bt_py_interfaces__msg__Node__Sequence__init(&ros_message->nodes, size)) {
      fprintf(stderr, "failed to create array for field 'nodes'");
      return false;
    }
    auto array_ptr = ros_message->nodes.data;
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_deserialize(
          cdr, &array_ptr[i]))
      {
        return false;
      }
    }
  }

  // Field name: data_wirings
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, NodeDataWiring
      )()->data);
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->data_wirings.data) {
      ros_bt_py_interfaces__msg__NodeDataWiring__Sequence__fini(&ros_message->data_wirings);
    }
    if (!ros_bt_py_interfaces__msg__NodeDataWiring__Sequence__init(&ros_message->data_wirings, size)) {
      fprintf(stderr, "failed to create array for field 'data_wirings'");
      return false;
    }
    auto array_ptr = ros_message->data_wirings.data;
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_deserialize(
          cdr, &array_ptr[i]))
      {
        return false;
      }
    }
  }

  // Field name: tick_frequency_hz
  {
    cdr >> ros_message->tick_frequency_hz;
  }

  // Field name: state
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->state.data) {
      rosidl_runtime_c__String__init(&ros_message->state);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->state,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'state'\n");
      return false;
    }
  }

  // Field name: public_node_data
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, NodeDataLocation
      )()->data);
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->public_node_data.data) {
      ros_bt_py_interfaces__msg__NodeDataLocation__Sequence__fini(&ros_message->public_node_data);
    }
    if (!ros_bt_py_interfaces__msg__NodeDataLocation__Sequence__init(&ros_message->public_node_data, size)) {
      fprintf(stderr, "failed to create array for field 'public_node_data'");
      return false;
    }
    auto array_ptr = ros_message->public_node_data.data;
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_deserialize(
          cdr, &array_ptr[i]))
      {
        return false;
      }
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t get_serialized_size_ros_bt_py_interfaces__msg__Tree(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Tree__ros_msg_type * ros_message = static_cast<const _Tree__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->name.size + 1);
  // field.name path
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->path.size + 1);
  // field.name root_name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->root_name.size + 1);
  // field.name nodes
  {
    size_t array_size = ros_message->nodes.size;
    auto array_ptr = ros_message->nodes.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += get_serialized_size_ros_bt_py_interfaces__msg__Node(
        &array_ptr[index], current_alignment);
    }
  }
  // field.name data_wirings
  {
    size_t array_size = ros_message->data_wirings.size;
    auto array_ptr = ros_message->data_wirings.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += get_serialized_size_ros_bt_py_interfaces__msg__NodeDataWiring(
        &array_ptr[index], current_alignment);
    }
  }
  // field.name tick_frequency_hz
  {
    size_t item_size = sizeof(ros_message->tick_frequency_hz);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name state
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->state.size + 1);
  // field.name public_node_data
  {
    size_t array_size = ros_message->public_node_data.size;
    auto array_ptr = ros_message->public_node_data.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += get_serialized_size_ros_bt_py_interfaces__msg__NodeDataLocation(
        &array_ptr[index], current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Tree__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ros_bt_py_interfaces__msg__Tree(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ros_bt_py_interfaces
size_t max_serialized_size_ros_bt_py_interfaces__msg__Tree(
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

  // member: name
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
  // member: path
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
  // member: root_name
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
  // member: nodes
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
  // member: data_wirings
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
        max_serialized_size_ros_bt_py_interfaces__msg__NodeDataWiring(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }
  // member: tick_frequency_hz
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: state
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
  // member: public_node_data
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
        max_serialized_size_ros_bt_py_interfaces__msg__NodeDataLocation(
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
    using DataType = ros_bt_py_interfaces__msg__Tree;
    is_plain =
      (
      offsetof(DataType, public_node_data) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _Tree__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ros_bt_py_interfaces__msg__Tree(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_Tree = {
  "ros_bt_py_interfaces::msg",
  "Tree",
  _Tree__cdr_serialize,
  _Tree__cdr_deserialize,
  _Tree__get_serialized_size,
  _Tree__max_serialized_size
};

static rosidl_message_type_support_t _Tree__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Tree,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ros_bt_py_interfaces, msg, Tree)() {
  return &_Tree__type_support;
}

#if defined(__cplusplus)
}
#endif
