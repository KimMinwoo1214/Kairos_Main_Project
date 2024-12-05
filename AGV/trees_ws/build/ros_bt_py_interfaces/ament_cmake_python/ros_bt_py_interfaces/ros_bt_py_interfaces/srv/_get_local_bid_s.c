// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ros_bt_py_interfaces:srv/GetLocalBid.idl
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
#include "ros_bt_py_interfaces/srv/detail/get_local_bid__struct.h"
#include "ros_bt_py_interfaces/srv/detail/get_local_bid__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

bool ros_bt_py_interfaces__msg__capability_interface__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ros_bt_py_interfaces__msg__capability_interface__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool ros_bt_py_interfaces__srv__get_local_bid__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[60];
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
    assert(strncmp("ros_bt_py_interfaces.srv._get_local_bid.GetLocalBid_Request", full_classname_dest, 59) == 0);
  }
  ros_bt_py_interfaces__srv__GetLocalBid_Request * ros_message = _ros_message;
  {  // interface
    PyObject * field = PyObject_GetAttrString(_pymsg, "interface");
    if (!field) {
      return false;
    }
    if (!ros_bt_py_interfaces__msg__capability_interface__convert_from_py(field, &ros_message->interface)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // node_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "node_id");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->node_id, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // implementation_tags_dict
    PyObject * field = PyObject_GetAttrString(_pymsg, "implementation_tags_dict");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->implementation_tags_dict, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ros_bt_py_interfaces__srv__get_local_bid__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of GetLocalBid_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ros_bt_py_interfaces.srv._get_local_bid");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "GetLocalBid_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ros_bt_py_interfaces__srv__GetLocalBid_Request * ros_message = (ros_bt_py_interfaces__srv__GetLocalBid_Request *)raw_ros_message;
  {  // interface
    PyObject * field = NULL;
    field = ros_bt_py_interfaces__msg__capability_interface__convert_to_py(&ros_message->interface);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "interface", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // node_id
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->node_id.data,
      strlen(ros_message->node_id.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "node_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // implementation_tags_dict
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->implementation_tags_dict.data,
      strlen(ros_message->implementation_tags_dict.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "implementation_tags_dict", field);
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
// #include "ros_bt_py_interfaces/srv/detail/get_local_bid__struct.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/get_local_bid__functions.h"

// already included above
// #include "rosidl_runtime_c/string.h"
// already included above
// #include "rosidl_runtime_c/string_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool ros_bt_py_interfaces__srv__get_local_bid__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[61];
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
    assert(strncmp("ros_bt_py_interfaces.srv._get_local_bid.GetLocalBid_Response", full_classname_dest, 60) == 0);
  }
  ros_bt_py_interfaces__srv__GetLocalBid_Response * ros_message = _ros_message;
  {  // implementation_name
    PyObject * field = PyObject_GetAttrString(_pymsg, "implementation_name");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->implementation_name, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // bid
    PyObject * field = PyObject_GetAttrString(_pymsg, "bid");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->bid = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
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
PyObject * ros_bt_py_interfaces__srv__get_local_bid__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of GetLocalBid_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ros_bt_py_interfaces.srv._get_local_bid");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "GetLocalBid_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ros_bt_py_interfaces__srv__GetLocalBid_Response * ros_message = (ros_bt_py_interfaces__srv__GetLocalBid_Response *)raw_ros_message;
  {  // implementation_name
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->implementation_name.data,
      strlen(ros_message->implementation_name.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "implementation_name", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // bid
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->bid);
    {
      int rc = PyObject_SetAttrString(_pymessage, "bid", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
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
