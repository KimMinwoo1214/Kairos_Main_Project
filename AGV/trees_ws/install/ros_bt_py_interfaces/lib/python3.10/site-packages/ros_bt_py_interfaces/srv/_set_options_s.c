// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ros_bt_py_interfaces:srv/SetOptions.idl
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
#include "ros_bt_py_interfaces/srv/detail/set_options__struct.h"
#include "ros_bt_py_interfaces/srv/detail/set_options__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

// Nested array functions includes
#include "ros_bt_py_interfaces/msg/detail/node_data__functions.h"
// end nested array functions include
bool ros_bt_py_interfaces__msg__node_data__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ros_bt_py_interfaces__msg__node_data__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool ros_bt_py_interfaces__srv__set_options__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[57];
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
    assert(strncmp("ros_bt_py_interfaces.srv._set_options.SetOptions_Request", full_classname_dest, 56) == 0);
  }
  ros_bt_py_interfaces__srv__SetOptions_Request * ros_message = _ros_message;
  {  // node_name
    PyObject * field = PyObject_GetAttrString(_pymsg, "node_name");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->node_name, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // rename_node
    PyObject * field = PyObject_GetAttrString(_pymsg, "rename_node");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->rename_node = (Py_True == field);
    Py_DECREF(field);
  }
  {  // new_name
    PyObject * field = PyObject_GetAttrString(_pymsg, "new_name");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->new_name, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // options
    PyObject * field = PyObject_GetAttrString(_pymsg, "options");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'options'");
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
    if (!ros_bt_py_interfaces__msg__NodeData__Sequence__init(&(ros_message->options), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create ros_bt_py_interfaces__msg__NodeData__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    ros_bt_py_interfaces__msg__NodeData * dest = ros_message->options.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!ros_bt_py_interfaces__msg__node_data__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ros_bt_py_interfaces__srv__set_options__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of SetOptions_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ros_bt_py_interfaces.srv._set_options");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "SetOptions_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ros_bt_py_interfaces__srv__SetOptions_Request * ros_message = (ros_bt_py_interfaces__srv__SetOptions_Request *)raw_ros_message;
  {  // node_name
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->node_name.data,
      strlen(ros_message->node_name.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "node_name", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // rename_node
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->rename_node ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "rename_node", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // new_name
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->new_name.data,
      strlen(ros_message->new_name.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "new_name", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // options
    PyObject * field = NULL;
    size_t size = ros_message->options.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    ros_bt_py_interfaces__msg__NodeData * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->options.data[i]);
      PyObject * pyitem = ros_bt_py_interfaces__msg__node_data__convert_to_py(item);
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
      int rc = PyObject_SetAttrString(_pymessage, "options", field);
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
// #include "ros_bt_py_interfaces/srv/detail/set_options__struct.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/set_options__functions.h"

// already included above
// #include "rosidl_runtime_c/string.h"
// already included above
// #include "rosidl_runtime_c/string_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool ros_bt_py_interfaces__srv__set_options__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[58];
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
    assert(strncmp("ros_bt_py_interfaces.srv._set_options.SetOptions_Response", full_classname_dest, 57) == 0);
  }
  ros_bt_py_interfaces__srv__SetOptions_Response * ros_message = _ros_message;
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
PyObject * ros_bt_py_interfaces__srv__set_options__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of SetOptions_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ros_bt_py_interfaces.srv._set_options");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "SetOptions_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ros_bt_py_interfaces__srv__SetOptions_Response * ros_message = (ros_bt_py_interfaces__srv__SetOptions_Response *)raw_ros_message;
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
