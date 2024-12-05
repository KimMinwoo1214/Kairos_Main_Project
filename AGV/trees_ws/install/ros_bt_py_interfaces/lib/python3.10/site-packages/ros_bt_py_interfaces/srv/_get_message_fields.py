# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/GetMessageFields.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GetMessageFields_Request(type):
    """Metaclass of message 'GetMessageFields_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'MESSAGE': 0,
        'REQUEST': 1,
        'RESPONSE': 2,
        'GOAL': 3,
        'FEEDBACK': 4,
        'RESULT': 5,
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
                'ros_bt_py_interfaces.srv.GetMessageFields_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_message_fields__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_message_fields__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_message_fields__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_message_fields__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_message_fields__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'MESSAGE': cls.__constants['MESSAGE'],
            'REQUEST': cls.__constants['REQUEST'],
            'RESPONSE': cls.__constants['RESPONSE'],
            'GOAL': cls.__constants['GOAL'],
            'FEEDBACK': cls.__constants['FEEDBACK'],
            'RESULT': cls.__constants['RESULT'],
        }

    @property
    def MESSAGE(self):
        """Message constant 'MESSAGE'."""
        return Metaclass_GetMessageFields_Request.__constants['MESSAGE']

    @property
    def REQUEST(self):
        """Message constant 'REQUEST'."""
        return Metaclass_GetMessageFields_Request.__constants['REQUEST']

    @property
    def RESPONSE(self):
        """Message constant 'RESPONSE'."""
        return Metaclass_GetMessageFields_Request.__constants['RESPONSE']

    @property
    def GOAL(self):
        """Message constant 'GOAL'."""
        return Metaclass_GetMessageFields_Request.__constants['GOAL']

    @property
    def FEEDBACK(self):
        """Message constant 'FEEDBACK'."""
        return Metaclass_GetMessageFields_Request.__constants['FEEDBACK']

    @property
    def RESULT(self):
        """Message constant 'RESULT'."""
        return Metaclass_GetMessageFields_Request.__constants['RESULT']


class GetMessageFields_Request(metaclass=Metaclass_GetMessageFields_Request):
    """
    Message class 'GetMessageFields_Request'.

    Constants:
      MESSAGE
      REQUEST
      RESPONSE
      GOAL
      FEEDBACK
      RESULT
    """

    __slots__ = [
        '_message_type',
        '_service',
        '_action',
        '_type',
    ]

    _fields_and_field_types = {
        'message_type': 'string',
        'service': 'boolean',
        'action': 'boolean',
        'type': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.message_type = kwargs.get('message_type', str())
        self.service = kwargs.get('service', bool())
        self.action = kwargs.get('action', bool())
        self.type = kwargs.get('type', int())

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
        if self.message_type != other.message_type:
            return False
        if self.service != other.service:
            return False
        if self.action != other.action:
            return False
        if self.type != other.type:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def message_type(self):
        """Message field 'message_type'."""
        return self._message_type

    @message_type.setter
    def message_type(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'message_type' field must be of type 'str'"
        self._message_type = value

    @builtins.property
    def service(self):
        """Message field 'service'."""
        return self._service

    @service.setter
    def service(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'service' field must be of type 'bool'"
        self._service = value

    @builtins.property
    def action(self):
        """Message field 'action'."""
        return self._action

    @action.setter
    def action(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'action' field must be of type 'bool'"
        self._action = value

    @builtins.property  # noqa: A003
    def type(self):  # noqa: A003
        """Message field 'type'."""
        return self._type

    @type.setter  # noqa: A003
    def type(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'type' field must be an unsigned integer in [0, 255]"
        self._type = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_GetMessageFields_Response(type):
    """Metaclass of message 'GetMessageFields_Response'."""

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
                'ros_bt_py_interfaces.srv.GetMessageFields_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_message_fields__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_message_fields__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_message_fields__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_message_fields__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_message_fields__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetMessageFields_Response(metaclass=Metaclass_GetMessageFields_Response):
    """Message class 'GetMessageFields_Response'."""

    __slots__ = [
        '_fields',
        '_field_names',
        '_success',
        '_error_message',
    ]

    _fields_and_field_types = {
        'fields': 'string',
        'field_names': 'sequence<string>',
        'success': 'boolean',
        'error_message': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.fields = kwargs.get('fields', str())
        self.field_names = kwargs.get('field_names', [])
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
        if self.fields != other.fields:
            return False
        if self.field_names != other.field_names:
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
    def fields(self):
        """Message field 'fields'."""
        return self._fields

    @fields.setter
    def fields(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'fields' field must be of type 'str'"
        self._fields = value

    @builtins.property
    def field_names(self):
        """Message field 'field_names'."""
        return self._field_names

    @field_names.setter
    def field_names(self, value):
        if __debug__:
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
                 all(isinstance(v, str) for v in value) and
                 True), \
                "The 'field_names' field must be a set or sequence and each value of type 'str'"
        self._field_names = value

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


class Metaclass_GetMessageFields(type):
    """Metaclass of service 'GetMessageFields'."""

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
                'ros_bt_py_interfaces.srv.GetMessageFields')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__get_message_fields

            from ros_bt_py_interfaces.srv import _get_message_fields
            if _get_message_fields.Metaclass_GetMessageFields_Request._TYPE_SUPPORT is None:
                _get_message_fields.Metaclass_GetMessageFields_Request.__import_type_support__()
            if _get_message_fields.Metaclass_GetMessageFields_Response._TYPE_SUPPORT is None:
                _get_message_fields.Metaclass_GetMessageFields_Response.__import_type_support__()


class GetMessageFields(metaclass=Metaclass_GetMessageFields):
    from ros_bt_py_interfaces.srv._get_message_fields import GetMessageFields_Request as Request
    from ros_bt_py_interfaces.srv._get_message_fields import GetMessageFields_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
