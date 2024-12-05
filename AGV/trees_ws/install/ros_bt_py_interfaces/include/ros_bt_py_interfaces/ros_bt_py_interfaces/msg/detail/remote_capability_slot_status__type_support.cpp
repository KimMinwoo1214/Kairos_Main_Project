// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from ros_bt_py_interfaces:msg/RemoteCapabilitySlotStatus.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "ros_bt_py_interfaces/msg/detail/remote_capability_slot_status__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace ros_bt_py_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void RemoteCapabilitySlotStatus_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ros_bt_py_interfaces::msg::RemoteCapabilitySlotStatus(_init);
}

void RemoteCapabilitySlotStatus_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ros_bt_py_interfaces::msg::RemoteCapabilitySlotStatus *>(message_memory);
  typed_message->~RemoteCapabilitySlotStatus();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember RemoteCapabilitySlotStatus_message_member_array[3] = {
  {
    "name",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros_bt_py_interfaces::msg::RemoteCapabilitySlotStatus, name),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "status",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros_bt_py_interfaces::msg::RemoteCapabilitySlotStatus, status),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "timestamp",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<builtin_interfaces::msg::Time>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros_bt_py_interfaces::msg::RemoteCapabilitySlotStatus, timestamp),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers RemoteCapabilitySlotStatus_message_members = {
  "ros_bt_py_interfaces::msg",  // message namespace
  "RemoteCapabilitySlotStatus",  // message name
  3,  // number of fields
  sizeof(ros_bt_py_interfaces::msg::RemoteCapabilitySlotStatus),
  RemoteCapabilitySlotStatus_message_member_array,  // message members
  RemoteCapabilitySlotStatus_init_function,  // function to initialize message memory (memory has to be allocated)
  RemoteCapabilitySlotStatus_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t RemoteCapabilitySlotStatus_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &RemoteCapabilitySlotStatus_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace ros_bt_py_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ros_bt_py_interfaces::msg::RemoteCapabilitySlotStatus>()
{
  return &::ros_bt_py_interfaces::msg::rosidl_typesupport_introspection_cpp::RemoteCapabilitySlotStatus_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, msg, RemoteCapabilitySlotStatus)() {
  return &::ros_bt_py_interfaces::msg::rosidl_typesupport_introspection_cpp::RemoteCapabilitySlotStatus_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif