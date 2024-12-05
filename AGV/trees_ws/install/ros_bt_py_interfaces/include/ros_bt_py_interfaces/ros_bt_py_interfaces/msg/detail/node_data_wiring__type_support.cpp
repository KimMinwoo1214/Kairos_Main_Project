// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from ros_bt_py_interfaces:msg/NodeDataWiring.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "ros_bt_py_interfaces/msg/detail/node_data_wiring__struct.hpp"
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

void NodeDataWiring_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ros_bt_py_interfaces::msg::NodeDataWiring(_init);
}

void NodeDataWiring_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ros_bt_py_interfaces::msg::NodeDataWiring *>(message_memory);
  typed_message->~NodeDataWiring();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember NodeDataWiring_message_member_array[2] = {
  {
    "source",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ros_bt_py_interfaces::msg::NodeDataLocation>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros_bt_py_interfaces::msg::NodeDataWiring, source),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "target",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ros_bt_py_interfaces::msg::NodeDataLocation>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros_bt_py_interfaces::msg::NodeDataWiring, target),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers NodeDataWiring_message_members = {
  "ros_bt_py_interfaces::msg",  // message namespace
  "NodeDataWiring",  // message name
  2,  // number of fields
  sizeof(ros_bt_py_interfaces::msg::NodeDataWiring),
  NodeDataWiring_message_member_array,  // message members
  NodeDataWiring_init_function,  // function to initialize message memory (memory has to be allocated)
  NodeDataWiring_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t NodeDataWiring_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &NodeDataWiring_message_members,
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
get_message_type_support_handle<ros_bt_py_interfaces::msg::NodeDataWiring>()
{
  return &::ros_bt_py_interfaces::msg::rosidl_typesupport_introspection_cpp::NodeDataWiring_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, msg, NodeDataWiring)() {
  return &::ros_bt_py_interfaces::msg::rosidl_typesupport_introspection_cpp::NodeDataWiring_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
