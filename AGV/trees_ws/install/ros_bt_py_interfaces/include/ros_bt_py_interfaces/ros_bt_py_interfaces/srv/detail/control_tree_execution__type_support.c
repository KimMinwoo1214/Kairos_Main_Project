// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ros_bt_py_interfaces:srv/ControlTreeExecution.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ros_bt_py_interfaces/srv/detail/control_tree_execution__rosidl_typesupport_introspection_c.h"
#include "ros_bt_py_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ros_bt_py_interfaces/srv/detail/control_tree_execution__functions.h"
#include "ros_bt_py_interfaces/srv/detail/control_tree_execution__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void ros_bt_py_interfaces__srv__ControlTreeExecution_Request__rosidl_typesupport_introspection_c__ControlTreeExecution_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ros_bt_py_interfaces__srv__ControlTreeExecution_Request__init(message_memory);
}

void ros_bt_py_interfaces__srv__ControlTreeExecution_Request__rosidl_typesupport_introspection_c__ControlTreeExecution_Request_fini_function(void * message_memory)
{
  ros_bt_py_interfaces__srv__ControlTreeExecution_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember ros_bt_py_interfaces__srv__ControlTreeExecution_Request__rosidl_typesupport_introspection_c__ControlTreeExecution_Request_message_member_array[2] = {
  {
    "command",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros_bt_py_interfaces__srv__ControlTreeExecution_Request, command),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "tick_frequency_hz",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros_bt_py_interfaces__srv__ControlTreeExecution_Request, tick_frequency_hz),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ros_bt_py_interfaces__srv__ControlTreeExecution_Request__rosidl_typesupport_introspection_c__ControlTreeExecution_Request_message_members = {
  "ros_bt_py_interfaces__srv",  // message namespace
  "ControlTreeExecution_Request",  // message name
  2,  // number of fields
  sizeof(ros_bt_py_interfaces__srv__ControlTreeExecution_Request),
  ros_bt_py_interfaces__srv__ControlTreeExecution_Request__rosidl_typesupport_introspection_c__ControlTreeExecution_Request_message_member_array,  // message members
  ros_bt_py_interfaces__srv__ControlTreeExecution_Request__rosidl_typesupport_introspection_c__ControlTreeExecution_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  ros_bt_py_interfaces__srv__ControlTreeExecution_Request__rosidl_typesupport_introspection_c__ControlTreeExecution_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ros_bt_py_interfaces__srv__ControlTreeExecution_Request__rosidl_typesupport_introspection_c__ControlTreeExecution_Request_message_type_support_handle = {
  0,
  &ros_bt_py_interfaces__srv__ControlTreeExecution_Request__rosidl_typesupport_introspection_c__ControlTreeExecution_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ros_bt_py_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros_bt_py_interfaces, srv, ControlTreeExecution_Request)() {
  if (!ros_bt_py_interfaces__srv__ControlTreeExecution_Request__rosidl_typesupport_introspection_c__ControlTreeExecution_Request_message_type_support_handle.typesupport_identifier) {
    ros_bt_py_interfaces__srv__ControlTreeExecution_Request__rosidl_typesupport_introspection_c__ControlTreeExecution_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ros_bt_py_interfaces__srv__ControlTreeExecution_Request__rosidl_typesupport_introspection_c__ControlTreeExecution_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "ros_bt_py_interfaces/srv/detail/control_tree_execution__rosidl_typesupport_introspection_c.h"
// already included above
// #include "ros_bt_py_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/control_tree_execution__functions.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/control_tree_execution__struct.h"


// Include directives for member types
// Member `error_message`
// Member `tree_state`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ros_bt_py_interfaces__srv__ControlTreeExecution_Response__rosidl_typesupport_introspection_c__ControlTreeExecution_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ros_bt_py_interfaces__srv__ControlTreeExecution_Response__init(message_memory);
}

void ros_bt_py_interfaces__srv__ControlTreeExecution_Response__rosidl_typesupport_introspection_c__ControlTreeExecution_Response_fini_function(void * message_memory)
{
  ros_bt_py_interfaces__srv__ControlTreeExecution_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember ros_bt_py_interfaces__srv__ControlTreeExecution_Response__rosidl_typesupport_introspection_c__ControlTreeExecution_Response_message_member_array[3] = {
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros_bt_py_interfaces__srv__ControlTreeExecution_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "error_message",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros_bt_py_interfaces__srv__ControlTreeExecution_Response, error_message),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "tree_state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros_bt_py_interfaces__srv__ControlTreeExecution_Response, tree_state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ros_bt_py_interfaces__srv__ControlTreeExecution_Response__rosidl_typesupport_introspection_c__ControlTreeExecution_Response_message_members = {
  "ros_bt_py_interfaces__srv",  // message namespace
  "ControlTreeExecution_Response",  // message name
  3,  // number of fields
  sizeof(ros_bt_py_interfaces__srv__ControlTreeExecution_Response),
  ros_bt_py_interfaces__srv__ControlTreeExecution_Response__rosidl_typesupport_introspection_c__ControlTreeExecution_Response_message_member_array,  // message members
  ros_bt_py_interfaces__srv__ControlTreeExecution_Response__rosidl_typesupport_introspection_c__ControlTreeExecution_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  ros_bt_py_interfaces__srv__ControlTreeExecution_Response__rosidl_typesupport_introspection_c__ControlTreeExecution_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ros_bt_py_interfaces__srv__ControlTreeExecution_Response__rosidl_typesupport_introspection_c__ControlTreeExecution_Response_message_type_support_handle = {
  0,
  &ros_bt_py_interfaces__srv__ControlTreeExecution_Response__rosidl_typesupport_introspection_c__ControlTreeExecution_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ros_bt_py_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros_bt_py_interfaces, srv, ControlTreeExecution_Response)() {
  if (!ros_bt_py_interfaces__srv__ControlTreeExecution_Response__rosidl_typesupport_introspection_c__ControlTreeExecution_Response_message_type_support_handle.typesupport_identifier) {
    ros_bt_py_interfaces__srv__ControlTreeExecution_Response__rosidl_typesupport_introspection_c__ControlTreeExecution_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ros_bt_py_interfaces__srv__ControlTreeExecution_Response__rosidl_typesupport_introspection_c__ControlTreeExecution_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "ros_bt_py_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/control_tree_execution__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers ros_bt_py_interfaces__srv__detail__control_tree_execution__rosidl_typesupport_introspection_c__ControlTreeExecution_service_members = {
  "ros_bt_py_interfaces__srv",  // service namespace
  "ControlTreeExecution",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // ros_bt_py_interfaces__srv__detail__control_tree_execution__rosidl_typesupport_introspection_c__ControlTreeExecution_Request_message_type_support_handle,
  NULL  // response message
  // ros_bt_py_interfaces__srv__detail__control_tree_execution__rosidl_typesupport_introspection_c__ControlTreeExecution_Response_message_type_support_handle
};

static rosidl_service_type_support_t ros_bt_py_interfaces__srv__detail__control_tree_execution__rosidl_typesupport_introspection_c__ControlTreeExecution_service_type_support_handle = {
  0,
  &ros_bt_py_interfaces__srv__detail__control_tree_execution__rosidl_typesupport_introspection_c__ControlTreeExecution_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros_bt_py_interfaces, srv, ControlTreeExecution_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros_bt_py_interfaces, srv, ControlTreeExecution_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ros_bt_py_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros_bt_py_interfaces, srv, ControlTreeExecution)() {
  if (!ros_bt_py_interfaces__srv__detail__control_tree_execution__rosidl_typesupport_introspection_c__ControlTreeExecution_service_type_support_handle.typesupport_identifier) {
    ros_bt_py_interfaces__srv__detail__control_tree_execution__rosidl_typesupport_introspection_c__ControlTreeExecution_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)ros_bt_py_interfaces__srv__detail__control_tree_execution__rosidl_typesupport_introspection_c__ControlTreeExecution_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros_bt_py_interfaces, srv, ControlTreeExecution_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros_bt_py_interfaces, srv, ControlTreeExecution_Response)()->data;
  }

  return &ros_bt_py_interfaces__srv__detail__control_tree_execution__rosidl_typesupport_introspection_c__ControlTreeExecution_service_type_support_handle;
}
