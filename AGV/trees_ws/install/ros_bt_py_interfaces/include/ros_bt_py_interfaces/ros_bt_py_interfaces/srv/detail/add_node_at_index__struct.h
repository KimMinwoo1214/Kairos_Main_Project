// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ros_bt_py_interfaces:srv/AddNodeAtIndex.idl
// generated code does not contain a copyright notice

#ifndef ROS_BT_PY_INTERFACES__SRV__DETAIL__ADD_NODE_AT_INDEX__STRUCT_H_
#define ROS_BT_PY_INTERFACES__SRV__DETAIL__ADD_NODE_AT_INDEX__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'parent_name'
#include "rosidl_runtime_c/string.h"
// Member 'node'
#include "ros_bt_py_interfaces/msg/detail/node__struct.h"

/// Struct defined in srv/AddNodeAtIndex in the package ros_bt_py_interfaces.
typedef struct ros_bt_py_interfaces__srv__AddNodeAtIndex_Request
{
  rosidl_runtime_c__String parent_name;
  ros_bt_py_interfaces__msg__Node node;
  /// If this is true, rename the node to name_N if one or more
  /// nodes with the same name / prefix exist already.
  bool allow_rename;
  /// Follows Python convention, i.e. can be negative to count from the
  /// end of the children list.
  int32_t new_child_index;
} ros_bt_py_interfaces__srv__AddNodeAtIndex_Request;

// Struct for a sequence of ros_bt_py_interfaces__srv__AddNodeAtIndex_Request.
typedef struct ros_bt_py_interfaces__srv__AddNodeAtIndex_Request__Sequence
{
  ros_bt_py_interfaces__srv__AddNodeAtIndex_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ros_bt_py_interfaces__srv__AddNodeAtIndex_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'actual_node_name'
// Member 'error_message'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/AddNodeAtIndex in the package ros_bt_py_interfaces.
typedef struct ros_bt_py_interfaces__srv__AddNodeAtIndex_Response
{
  bool success;
  rosidl_runtime_c__String actual_node_name;
  rosidl_runtime_c__String error_message;
} ros_bt_py_interfaces__srv__AddNodeAtIndex_Response;

// Struct for a sequence of ros_bt_py_interfaces__srv__AddNodeAtIndex_Response.
typedef struct ros_bt_py_interfaces__srv__AddNodeAtIndex_Response__Sequence
{
  ros_bt_py_interfaces__srv__AddNodeAtIndex_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ros_bt_py_interfaces__srv__AddNodeAtIndex_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROS_BT_PY_INTERFACES__SRV__DETAIL__ADD_NODE_AT_INDEX__STRUCT_H_