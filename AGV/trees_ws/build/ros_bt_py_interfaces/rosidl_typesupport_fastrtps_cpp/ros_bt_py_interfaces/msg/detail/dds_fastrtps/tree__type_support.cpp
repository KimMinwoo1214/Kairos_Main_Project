// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from ros_bt_py_interfaces:msg/Tree.idl
// generated code does not contain a copyright notice
#include "ros_bt_py_interfaces/msg/detail/tree__rosidl_typesupport_fastrtps_cpp.hpp"
#include "ros_bt_py_interfaces/msg/detail/tree__struct.hpp"

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
  const ros_bt_py_interfaces::msg::Node &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ros_bt_py_interfaces::msg::Node &);
size_t get_serialized_size(
  const ros_bt_py_interfaces::msg::Node &,
  size_t current_alignment);
size_t
max_serialized_size_Node(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace ros_bt_py_interfaces

namespace ros_bt_py_interfaces
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const ros_bt_py_interfaces::msg::NodeDataWiring &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ros_bt_py_interfaces::msg::NodeDataWiring &);
size_t get_serialized_size(
  const ros_bt_py_interfaces::msg::NodeDataWiring &,
  size_t current_alignment);
size_t
max_serialized_size_NodeDataWiring(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace ros_bt_py_interfaces

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


namespace ros_bt_py_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
cdr_serialize(
  const ros_bt_py_interfaces::msg::Tree & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: name
  cdr << ros_message.name;
  // Member: path
  cdr << ros_message.path;
  // Member: root_name
  cdr << ros_message.root_name;
  // Member: nodes
  {
    size_t size = ros_message.nodes.size();
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; i++) {
      ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::cdr_serialize(
        ros_message.nodes[i],
        cdr);
    }
  }
  // Member: data_wirings
  {
    size_t size = ros_message.data_wirings.size();
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; i++) {
      ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::cdr_serialize(
        ros_message.data_wirings[i],
        cdr);
    }
  }
  // Member: tick_frequency_hz
  cdr << ros_message.tick_frequency_hz;
  // Member: state
  cdr << ros_message.state;
  // Member: public_node_data
  {
    size_t size = ros_message.public_node_data.size();
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; i++) {
      ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::cdr_serialize(
        ros_message.public_node_data[i],
        cdr);
    }
  }
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ros_bt_py_interfaces::msg::Tree & ros_message)
{
  // Member: name
  cdr >> ros_message.name;

  // Member: path
  cdr >> ros_message.path;

  // Member: root_name
  cdr >> ros_message.root_name;

  // Member: nodes
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    ros_message.nodes.resize(size);
    for (size_t i = 0; i < size; i++) {
      ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::cdr_deserialize(
        cdr, ros_message.nodes[i]);
    }
  }

  // Member: data_wirings
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    ros_message.data_wirings.resize(size);
    for (size_t i = 0; i < size; i++) {
      ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::cdr_deserialize(
        cdr, ros_message.data_wirings[i]);
    }
  }

  // Member: tick_frequency_hz
  cdr >> ros_message.tick_frequency_hz;

  // Member: state
  cdr >> ros_message.state;

  // Member: public_node_data
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    ros_message.public_node_data.resize(size);
    for (size_t i = 0; i < size; i++) {
      ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::cdr_deserialize(
        cdr, ros_message.public_node_data[i]);
    }
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
get_serialized_size(
  const ros_bt_py_interfaces::msg::Tree & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.name.size() + 1);
  // Member: path
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.path.size() + 1);
  // Member: root_name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.root_name.size() + 1);
  // Member: nodes
  {
    size_t array_size = ros_message.nodes.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::get_serialized_size(
        ros_message.nodes[index], current_alignment);
    }
  }
  // Member: data_wirings
  {
    size_t array_size = ros_message.data_wirings.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::get_serialized_size(
        ros_message.data_wirings[index], current_alignment);
    }
  }
  // Member: tick_frequency_hz
  {
    size_t item_size = sizeof(ros_message.tick_frequency_hz);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: state
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.state.size() + 1);
  // Member: public_node_data
  {
    size_t array_size = ros_message.public_node_data.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::get_serialized_size(
        ros_message.public_node_data[index], current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
max_serialized_size_Tree(
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


  // Member: name
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

  // Member: path
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

  // Member: root_name
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

  // Member: nodes
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
      size_t inner_size =
        ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::max_serialized_size_Node(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  // Member: data_wirings
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
      size_t inner_size =
        ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::max_serialized_size_NodeDataWiring(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  // Member: tick_frequency_hz
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: state
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

  // Member: public_node_data
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
    using DataType = ros_bt_py_interfaces::msg::Tree;
    is_plain =
      (
      offsetof(DataType, public_node_data) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _Tree__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ros_bt_py_interfaces::msg::Tree *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Tree__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ros_bt_py_interfaces::msg::Tree *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Tree__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ros_bt_py_interfaces::msg::Tree *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Tree__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_Tree(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _Tree__callbacks = {
  "ros_bt_py_interfaces::msg",
  "Tree",
  _Tree__cdr_serialize,
  _Tree__cdr_deserialize,
  _Tree__get_serialized_size,
  _Tree__max_serialized_size
};

static rosidl_message_type_support_t _Tree__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Tree__callbacks,
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
get_message_type_support_handle<ros_bt_py_interfaces::msg::Tree>()
{
  return &ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::_Tree__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, msg, Tree)() {
  return &ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::_Tree__handle;
}

#ifdef __cplusplus
}
#endif
