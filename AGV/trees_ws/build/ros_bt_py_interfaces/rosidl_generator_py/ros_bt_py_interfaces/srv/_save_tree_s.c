// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ros_bt_py_interfaces:srv/SaveTree.idl
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
#include "ros_bt_py_interfaces/srv/detail/save_tree__struct.h"
#include "ros_bt_py_interfaces/srv/detail/save_tree__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

bool ros_bt_py_interfaces__msg__tree__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ros_bt_py_interfaces__msg__tree__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool ros_bt_py_interfaces__srv__save_tree__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[53];
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
    assert(strncmp("ros_bt_py_interfaces.srv._save_tree.SaveTree_Request", full_classname_dest, 52) == 0);
  }
  ros_bt_py_interfaces__srv__SaveTree_Request * ros_message = _ros_message;
  {  // storage_path
    PyObject * field = PyObject_GetAttrString(_pymsg, "storage_path");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->storage_path, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // filepath
    PyObject * field = PyObject_GetAttrString(_pymsg, "filepath");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->filepath, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // tree
    PyObject * field = PyObject_GetAttrString(_pymsg, "tree");
    if (!field) {
      return false;
    }
    if (!ros_bt_py_interfaces__msg__tree__convert_from_py(field, &ros_message->tree)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // allow_overwrite
    PyObject * field = PyObject_GetAttrString(_pymsg, "allow_overwrite");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->allow_overwrite = (Py_True == field);
    Py_DECREF(field);
  }
  {  // allow_rename
    PyObject * field = PyObject_GetAttrString(_pymsg, "allow_rename");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->allow_rename = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ros_bt_py_interfaces__srv__save_tree__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of SaveTree_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ros_bt_py_interfaces.srv._save_tree");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "SaveTree_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ros_bt_py_interfaces__srv__SaveTree_Request * ros_message = (ros_bt_py_interfaces__srv__SaveTree_Request *)raw_ros_message;
  {  // storage_path
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->storage_path.data,
      strlen(ros_message->storage_path.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "storage_path", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // filepath
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->filepath.data,
      strlen(ros_message->filepath.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "filepath", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tree
    PyObject * field = NULL;
    field = ros_bt_py_interfaces__msg__tree__convert_to_py(&ros_message->tree);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "tree", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // allow_overwrite
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->allow_overwrite ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "allow_overwrite", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // allow_rename
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->allow_rename ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "allow_rename", field);
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
// #include "ros_bt_py_interfaces/srv/detail/save_tree__struct.h"
// already included above
// #include "ros_bt_py_interfaces/srv/detail/save_tree__functions.h"

// already included above
// #include "rosidl_runtime_c/string.h"
// already included above
// #include "rosidl_runtime_c/string_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool ros_bt_py_interfaces__srv__save_tree__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[54];
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
    assert(strncmp("ros_bt_py_interfaces.srv._save_tree.SaveTree_Response", full_classname_dest, 53) == 0);
  }
  ros_bt_py_interfaces__srv__SaveTree_Response * ros_message = _ros_message;
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
  {  // file_path
    PyObject * field = PyObject_GetAttrString(_pymsg, "file_path");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->file_path, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ros_bt_py_interfaces__srv__save_tree__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of SaveTree_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ros_bt_py_interfaces.srv._save_tree");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "SaveTree_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ros_bt_py_interfaces__srv__SaveTree_Response * ros_message = (ros_bt_py_interfaces__srv__SaveTree_Response *)raw_ros_message;
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
  {  // file_path
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->file_path.data,
      strlen(ros_message->file_path.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "file_path", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
