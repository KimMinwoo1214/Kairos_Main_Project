// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ros_bt_py_interfaces:srv/WireNodeData.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "ros_bt_py_interfaces/srv/detail/wire_node_data__struct.h"
#include "ros_bt_py_interfaces/srv/detail/wire_node_data__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

// Nested array functions includes
#include "ros_bt_py_interfaces/msg/detail/node_data_wiring__functions.h"
// end nested array functions include
bool ros_bt_py_interfaces__msg__node_data_wiring__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ros_bt_py_interfaces__msg__node_data_wiring__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool ros_bt_py_interfaces__srv__wire_node_data__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[62];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("ros_bt_py_interfaces.srv._wire_node_data.WireNodeData_Request", full_classname_dest, 61) == 0);
  }
  ros_bt_py_interfaces__srv__WireNodeData_Request * ros_message = _ros_message;
  {  // wirings
    PyObject * field = PyObject_GetAttrString(_pymsg, "wirings");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'wirings'");
    if (!seq_field) {
      Py_DECREF(field);
      return false;
    }
    Py_ssize_t size = PySequence_Size(field);
    if (-1 == size) {
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    if (!ros_bt_py_interfaces__msg__NodeDataWiring__Sequence__init(&(ros_message->wirings), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create ros_bt_py_interfaces__msg__NodeDataWiring__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    ros_bt_py_interfaces__msg__NodeDataWiring * dest = ros_message->wirings.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!ros_bt_py_interfaces__msg__node_data_wiring__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // ignore_failure
    PyObject * field = PyObject_GetAttrString(_pymsg, "ignore_failure");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->ignore_failure = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ros_bt_py_interfaces__srv__wire_node_data__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of WireNodeData_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ros_bt_py_interfaces.srv._wire_node_data");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "WireNodeData_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ros_bt_py_interfaces__srv__WireNodeData_Request * ros_message = (ros_bt_py_interfaces__srv__WireNodeData_Request *)raw_ros_message;
  {  // wirings
    PyObject * field = NULL;
    size_t size = ros_message->wirings.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    ros_bt_py_interfaces__msg__NodeDataWiring * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->wirings.data[i]);
      PyObject * pyitem = ros_bt_py_interfaces__msg__node_data_wiring__convert_to_py(item);
      if (!pyitem) {
        Py_DECREF(field);
        return NULL;
      }
      int rc = PyList_SetItem(field, i, pyitem);
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    {
      int rc = PyObject_SetAttrString(_pymessage, "wirings", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ignore_failure
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->ignore_failure ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ignore_failure", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/wire_node_data__struct.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/wire_node_data__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool ros_bt_py_interfaces__srv__wire_node_data__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[63];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("ros_bt_py_interfaces.srv._wire_node_data.WireNodeData_Response", full_classname_dest, 62) == 0);
  }
  ros_bt_py_interfaces__srv__WireNodeData_Response * ros_message = _ros_message;
  {  // success
    PyObject * field = PyObject_GetAttrString(_pymsg, "success");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->success = (Py_True == field);
    Py_DECREF(field);
  }
  {  // error_message
    PyObject * field = PyObject_GetAttrString(_pymsg, "error_message");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->error_message, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ros_bt_py_interfaces__srv__wire_node_data__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of WireNodeData_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ros_bt_py_interfaces.srv._wire_node_data");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "WireNodeData_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ros_bt_py_interfaces__srv__WireNodeData_Response * ros_message = (ros_bt_py_interfaces__srv__WireNodeData_Response *)raw_ros_message;
  {  // success
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->success ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "success", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // error_message
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->error_message.data,
      strlen(ros_message->error_message.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "error_message", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
