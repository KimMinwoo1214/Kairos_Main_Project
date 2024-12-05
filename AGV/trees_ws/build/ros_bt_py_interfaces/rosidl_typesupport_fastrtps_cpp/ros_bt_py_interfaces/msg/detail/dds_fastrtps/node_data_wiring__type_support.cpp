// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from ros_bt_py_interfaces:msg/NodeDataWiring.idl
// generated code does not contain a copyright notice
#include "ros_bt_py_interfaces/msg/detail/node_data_wiring__rosidl_typesupport_fastrtps_cpp.hpp"
#include "ros_bt_py_interfaces/msg/detail/node_data_wiring__struct.hpp"

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
bool cdr_serialize(
  const ros_bt_py_interfaces::msg::NodeDataLocation &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ros_bt_py_interfaces::msg::NodeDataLocation &);
size_t get_serialized_size(
  const ros_bt_py_interfaces::msg::NodeDataLocation &,
  size_t current_alignment);
size_t
max_serialized_size_NodeDataLocation(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace ros_bt_py_interfaces

// functions for ros_bt_py_interfaces::msg::NodeDataLocation already declared above


namespace ros_bt_py_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
cdr_serialize(
  const ros_bt_py_interfaces::msg::NodeDataWiring & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: source
  ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.source,
    cdr);
  // Member: target
  ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.target,
    cdr);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ros_bt_py_interfaces::msg::NodeDataWiring & ros_message)
{
  // Member: source
  ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.source);

  // Member: target
  ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.target);

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
get_serialized_size(
  const ros_bt_py_interfaces::msg::NodeDataWiring & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: source

  current_alignment +=
    ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.source, current_alignment);
  // Member: target

  current_alignment +=
    ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.target, current_alignment);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
max_serialized_size_NodeDataWiring(
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


  // Member: source
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size =
        ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::max_serialized_size_NodeDataLocation(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  // Member: target
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size =
        ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::max_serialized_size_NodeDataLocation(
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
    using DataType = ros_bt_py_interfaces::msg::NodeDataWiring;
    is_plain =
      (
      offsetof(DataType, target) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _NodeDataWiring__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ros_bt_py_interfaces::msg::NodeDataWiring *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _NodeDataWiring__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ros_bt_py_interfaces::msg::NodeDataWiring *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _NodeDataWiring__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ros_bt_py_interfaces::msg::NodeDataWiring *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _NodeDataWiring__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_NodeDataWiring(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _NodeDataWiring__callbacks = {
  "ros_bt_py_interfaces::msg",
  "NodeDataWiring",
  _NodeDataWiring__cdr_serialize,
  _NodeDataWiring__cdr_deserialize,
  _NodeDataWiring__get_serialized_size,
  _NodeDataWiring__max_serialized_size
};

static rosidl_message_type_support_t _NodeDataWiring__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_NodeDataWiring__callbacks,
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
get_message_type_support_handle<ros_bt_py_interfaces::msg::NodeDataWiring>()
{
  return &ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::_NodeDataWiring__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, msg, NodeDataWiring)() {
  return &ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::_NodeDataWiring__handle;
}

#ifdef __cplusplus
}
#endif
