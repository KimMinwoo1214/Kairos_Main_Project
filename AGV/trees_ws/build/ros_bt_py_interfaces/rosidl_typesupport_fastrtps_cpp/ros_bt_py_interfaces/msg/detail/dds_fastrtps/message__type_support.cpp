// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from ros_bt_py_interfaces:msg/Message.idl
// generated code does not contain a copyright notice
#include "ros_bt_py_interfaces/msg/detail/message__rosidl_typesupport_fastrtps_cpp.hpp"
#include "ros_bt_py_interfaces/msg/detail/message__struct.hpp"

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
  const ros_bt_py_interfaces::msg::Message & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: msg
  cdr << ros_message.msg;
  // Member: service
  cdr << (ros_message.service ? true : false);
  // Member: action
  cdr << (ros_message.action ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ros_bt_py_interfaces::msg::Message & ros_message)
{
  // Member: msg
  cdr >> ros_message.msg;

  // Member: service
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.service = tmp ? true : false;
  }

  // Member: action
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.action = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
get_serialized_size(
  const ros_bt_py_interfaces::msg::Message & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: msg
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.msg.size() + 1);
  // Member: service
  {
    size_t item_size = sizeof(ros_message.service);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: action
  {
    size_t item_size = sizeof(ros_message.action);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ros_bt_py_interfaces
max_serialized_size_Message(
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


  // Member: msg
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

  // Member: service
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: action
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
    using DataType = ros_bt_py_interfaces::msg::Message;
    is_plain =
      (
      offsetof(DataType, action) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _Message__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ros_bt_py_interfaces::msg::Message *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Message__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ros_bt_py_interfaces::msg::Message *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Message__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ros_bt_py_interfaces::msg::Message *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Message__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_Message(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _Message__callbacks = {
  "ros_bt_py_interfaces::msg",
  "Message",
  _Message__cdr_serialize,
  _Message__cdr_deserialize,
  _Message__get_serialized_size,
  _Message__max_serialized_size
};

static rosidl_message_type_support_t _Message__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Message__callbacks,
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
get_message_type_support_handle<ros_bt_py_interfaces::msg::Message>()
{
  return &ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::_Message__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, msg, Message)() {
  return &ros_bt_py_interfaces::msg::typesupport_fastrtps_cpp::_Message__handle;
}

#ifdef __cplusplus
}
#endif
