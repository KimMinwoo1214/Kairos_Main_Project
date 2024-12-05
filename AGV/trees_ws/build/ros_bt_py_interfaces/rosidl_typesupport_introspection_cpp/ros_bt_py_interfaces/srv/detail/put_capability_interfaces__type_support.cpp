// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from ros_bt_py_interfaces:srv/PutCapabilityInterfaces.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "ros_bt_py_interfaces/srv/detail/put_capability_interfaces__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace ros_bt_py_interfaces
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void PutCapabilityInterfaces_Request_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ros_bt_py_interfaces::srv::PutCapabilityInterfaces_Request(_init);
}

void PutCapabilityInterfaces_Request_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ros_bt_py_interfaces::srv::PutCapabilityInterfaces_Request *>(message_memory);
  typed_message->~PutCapabilityInterfaces_Request();
}

size_t size_function__PutCapabilityInterfaces_Request__capabilities(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<ros_bt_py_interfaces::msg::CapabilityInterface> *>(untyped_member);
  return member->size();
}

const void * get_const_function__PutCapabilityInterfaces_Request__capabilities(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<ros_bt_py_interfaces::msg::CapabilityInterface> *>(untyped_member);
  return &member[index];
}

void * get_function__PutCapabilityInterfaces_Request__capabilities(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<ros_bt_py_interfaces::msg::CapabilityInterface> *>(untyped_member);
  return &member[index];
}

void fetch_function__PutCapabilityInterfaces_Request__capabilities(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const ros_bt_py_interfaces::msg::CapabilityInterface *>(
    get_const_function__PutCapabilityInterfaces_Request__capabilities(untyped_member, index));
  auto & value = *reinterpret_cast<ros_bt_py_interfaces::msg::CapabilityInterface *>(untyped_value);
  value = item;
}

void assign_function__PutCapabilityInterfaces_Request__capabilities(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<ros_bt_py_interfaces::msg::CapabilityInterface *>(
    get_function__PutCapabilityInterfaces_Request__capabilities(untyped_member, index));
  const auto & value = *reinterpret_cast<const ros_bt_py_interfaces::msg::CapabilityInterface *>(untyped_value);
  item = value;
}

void resize_function__PutCapabilityInterfaces_Request__capabilities(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<ros_bt_py_interfaces::msg::CapabilityInterface> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember PutCapabilityInterfaces_Request_message_member_array[1] = {
  {
    "capabilities",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ros_bt_py_interfaces::msg::CapabilityInterface>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros_bt_py_interfaces::srv::PutCapabilityInterfaces_Request, capabilities),  // bytes offset in struct
    nullptr,  // default value
    size_function__PutCapabilityInterfaces_Request__capabilities,  // size() function pointer
    get_const_function__PutCapabilityInterfaces_Request__capabilities,  // get_const(index) function pointer
    get_function__PutCapabilityInterfaces_Request__capabilities,  // get(index) function pointer
    fetch_function__PutCapabilityInterfaces_Request__capabilities,  // fetch(index, &value) function pointer
    assign_function__PutCapabilityInterfaces_Request__capabilities,  // assign(index, value) function pointer
    resize_function__PutCapabilityInterfaces_Request__capabilities  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers PutCapabilityInterfaces_Request_message_members = {
  "ros_bt_py_interfaces::srv",  // message namespace
  "PutCapabilityInterfaces_Request",  // message name
  1,  // number of fields
  sizeof(ros_bt_py_interfaces::srv::PutCapabilityInterfaces_Request),
  PutCapabilityInterfaces_Request_message_member_array,  // message members
  PutCapabilityInterfaces_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  PutCapabilityInterfaces_Request_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t PutCapabilityInterfaces_Request_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &PutCapabilityInterfaces_Request_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace ros_bt_py_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ros_bt_py_interfaces::srv::PutCapabilityInterfaces_Request>()
{
  return &::ros_bt_py_interfaces::srv::rosidl_typesupport_introspection_cpp::PutCapabilityInterfaces_Request_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, srv, PutCapabilityInterfaces_Request)() {
  return &::ros_bt_py_interfaces::srv::rosidl_typesupport_introspection_cpp::PutCapabilityInterfaces_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "array"
// already included above
// #include "cstddef"
// already included above
// #include "string"
// already included above
// #include "vector"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/put_capability_interfaces__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/field_types.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace ros_bt_py_interfaces
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void PutCapabilityInterfaces_Response_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ros_bt_py_interfaces::srv::PutCapabilityInterfaces_Response(_init);
}

void PutCapabilityInterfaces_Response_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ros_bt_py_interfaces::srv::PutCapabilityInterfaces_Response *>(message_memory);
  typed_message->~PutCapabilityInterfaces_Response();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember PutCapabilityInterfaces_Response_message_member_array[2] = {
  {
    "success",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros_bt_py_interfaces::srv::PutCapabilityInterfaces_Response, success),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "error_message",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros_bt_py_interfaces::srv::PutCapabilityInterfaces_Response, error_message),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers PutCapabilityInterfaces_Response_message_members = {
  "ros_bt_py_interfaces::srv",  // message namespace
  "PutCapabilityInterfaces_Response",  // message name
  2,  // number of fields
  sizeof(ros_bt_py_interfaces::srv::PutCapabilityInterfaces_Response),
  PutCapabilityInterfaces_Response_message_member_array,  // message members
  PutCapabilityInterfaces_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  PutCapabilityInterfaces_Response_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t PutCapabilityInterfaces_Response_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &PutCapabilityInterfaces_Response_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace ros_bt_py_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ros_bt_py_interfaces::srv::PutCapabilityInterfaces_Response>()
{
  return &::ros_bt_py_interfaces::srv::rosidl_typesupport_introspection_cpp::PutCapabilityInterfaces_Response_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, srv, PutCapabilityInterfaces_Response)() {
  return &::ros_bt_py_interfaces::srv::rosidl_typesupport_introspection_cpp::PutCapabilityInterfaces_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/put_capability_interfaces__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/service_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/service_type_support_decl.hpp"

namespace ros_bt_py_interfaces
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

// this is intentionally not const to allow initialization later to prevent an initialization race
static ::rosidl_typesupport_introspection_cpp::ServiceMembers PutCapabilityInterfaces_service_members = {
  "ros_bt_py_interfaces::srv",  // service namespace
  "PutCapabilityInterfaces",  // service name
  // these two fields are initialized below on the first access
  // see get_service_type_support_handle<ros_bt_py_interfaces::srv::PutCapabilityInterfaces>()
  nullptr,  // request message
  nullptr  // response message
};

static const rosidl_service_type_support_t PutCapabilityInterfaces_service_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &PutCapabilityInterfaces_service_members,
  get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace ros_bt_py_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<ros_bt_py_interfaces::srv::PutCapabilityInterfaces>()
{
  // get a handle to the value to be returned
  auto service_type_support =
    &::ros_bt_py_interfaces::srv::rosidl_typesupport_introspection_cpp::PutCapabilityInterfaces_service_type_support_handle;
  // get a non-const and properly typed version of the data void *
  auto service_members = const_cast<::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
    static_cast<const ::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
      service_type_support->data));
  // make sure that both the request_members_ and the response_members_ are initialized
  // if they are not, initialize them
  if (
    service_members->request_members_ == nullptr ||
    service_members->response_members_ == nullptr)
  {
    // initialize the request_members_ with the static function from the external library
    service_members->request_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::ros_bt_py_interfaces::srv::PutCapabilityInterfaces_Request
      >()->data
      );
    // initialize the response_members_ with the static function from the external library
    service_members->response_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::ros_bt_py_interfaces::srv::PutCapabilityInterfaces_Response
      >()->data
      );
  }
  // finally return the properly initialized service_type_support handle
  return service_type_support;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, srv, PutCapabilityInterfaces)() {
  return ::rosidl_typesupport_introspection_cpp::get_service_type_support_handle<ros_bt_py_interfaces::srv::PutCapabilityInterfaces>();
}

#ifdef __cplusplus
}
#endif