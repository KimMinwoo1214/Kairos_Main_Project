// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ros_bt_py_interfaces:msg/UtilityBounds.idl
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
#include "ros_bt_py_interfaces/msg/detail/utility_bounds__struct.h"
#include "ros_bt_py_interfaces/msg/detail/utility_bounds__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool ros_bt_py_interfaces__msg__utility_bounds__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[55];
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
    assert(strncmp("ros_bt_py_interfaces.msg._utility_bounds.UtilityBounds", full_classname_dest, 54) == 0);
  }
  ros_bt_py_interfaces__msg__UtilityBounds * ros_message = _ros_message;
  {  // can_execute
    PyObject * field = PyObject_GetAttrString(_pymsg, "can_execute");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->can_execute = (Py_True == field);
    Py_DECREF(field);
  }
  {  // has_upper_bound_success
    PyObject * field = PyObject_GetAttrString(_pymsg, "has_upper_bound_success");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->has_upper_bound_success = (Py_True == field);
    Py_DECREF(field);
  }
  {  // upper_bound_success
    PyObject * field = PyObject_GetAttrString(_pymsg, "upper_bound_success");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->upper_bound_success = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // has_lower_bound_success
    PyObject * field = PyObject_GetAttrString(_pymsg, "has_lower_bound_success");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->has_lower_bound_success = (Py_True == field);
    Py_DECREF(field);
  }
  {  // lower_bound_success
    PyObject * field = PyObject_GetAttrString(_pymsg, "lower_bound_success");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->lower_bound_success = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // has_upper_bound_failure
    PyObject * field = PyObject_GetAttrString(_pymsg, "has_upper_bound_failure");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->has_upper_bound_failure = (Py_True == field);
    Py_DECREF(field);
  }
  {  // upper_bound_failure
    PyObject * field = PyObject_GetAttrString(_pymsg, "upper_bound_failure");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->upper_bound_failure = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // has_lower_bound_failure
    PyObject * field = PyObject_GetAttrString(_pymsg, "has_lower_bound_failure");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->has_lower_bound_failure = (Py_True == field);
    Py_DECREF(field);
  }
  {  // lower_bound_failure
    PyObject * field = PyObject_GetAttrString(_pymsg, "lower_bound_failure");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->lower_bound_failure = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ros_bt_py_interfaces__msg__utility_bounds__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of UtilityBounds */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ros_bt_py_interfaces.msg._utility_bounds");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "UtilityBounds");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ros_bt_py_interfaces__msg__UtilityBounds * ros_message = (ros_bt_py_interfaces__msg__UtilityBounds *)raw_ros_message;
  {  // can_execute
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->can_execute ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "can_execute", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // has_upper_bound_success
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->has_upper_bound_success ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "has_upper_bound_success", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // upper_bound_success
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->upper_bound_success);
    {
      int rc = PyObject_SetAttrString(_pymessage, "upper_bound_success", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // has_lower_bound_success
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->has_lower_bound_success ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "has_lower_bound_success", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lower_bound_success
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->lower_bound_success);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lower_bound_success", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // has_upper_bound_failure
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->has_upper_bound_failure ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "has_upper_bound_failure", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // upper_bound_failure
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->upper_bound_failure);
    {
      int rc = PyObject_SetAttrString(_pymessage, "upper_bound_failure", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // has_lower_bound_failure
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->has_lower_bound_failure ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "has_lower_bound_failure", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lower_bound_failure
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->lower_bound_failure);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lower_bound_failure", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
