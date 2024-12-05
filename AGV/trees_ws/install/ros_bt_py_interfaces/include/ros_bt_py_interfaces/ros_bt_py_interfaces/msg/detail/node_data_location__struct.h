// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ros_bt_py_interfaces:msg/NodeDataLocation.idl
// generated code does not contain a copyright notice

#ifndef ROS_BT_PY_INTERFACES__MSG__DETAIL__NODE_DATA_LOCATION__STRUCT_H_
#define ROS_BT_PY_INTERFACES__MSG__DETAIL__NODE_DATA_LOCATION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'INPUT_DATA'.
static const char * const ros_bt_py_interfaces__msg__NodeDataLocation__INPUT_DATA = "inputs";

/// Constant 'OUTPUT_DATA'.
static const char * const ros_bt_py_interfaces__msg__NodeDataLocation__OUTPUT_DATA = "outputs";

/// Constant 'OPTION_DATA'.
static const char * const ros_bt_py_interfaces__msg__NodeDataLocation__OPTION_DATA = "options";

// Include directives for member types
// Member 'node_name'
// Member 'data_kind'
// Member 'data_key'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/NodeDataLocation in the package ros_bt_py_interfaces.
/**
  * Copyright 2023 FZI Forschungszentrum Informatik
  *
  * Redistribution and use in source and binary forms, with or without
  * modification, are permitted provided that the following conditions are met:
  *
  *    * Redistributions of source code must retain the above copyright
  *      notice, this list of conditions and the following disclaimer.
  *
  *    * Redistributions in binary form must reproduce the above copyright
  *      notice, this list of conditions and the following disclaimer in the
  *      documentation and/or other materials provided with the distribution.
  *
  *    * Neither the name of the FZI Forschungszentrum Informatik nor the names of its
  *      contributors may be used to endorse or promote products derived from
  *      this software without specific prior written permission.
  *
  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
  * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
  * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
  * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
  * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
  * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
  * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
  * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
  * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
  * POSSIBILITY OF SUCH DAMAGE.
 */
typedef struct ros_bt_py_interfaces__msg__NodeDataLocation
{
  rosidl_runtime_c__String node_name;
  rosidl_runtime_c__String data_kind;
  rosidl_runtime_c__String data_key;
} ros_bt_py_interfaces__msg__NodeDataLocation;

// Struct for a sequence of ros_bt_py_interfaces__msg__NodeDataLocation.
typedef struct ros_bt_py_interfaces__msg__NodeDataLocation__Sequence
{
  ros_bt_py_interfaces__msg__NodeDataLocation * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ros_bt_py_interfaces__msg__NodeDataLocation__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROS_BT_PY_INTERFACES__MSG__DETAIL__NODE_DATA_LOCATION__STRUCT_H_