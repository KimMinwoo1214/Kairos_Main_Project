// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ros_bt_py_interfaces:msg/RemoteCapabilitySlotStatus.idl
// generated code does not contain a copyright notice
#include "ros_bt_py_interfaces/msg/detail/remote_capability_slot_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `name`
// Member `status`
#include "rosidl_runtime_c/string_functions.h"
// Member `timestamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__init(ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus * msg)
{
  if (!msg) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__init(&msg->name)) {
    ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__fini(msg);
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__init(&msg->status)) {
    ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__fini(msg);
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__init(&msg->timestamp)) {
    ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__fini(msg);
    return false;
  }
  return true;
}

void
ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__fini(ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus * msg)
{
  if (!msg) {
    return;
  }
  // name
  rosidl_runtime_c__String__fini(&msg->name);
  // status
  rosidl_runtime_c__String__fini(&msg->status);
  // timestamp
  builtin_interfaces__msg__Time__fini(&msg->timestamp);
}

bool
ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__are_equal(const ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus * lhs, const ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->name), &(rhs->name)))
  {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->status), &(rhs->status)))
  {
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->timestamp), &(rhs->timestamp)))
  {
    return false;
  }
  return true;
}

bool
ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__copy(
  const ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus * input,
  ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus * output)
{
  if (!input || !output) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__copy(
      &(input->name), &(output->name)))
  {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__copy(
      &(input->status), &(output->status)))
  {
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->timestamp), &(output->timestamp)))
  {
    return false;
  }
  return true;
}

ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus *
ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus * msg = (ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus *)allocator.allocate(sizeof(ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus));
  bool success = ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__destroy(ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence__init(ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus * data = NULL;

  if (size) {
    data = (ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus *)allocator.zero_allocate(size, sizeof(ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence__fini(ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence *
ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence * array = (ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence *)allocator.allocate(sizeof(ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence__destroy(ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence__are_equal(const ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence * lhs, const ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence__copy(
  const ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence * input,
  ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus * data =
      (ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ros_bt_py_interfaces__msg__RemoteCapabilitySlotStatus__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}