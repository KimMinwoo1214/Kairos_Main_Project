// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from ros_bt_py_interfaces:action/FindBestExecutor.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace ros_bt_py_interfaces
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _FindBestExecutor_Goal_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _FindBestExecutor_Goal_type_support_ids_t;

static const _FindBestExecutor_Goal_type_support_ids_t _FindBestExecutor_Goal_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _FindBestExecutor_Goal_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _FindBestExecutor_Goal_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _FindBestExecutor_Goal_type_support_symbol_names_t _FindBestExecutor_Goal_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, action, FindBestExecutor_Goal)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, action, FindBestExecutor_Goal)),
  }
};

typedef struct _FindBestExecutor_Goal_type_support_data_t
{
  void * data[2];
} _FindBestExecutor_Goal_type_support_data_t;

static _FindBestExecutor_Goal_type_support_data_t _FindBestExecutor_Goal_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _FindBestExecutor_Goal_message_typesupport_map = {
  2,
  "ros_bt_py_interfaces",
  &_FindBestExecutor_Goal_message_typesupport_ids.typesupport_identifier[0],
  &_FindBestExecutor_Goal_message_typesupport_symbol_names.symbol_name[0],
  &_FindBestExecutor_Goal_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t FindBestExecutor_Goal_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_FindBestExecutor_Goal_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_Goal>()
{
  return &::ros_bt_py_interfaces::action::rosidl_typesupport_cpp::FindBestExecutor_Goal_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, ros_bt_py_interfaces, action, FindBestExecutor_Goal)() {
  return get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_Goal>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ros_bt_py_interfaces
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _FindBestExecutor_Result_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _FindBestExecutor_Result_type_support_ids_t;

static const _FindBestExecutor_Result_type_support_ids_t _FindBestExecutor_Result_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _FindBestExecutor_Result_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _FindBestExecutor_Result_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _FindBestExecutor_Result_type_support_symbol_names_t _FindBestExecutor_Result_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, action, FindBestExecutor_Result)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, action, FindBestExecutor_Result)),
  }
};

typedef struct _FindBestExecutor_Result_type_support_data_t
{
  void * data[2];
} _FindBestExecutor_Result_type_support_data_t;

static _FindBestExecutor_Result_type_support_data_t _FindBestExecutor_Result_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _FindBestExecutor_Result_message_typesupport_map = {
  2,
  "ros_bt_py_interfaces",
  &_FindBestExecutor_Result_message_typesupport_ids.typesupport_identifier[0],
  &_FindBestExecutor_Result_message_typesupport_symbol_names.symbol_name[0],
  &_FindBestExecutor_Result_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t FindBestExecutor_Result_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_FindBestExecutor_Result_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_Result>()
{
  return &::ros_bt_py_interfaces::action::rosidl_typesupport_cpp::FindBestExecutor_Result_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, ros_bt_py_interfaces, action, FindBestExecutor_Result)() {
  return get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_Result>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ros_bt_py_interfaces
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _FindBestExecutor_Feedback_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _FindBestExecutor_Feedback_type_support_ids_t;

static const _FindBestExecutor_Feedback_type_support_ids_t _FindBestExecutor_Feedback_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _FindBestExecutor_Feedback_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _FindBestExecutor_Feedback_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _FindBestExecutor_Feedback_type_support_symbol_names_t _FindBestExecutor_Feedback_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, action, FindBestExecutor_Feedback)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, action, FindBestExecutor_Feedback)),
  }
};

typedef struct _FindBestExecutor_Feedback_type_support_data_t
{
  void * data[2];
} _FindBestExecutor_Feedback_type_support_data_t;

static _FindBestExecutor_Feedback_type_support_data_t _FindBestExecutor_Feedback_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _FindBestExecutor_Feedback_message_typesupport_map = {
  2,
  "ros_bt_py_interfaces",
  &_FindBestExecutor_Feedback_message_typesupport_ids.typesupport_identifier[0],
  &_FindBestExecutor_Feedback_message_typesupport_symbol_names.symbol_name[0],
  &_FindBestExecutor_Feedback_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t FindBestExecutor_Feedback_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_FindBestExecutor_Feedback_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_Feedback>()
{
  return &::ros_bt_py_interfaces::action::rosidl_typesupport_cpp::FindBestExecutor_Feedback_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, ros_bt_py_interfaces, action, FindBestExecutor_Feedback)() {
  return get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_Feedback>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ros_bt_py_interfaces
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _FindBestExecutor_SendGoal_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _FindBestExecutor_SendGoal_Request_type_support_ids_t;

static const _FindBestExecutor_SendGoal_Request_type_support_ids_t _FindBestExecutor_SendGoal_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _FindBestExecutor_SendGoal_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _FindBestExecutor_SendGoal_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _FindBestExecutor_SendGoal_Request_type_support_symbol_names_t _FindBestExecutor_SendGoal_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, action, FindBestExecutor_SendGoal_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, action, FindBestExecutor_SendGoal_Request)),
  }
};

typedef struct _FindBestExecutor_SendGoal_Request_type_support_data_t
{
  void * data[2];
} _FindBestExecutor_SendGoal_Request_type_support_data_t;

static _FindBestExecutor_SendGoal_Request_type_support_data_t _FindBestExecutor_SendGoal_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _FindBestExecutor_SendGoal_Request_message_typesupport_map = {
  2,
  "ros_bt_py_interfaces",
  &_FindBestExecutor_SendGoal_Request_message_typesupport_ids.typesupport_identifier[0],
  &_FindBestExecutor_SendGoal_Request_message_typesupport_symbol_names.symbol_name[0],
  &_FindBestExecutor_SendGoal_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t FindBestExecutor_SendGoal_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_FindBestExecutor_SendGoal_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request>()
{
  return &::ros_bt_py_interfaces::action::rosidl_typesupport_cpp::FindBestExecutor_SendGoal_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, ros_bt_py_interfaces, action, FindBestExecutor_SendGoal_Request)() {
  return get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ros_bt_py_interfaces
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _FindBestExecutor_SendGoal_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _FindBestExecutor_SendGoal_Response_type_support_ids_t;

static const _FindBestExecutor_SendGoal_Response_type_support_ids_t _FindBestExecutor_SendGoal_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _FindBestExecutor_SendGoal_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _FindBestExecutor_SendGoal_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _FindBestExecutor_SendGoal_Response_type_support_symbol_names_t _FindBestExecutor_SendGoal_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, action, FindBestExecutor_SendGoal_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, action, FindBestExecutor_SendGoal_Response)),
  }
};

typedef struct _FindBestExecutor_SendGoal_Response_type_support_data_t
{
  void * data[2];
} _FindBestExecutor_SendGoal_Response_type_support_data_t;

static _FindBestExecutor_SendGoal_Response_type_support_data_t _FindBestExecutor_SendGoal_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _FindBestExecutor_SendGoal_Response_message_typesupport_map = {
  2,
  "ros_bt_py_interfaces",
  &_FindBestExecutor_SendGoal_Response_message_typesupport_ids.typesupport_identifier[0],
  &_FindBestExecutor_SendGoal_Response_message_typesupport_symbol_names.symbol_name[0],
  &_FindBestExecutor_SendGoal_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t FindBestExecutor_SendGoal_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_FindBestExecutor_SendGoal_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response>()
{
  return &::ros_bt_py_interfaces::action::rosidl_typesupport_cpp::FindBestExecutor_SendGoal_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, ros_bt_py_interfaces, action, FindBestExecutor_SendGoal_Response)() {
  return get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ros_bt_py_interfaces
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _FindBestExecutor_SendGoal_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _FindBestExecutor_SendGoal_type_support_ids_t;

static const _FindBestExecutor_SendGoal_type_support_ids_t _FindBestExecutor_SendGoal_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _FindBestExecutor_SendGoal_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _FindBestExecutor_SendGoal_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _FindBestExecutor_SendGoal_type_support_symbol_names_t _FindBestExecutor_SendGoal_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, action, FindBestExecutor_SendGoal)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, action, FindBestExecutor_SendGoal)),
  }
};

typedef struct _FindBestExecutor_SendGoal_type_support_data_t
{
  void * data[2];
} _FindBestExecutor_SendGoal_type_support_data_t;

static _FindBestExecutor_SendGoal_type_support_data_t _FindBestExecutor_SendGoal_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _FindBestExecutor_SendGoal_service_typesupport_map = {
  2,
  "ros_bt_py_interfaces",
  &_FindBestExecutor_SendGoal_service_typesupport_ids.typesupport_identifier[0],
  &_FindBestExecutor_SendGoal_service_typesupport_symbol_names.symbol_name[0],
  &_FindBestExecutor_SendGoal_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t FindBestExecutor_SendGoal_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_FindBestExecutor_SendGoal_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_SendGoal>()
{
  return &::ros_bt_py_interfaces::action::rosidl_typesupport_cpp::FindBestExecutor_SendGoal_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ros_bt_py_interfaces
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _FindBestExecutor_GetResult_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _FindBestExecutor_GetResult_Request_type_support_ids_t;

static const _FindBestExecutor_GetResult_Request_type_support_ids_t _FindBestExecutor_GetResult_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _FindBestExecutor_GetResult_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _FindBestExecutor_GetResult_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _FindBestExecutor_GetResult_Request_type_support_symbol_names_t _FindBestExecutor_GetResult_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, action, FindBestExecutor_GetResult_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, action, FindBestExecutor_GetResult_Request)),
  }
};

typedef struct _FindBestExecutor_GetResult_Request_type_support_data_t
{
  void * data[2];
} _FindBestExecutor_GetResult_Request_type_support_data_t;

static _FindBestExecutor_GetResult_Request_type_support_data_t _FindBestExecutor_GetResult_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _FindBestExecutor_GetResult_Request_message_typesupport_map = {
  2,
  "ros_bt_py_interfaces",
  &_FindBestExecutor_GetResult_Request_message_typesupport_ids.typesupport_identifier[0],
  &_FindBestExecutor_GetResult_Request_message_typesupport_symbol_names.symbol_name[0],
  &_FindBestExecutor_GetResult_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t FindBestExecutor_GetResult_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_FindBestExecutor_GetResult_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request>()
{
  return &::ros_bt_py_interfaces::action::rosidl_typesupport_cpp::FindBestExecutor_GetResult_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, ros_bt_py_interfaces, action, FindBestExecutor_GetResult_Request)() {
  return get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ros_bt_py_interfaces
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _FindBestExecutor_GetResult_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _FindBestExecutor_GetResult_Response_type_support_ids_t;

static const _FindBestExecutor_GetResult_Response_type_support_ids_t _FindBestExecutor_GetResult_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _FindBestExecutor_GetResult_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _FindBestExecutor_GetResult_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _FindBestExecutor_GetResult_Response_type_support_symbol_names_t _FindBestExecutor_GetResult_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, action, FindBestExecutor_GetResult_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, action, FindBestExecutor_GetResult_Response)),
  }
};

typedef struct _FindBestExecutor_GetResult_Response_type_support_data_t
{
  void * data[2];
} _FindBestExecutor_GetResult_Response_type_support_data_t;

static _FindBestExecutor_GetResult_Response_type_support_data_t _FindBestExecutor_GetResult_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _FindBestExecutor_GetResult_Response_message_typesupport_map = {
  2,
  "ros_bt_py_interfaces",
  &_FindBestExecutor_GetResult_Response_message_typesupport_ids.typesupport_identifier[0],
  &_FindBestExecutor_GetResult_Response_message_typesupport_symbol_names.symbol_name[0],
  &_FindBestExecutor_GetResult_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t FindBestExecutor_GetResult_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_FindBestExecutor_GetResult_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response>()
{
  return &::ros_bt_py_interfaces::action::rosidl_typesupport_cpp::FindBestExecutor_GetResult_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, ros_bt_py_interfaces, action, FindBestExecutor_GetResult_Response)() {
  return get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_GetResult_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ros_bt_py_interfaces
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _FindBestExecutor_GetResult_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _FindBestExecutor_GetResult_type_support_ids_t;

static const _FindBestExecutor_GetResult_type_support_ids_t _FindBestExecutor_GetResult_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _FindBestExecutor_GetResult_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _FindBestExecutor_GetResult_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _FindBestExecutor_GetResult_type_support_symbol_names_t _FindBestExecutor_GetResult_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, action, FindBestExecutor_GetResult)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, action, FindBestExecutor_GetResult)),
  }
};

typedef struct _FindBestExecutor_GetResult_type_support_data_t
{
  void * data[2];
} _FindBestExecutor_GetResult_type_support_data_t;

static _FindBestExecutor_GetResult_type_support_data_t _FindBestExecutor_GetResult_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _FindBestExecutor_GetResult_service_typesupport_map = {
  2,
  "ros_bt_py_interfaces",
  &_FindBestExecutor_GetResult_service_typesupport_ids.typesupport_identifier[0],
  &_FindBestExecutor_GetResult_service_typesupport_symbol_names.symbol_name[0],
  &_FindBestExecutor_GetResult_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t FindBestExecutor_GetResult_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_FindBestExecutor_GetResult_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_GetResult>()
{
  return &::ros_bt_py_interfaces::action::rosidl_typesupport_cpp::FindBestExecutor_GetResult_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ros_bt_py_interfaces
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _FindBestExecutor_FeedbackMessage_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _FindBestExecutor_FeedbackMessage_type_support_ids_t;

static const _FindBestExecutor_FeedbackMessage_type_support_ids_t _FindBestExecutor_FeedbackMessage_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _FindBestExecutor_FeedbackMessage_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _FindBestExecutor_FeedbackMessage_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _FindBestExecutor_FeedbackMessage_type_support_symbol_names_t _FindBestExecutor_FeedbackMessage_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ros_bt_py_interfaces, action, FindBestExecutor_FeedbackMessage)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ros_bt_py_interfaces, action, FindBestExecutor_FeedbackMessage)),
  }
};

typedef struct _FindBestExecutor_FeedbackMessage_type_support_data_t
{
  void * data[2];
} _FindBestExecutor_FeedbackMessage_type_support_data_t;

static _FindBestExecutor_FeedbackMessage_type_support_data_t _FindBestExecutor_FeedbackMessage_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _FindBestExecutor_FeedbackMessage_message_typesupport_map = {
  2,
  "ros_bt_py_interfaces",
  &_FindBestExecutor_FeedbackMessage_message_typesupport_ids.typesupport_identifier[0],
  &_FindBestExecutor_FeedbackMessage_message_typesupport_symbol_names.symbol_name[0],
  &_FindBestExecutor_FeedbackMessage_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t FindBestExecutor_FeedbackMessage_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_FindBestExecutor_FeedbackMessage_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage>()
{
  return &::ros_bt_py_interfaces::action::rosidl_typesupport_cpp::FindBestExecutor_FeedbackMessage_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, ros_bt_py_interfaces, action, FindBestExecutor_FeedbackMessage)() {
  return get_message_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor_FeedbackMessage>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

#include "action_msgs/msg/goal_status_array.hpp"
#include "action_msgs/srv/cancel_goal.hpp"
// already included above
// #include "ros_bt_py_interfaces/action/detail/find_best_executor__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_runtime_c/action_type_support_struct.h"
#include "rosidl_typesupport_cpp/action_type_support.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_cpp/service_type_support.hpp"

namespace ros_bt_py_interfaces
{

namespace action
{

namespace rosidl_typesupport_cpp
{

static rosidl_action_type_support_t FindBestExecutor_action_type_support_handle = {
  NULL, NULL, NULL, NULL, NULL};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace ros_bt_py_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_action_type_support_t *
get_action_type_support_handle<ros_bt_py_interfaces::action::FindBestExecutor>()
{
  using ::ros_bt_py_interfaces::action::rosidl_typesupport_cpp::FindBestExecutor_action_type_support_handle;
  // Thread-safe by always writing the same values to the static struct
  FindBestExecutor_action_type_support_handle.goal_service_type_support = get_service_type_support_handle<::ros_bt_py_interfaces::action::FindBestExecutor::Impl::SendGoalService>();
  FindBestExecutor_action_type_support_handle.result_service_type_support = get_service_type_support_handle<::ros_bt_py_interfaces::action::FindBestExecutor::Impl::GetResultService>();
  FindBestExecutor_action_type_support_handle.cancel_service_type_support = get_service_type_support_handle<::ros_bt_py_interfaces::action::FindBestExecutor::Impl::CancelGoalService>();
  FindBestExecutor_action_type_support_handle.feedback_message_type_support = get_message_type_support_handle<::ros_bt_py_interfaces::action::FindBestExecutor::Impl::FeedbackMessage>();
  FindBestExecutor_action_type_support_handle.status_message_type_support = get_message_type_support_handle<::ros_bt_py_interfaces::action::FindBestExecutor::Impl::GoalStatusMessage>();
  return &FindBestExecutor_action_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp