# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/RequestCapabilityExecution.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RequestCapabilityExecution_Request(type):
    """Metaclass of message 'RequestCapabilityExecution_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ros_bt_py_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ros_bt_py_interfaces.srv.RequestCapabilityExecution_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__request_capability_execution__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__request_capability_execution__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__request_capability_execution__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__request_capability_execution__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__request_capability_execution__request

            from ros_bt_py_interfaces.msg import CapabilityInterface
            if CapabilityInterface.__class__._TYPE_SUPPORT is None:
                CapabilityInterface.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RequestCapabilityExecution_Request(metaclass=Metaclass_RequestCapabilityExecution_Request):
    """Message class 'RequestCapabilityExecution_Request'."""

    __slots__ = [
        '_capability',
        '_node_id',
        '_require_local_execution',
        '_implementation_tags_dict',
    ]

    _fields_and_field_types = {
        'capability': 'ros_bt_py_interfaces/CapabilityInterface',
        'node_id': 'string',
        'require_local_execution': 'boolean',
        'implementation_tags_dict': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'CapabilityInterface'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from ros_bt_py_interfaces.msg import CapabilityInterface
        self.capability = kwargs.get('capability', CapabilityInterface())
        self.node_id = kwargs.get('node_id', str())
        self.require_local_execution = kwargs.get('require_local_execution', bool())
        self.implementation_tags_dict = kwargs.get('implementation_tags_dict', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.capability != other.capability:
            return False
        if self.node_id != other.node_id:
            return False
        if self.require_local_execution != other.require_local_execution:
            return False
        if self.implementation_tags_dict != other.implementation_tags_dict:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def capability(self):
        """Message field 'capability'."""
        return self._capability

    @capability.setter
    def capability(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import CapabilityInterface
            assert \
                isinstance(value, CapabilityInterface), \
                "The 'capability' field must be a sub message of type 'CapabilityInterface'"
        self._capability = value

    @builtins.property
    def node_id(self):
        """Message field 'node_id'."""
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'node_id' field must be of type 'str'"
        self._node_id = value

    @builtins.property
    def require_local_execution(self):
        """Message field 'require_local_execution'."""
        return self._require_local_execution

    @require_local_execution.setter
    def require_local_execution(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'require_local_execution' field must be of type 'bool'"
        self._require_local_execution = value

    @builtins.property
    def implementation_tags_dict(self):
        """Message field 'implementation_tags_dict'."""
        return self._implementation_tags_dict

    @implementation_tags_dict.setter
    def implementation_tags_dict(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'implementation_tags_dict' field must be of type 'str'"
        self._implementation_tags_dict = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_RequestCapabilityExecution_Response(type):
    """Metaclass of message 'RequestCapabilityExecution_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ros_bt_py_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ros_bt_py_interfaces.srv.RequestCapabilityExecution_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__request_capability_execution__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__request_capability_execution__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__request_capability_execution__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__request_capability_execution__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__request_capability_execution__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RequestCapabilityExecution_Response(metaclass=Metaclass_RequestCapabilityExecution_Response):
    """Message class 'RequestCapabilityExecution_Response'."""

    __slots__ = [
        '_success',
        '_error_message',
        '_execute_local',
        '_implementation_name',
        '_remote_mission_controller_topic',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'error_message': 'string',
        'execute_local': 'boolean',
        'implementation_name': 'string',
        'remote_mission_controller_topic': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())
        self.error_message = kwargs.get('error_message', str())
        self.execute_local = kwargs.get('execute_local', bool())
        self.implementation_name = kwargs.get('implementation_name', str())
        self.remote_mission_controller_topic = kwargs.get('remote_mission_controller_topic', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.success != other.success:
            return False
        if self.error_message != other.error_message:
            return False
        if self.execute_local != other.execute_local:
            return False
        if self.implementation_name != other.implementation_name:
            return False
        if self.remote_mission_controller_topic != other.remote_mission_controller_topic:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value

    @builtins.property
    def error_message(self):
        """Message field 'error_message'."""
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'error_message' field must be of type 'str'"
        self._error_message = value

    @builtins.property
    def execute_local(self):
        """Message field 'execute_local'."""
        return self._execute_local

    @execute_local.setter
    def execute_local(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'execute_local' field must be of type 'bool'"
        self._execute_local = value

    @builtins.property
    def implementation_name(self):
        """Message field 'implementation_name'."""
        return self._implementation_name

    @implementation_name.setter
    def implementation_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'implementation_name' field must be of type 'str'"
        self._implementation_name = value

    @builtins.property
    def remote_mission_controller_topic(self):
        """Message field 'remote_mission_controller_topic'."""
        return self._remote_mission_controller_topic

    @remote_mission_controller_topic.setter
    def remote_mission_controller_topic(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'remote_mission_controller_topic' field must be of type 'str'"
        self._remote_mission_controller_topic = value


class Metaclass_RequestCapabilityExecution(type):
    """Metaclass of service 'RequestCapabilityExecution'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ros_bt_py_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ros_bt_py_interfaces.srv.RequestCapabilityExecution')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__request_capability_execution

            from ros_bt_py_interfaces.srv import _request_capability_execution
            if _request_capability_execution.Metaclass_RequestCapabilityExecution_Request._TYPE_SUPPORT is None:
                _request_capability_execution.Metaclass_RequestCapabilityExecution_Request.__import_type_support__()
            if _request_capability_execution.Metaclass_RequestCapabilityExecution_Response._TYPE_SUPPORT is None:
                _request_capability_execution.Metaclass_RequestCapabilityExecution_Response.__import_type_support__()


class RequestCapabilityExecution(metaclass=Metaclass_RequestCapabilityExecution):
    from ros_bt_py_interfaces.srv._request_capability_execution import RequestCapabilityExecution_Request as Request
    from ros_bt_py_interfaces.srv._request_capability_execution import RequestCapabilityExecution_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
