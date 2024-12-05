// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ros_bt_py_interfaces:srv/GetSubtree.idl
// generated code does not contain a copyright notice
#include "ros_bt_py_interfaces/srv/detail/get_subtree__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `subtree_root_name`
#include "rosidl_runtime_c/string_functions.h"

bool
ros_bt_py_interfaces__srv__GetSubtree_Request__init(ros_bt_py_interfaces__srv__GetSubtree_Request * msg)
{
  if (!msg) {
    return false;
  }
  // subtree_root_name
  if (!rosidl_runtime_c__String__init(&msg->subtree_root_name)) {
    ros_bt_py_interfaces__srv__GetSubtree_Request__fini(msg);
    return false;
  }
  return true;
}

void
ros_bt_py_interfaces__srv__GetSubtree_Request__fini(ros_bt_py_interfaces__srv__GetSubtree_Request * msg)
{
  if (!msg) {
    return;
  }
  // subtree_root_name
  rosidl_runtime_c__String__fini(&msg->subtree_root_name);
}

bool
ros_bt_py_interfaces__srv__GetSubtree_Request__are_equal(const ros_bt_py_interfaces__srv__GetSubtree_Request * lhs, const ros_bt_py_interfaces__srv__GetSubtree_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // subtree_root_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->subtree_root_name), &(rhs->subtree_root_name)))
  {
    return false;
  }
  return true;
}

bool
ros_bt_py_interfaces__srv__GetSubtree_Request__copy(
  const ros_bt_py_interfaces__srv__GetSubtree_Request * input,
  ros_bt_py_interfaces__srv__GetSubtree_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // subtree_root_name
  if (!rosidl_runtime_c__String__copy(
      &(input->subtree_root_name), &(output->subtree_root_name)))
  {
    return false;
  }
  return true;
}

ros_bt_py_interfaces__srv__GetSubtree_Request *
ros_bt_py_interfaces__srv__GetSubtree_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros_bt_py_interfaces__srv__GetSubtree_Request * msg = (ros_bt_py_interfaces__srv__GetSubtree_Request *)allocator.allocate(sizeof(ros_bt_py_interfaces__srv__GetSubtree_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ros_bt_py_interfaces__srv__GetSubtree_Request));
  bool success = ros_bt_py_interfaces__srv__GetSubtree_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ros_bt_py_interfaces__srv__GetSubtree_Request__destroy(ros_bt_py_interfaces__srv__GetSubtree_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ros_bt_py_interfaces__srv__GetSubtree_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence__init(ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros_bt_py_interfaces__srv__GetSubtree_Request * data = NULL;

  if (size) {
    data = (ros_bt_py_interfaces__srv__GetSubtree_Request *)allocator.zero_allocate(size, sizeof(ros_bt_py_interfaces__srv__GetSubtree_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ros_bt_py_interfaces__srv__GetSubtree_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ros_bt_py_interfaces__srv__GetSubtree_Request__fini(&data[i - 1]);
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
ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence__fini(ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence * array)
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
      ros_bt_py_interfaces__srv__GetSubtree_Request__fini(&array->data[i]);
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

ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence *
ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence * array = (ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence *)allocator.allocate(sizeof(ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence__destroy(ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence__are_equal(const ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence * lhs, const ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ros_bt_py_interfaces__srv__GetSubtree_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence__copy(
  const ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence * input,
  ros_bt_py_interfaces__srv__GetSubtree_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ros_bt_py_interfaces__srv__GetSubtree_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ros_bt_py_interfaces__srv__GetSubtree_Request * data =
      (ros_bt_py_interfaces__srv__GetSubtree_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ros_bt_py_interfaces__srv__GetSubtree_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ros_bt_py_interfaces__srv__GetSubtree_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ros_bt_py_interfaces__srv__GetSubtree_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `error_message`
// already included above
// #include "rosidl_runtime_c/string_functions.h"
// Member `subtree`
#include "ros_bt_py_interfaces/msg/detail/tree__functions.h"

bool
ros_bt_py_interfaces__srv__GetSubtree_Response__init(ros_bt_py_interfaces__srv__GetSubtree_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  // error_message
  if (!rosidl_runtime_c__String__init(&msg->error_message)) {
    ros_bt_py_interfaces__srv__GetSubtree_Response__fini(msg);
    return false;
  }
  // subtree
  if (!ros_bt_py_interfaces__msg__Tree__init(&msg->subtree)) {
    ros_bt_py_interfaces__srv__GetSubtree_Response__fini(msg);
    return false;
  }
  return true;
}

void
ros_bt_py_interfaces__srv__GetSubtree_Response__fini(ros_bt_py_interfaces__srv__GetSubtree_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
  // error_message
  rosidl_runtime_c__String__fini(&msg->error_message);
  // subtree
  ros_bt_py_interfaces__msg__Tree__fini(&msg->subtree);
}

bool
ros_bt_py_interfaces__srv__GetSubtree_Response__are_equal(const ros_bt_py_interfaces__srv__GetSubtree_Response * lhs, const ros_bt_py_interfaces__srv__GetSubtree_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // error_message
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->error_message), &(rhs->error_message)))
  {
    return false;
  }
  // subtree
  if (!ros_bt_py_interfaces__msg__Tree__are_equal(
      &(lhs->subtree), &(rhs->subtree)))
  {
    return false;
  }
  return true;
}

bool
ros_bt_py_interfaces__srv__GetSubtree_Response__copy(
  const ros_bt_py_interfaces__srv__GetSubtree_Response * input,
  ros_bt_py_interfaces__srv__GetSubtree_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  // error_message
  if (!rosidl_runtime_c__String__copy(
      &(input->error_message), &(output->error_message)))
  {
    return false;
  }
  // subtree
  if (!ros_bt_py_interfaces__msg__Tree__copy(
      &(input->subtree), &(output->subtree)))
  {
    return false;
  }
  return true;
}

ros_bt_py_interfaces__srv__GetSubtree_Response *
ros_bt_py_interfaces__srv__GetSubtree_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros_bt_py_interfaces__srv__GetSubtree_Response * msg = (ros_bt_py_interfaces__srv__GetSubtree_Response *)allocator.allocate(sizeof(ros_bt_py_interfaces__srv__GetSubtree_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ros_bt_py_interfaces__srv__GetSubtree_Response));
  bool success = ros_bt_py_interfaces__srv__GetSubtree_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ros_bt_py_interfaces__srv__GetSubtree_Response__destroy(ros_bt_py_interfaces__srv__GetSubtree_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ros_bt_py_interfaces__srv__GetSubtree_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence__init(ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros_bt_py_interfaces__srv__GetSubtree_Response * data = NULL;

  if (size) {
    data = (ros_bt_py_interfaces__srv__GetSubtree_Response *)allocator.zero_allocate(size, sizeof(ros_bt_py_interfaces__srv__GetSubtree_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ros_bt_py_interfaces__srv__GetSubtree_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ros_bt_py_interfaces__srv__GetSubtree_Response__fini(&data[i - 1]);
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
ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence__fini(ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence * array)
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
      ros_bt_py_interfaces__srv__GetSubtree_Response__fini(&array->data[i]);
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

ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence *
ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence * array = (ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence *)allocator.allocate(sizeof(ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence__destroy(ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence__are_equal(const ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence * lhs, const ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ros_bt_py_interfaces__srv__GetSubtree_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence__copy(
  const ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence * input,
  ros_bt_py_interfaces__srv__GetSubtree_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ros_bt_py_interfaces__srv__GetSubtree_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ros_bt_py_interfaces__srv__GetSubtree_Response * data =
      (ros_bt_py_interfaces__srv__GetSubtree_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ros_bt_py_interfaces__srv__GetSubtree_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ros_bt_py_interfaces__srv__GetSubtree_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ros_bt_py_interfaces__srv__GetSubtree_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}