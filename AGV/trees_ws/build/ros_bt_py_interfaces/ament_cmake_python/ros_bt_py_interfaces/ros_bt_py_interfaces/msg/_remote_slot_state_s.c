// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ros_bt_py_interfaces:msg/RemoteSlotState.idl
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
#include "ros_bt_py_interfaces/msg/detail/remote_slot_state__struct.h"
#include "ros_bt_py_interfaces/msg/detail/remote_slot_state__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool ros_bt_py_interfaces__msg__remote_slot_state__convert_from_py(PyObject * _pymsg, void * _ros_message)
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
    assert(strncmp("ros_bt_py_interfaces.msg._remote_slot_state.RemoteSlotState", full_classname_dest, 59) == 0);
  }
  ros_bt_py_interfaces__msg__RemoteSlotState * ros_message = _ros_message;
  {  // tree_in_slot
    PyObject * field = PyObject_GetAttrString(_pymsg, "tree_in_slot");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->tree_in_slot = (Py_True == field);
    Py_DECREF(field);
  }
  {  // tree_running
    PyObject * field = PyObject_GetAttrString(_pymsg, "tree_running");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->tree_running = (Py_True == field);
    Py_DECREF(field);
  }
  {  // tree_finished
    PyObject * field = PyObject_GetAttrString(_pymsg, "tree_finished");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->tree_finished = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ros_bt_py_interfaces__msg__remote_slot_state__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of RemoteSlotState */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ros_bt_py_interfaces.msg._remote_slot_state");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "RemoteSlotState");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ros_bt_py_interfaces__msg__RemoteSlotState * ros_message = (ros_bt_py_interfaces__msg__RemoteSlotState *)raw_ros_message;
  {  // tree_in_slot
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->tree_in_slot ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tree_in_slot", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tree_running
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->tree_running ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tree_running", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tree_finished
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->tree_finished ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tree_finished", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
