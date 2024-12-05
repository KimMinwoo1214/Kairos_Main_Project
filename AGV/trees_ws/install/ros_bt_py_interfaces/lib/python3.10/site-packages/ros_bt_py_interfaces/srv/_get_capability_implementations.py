# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/GetCapabilityImplementations.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GetCapabilityImplementations_Request(type):
    """Metaclass of message 'GetCapabilityImplementations_Request'."""

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
                'ros_bt_py_interfaces.srv.GetCapabilityImplementations_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_capability_implementations__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_capability_implementations__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_capability_implementations__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_capability_implementations__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_capability_implementations__request

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


class GetCapabilityImplementations_Request(metaclass=Metaclass_GetCapabilityImplementations_Request):
    """Message class 'GetCapabilityImplementations_Request'."""

    __slots__ = [
        '_interface',
    ]

    _fields_and_field_types = {
        'interface': 'ros_bt_py_interfaces/CapabilityInterface',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'CapabilityInterface'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from ros_bt_py_interfaces.msg import CapabilityInterface
        self.interface = kwargs.get('interface', CapabilityInterface())

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
        if self.interface != other.interface:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def interface(self):
        """Message field 'interface'."""
        return self._interface

    @interface.setter
    def interface(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import CapabilityInterface
            assert \
                isinstance(value, CapabilityInterface), \
                "The 'interface' field must be a sub message of type 'CapabilityInterface'"
        self._interface = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_GetCapabilityImplementations_Response(type):
    """Metaclass of message 'GetCapabilityImplementations_Response'."""

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
                'ros_bt_py_interfaces.srv.GetCapabilityImplementations_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_capability_implementations__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_capability_implementations__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_capability_implementations__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_capability_implementations__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_capability_implementations__response

            from ros_bt_py_interfaces.msg import CapabilityImplementation
            if CapabilityImplementation.__class__._TYPE_SUPPORT is None:
                CapabilityImplementation.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetCapabilityImplementations_Response(metaclass=Metaclass_GetCapabilityImplementations_Response):
    """Message class 'GetCapabilityImplementations_Response'."""

    __slots__ = [
        '_implementations',
        '_success',
        '_error_message',
    ]

    _fields_and_field_types = {
        'implementations': 'sequence<ros_bt_py_interfaces/CapabilityImplementation>',
        'success': 'boolean',
        'error_message': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'CapabilityImplementation')),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.implementations = kwargs.get('implementations', [])
        self.success = kwargs.get('success', bool())
        self.error_message = kwargs.get('error_message', str())

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
        if self.implementations != other.implementations:
            return False
        if self.success != other.success:
            return False
        if self.error_message != other.error_message:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def implementations(self):
        """Message field 'implementations'."""
        return self._implementations

    @implementations.setter
    def implementations(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import CapabilityImplementation
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, CapabilityImplementation) for v in value) and
                 True), \
                "The 'implementations' field must be a set or sequence and each value of type 'CapabilityImplementation'"
        self._implementations = value

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


class Metaclass_GetCapabilityImplementations(type):
    """Metaclass of service 'GetCapabilityImplementations'."""

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
                'ros_bt_py_interfaces.srv.GetCapabilityImplementations')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__get_capability_implementations

            from ros_bt_py_interfaces.srv import _get_capability_implementations
            if _get_capability_implementations.Metaclass_GetCapabilityImplementations_Request._TYPE_SUPPORT is None:
                _get_capability_implementations.Metaclass_GetCapabilityImplementations_Request.__import_type_support__()
            if _get_capability_implementations.Metaclass_GetCapabilityImplementations_Response._TYPE_SUPPORT is None:
                _get_capability_implementations.Metaclass_GetCapabilityImplementations_Response.__import_type_support__()


class GetCapabilityImplementations(metaclass=Metaclass_GetCapabilityImplementations):
    from ros_bt_py_interfaces.srv._get_capability_implementations import GetCapabilityImplementations_Request as Request
    from ros_bt_py_interfaces.srv._get_capability_implementations import GetCapabilityImplementations_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
