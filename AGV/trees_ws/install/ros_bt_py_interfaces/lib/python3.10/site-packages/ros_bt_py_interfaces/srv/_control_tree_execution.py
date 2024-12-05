# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/ControlTreeExecution.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ControlTreeExecution_Request(type):
    """Metaclass of message 'ControlTreeExecution_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'DO_NOTHING': 0,
        'TICK_ONCE': 1,
        'TICK_PERIODICALLY': 2,
        'TICK_UNTIL_RESULT': 3,
        'STOP': 4,
        'RESET': 5,
        'SHUTDOWN': 6,
        'SETUP_AND_SHUTDOWN': 7,
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
                'ros_bt_py_interfaces.srv.ControlTreeExecution_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__control_tree_execution__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__control_tree_execution__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__control_tree_execution__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__control_tree_execution__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__control_tree_execution__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'DO_NOTHING': cls.__constants['DO_NOTHING'],
            'TICK_ONCE': cls.__constants['TICK_ONCE'],
            'TICK_PERIODICALLY': cls.__constants['TICK_PERIODICALLY'],
            'TICK_UNTIL_RESULT': cls.__constants['TICK_UNTIL_RESULT'],
            'STOP': cls.__constants['STOP'],
            'RESET': cls.__constants['RESET'],
            'SHUTDOWN': cls.__constants['SHUTDOWN'],
            'SETUP_AND_SHUTDOWN': cls.__constants['SETUP_AND_SHUTDOWN'],
        }

    @property
    def DO_NOTHING(self):
        """Message constant 'DO_NOTHING'."""
        return Metaclass_ControlTreeExecution_Request.__constants['DO_NOTHING']

    @property
    def TICK_ONCE(self):
        """Message constant 'TICK_ONCE'."""
        return Metaclass_ControlTreeExecution_Request.__constants['TICK_ONCE']

    @property
    def TICK_PERIODICALLY(self):
        """Message constant 'TICK_PERIODICALLY'."""
        return Metaclass_ControlTreeExecution_Request.__constants['TICK_PERIODICALLY']

    @property
    def TICK_UNTIL_RESULT(self):
        """Message constant 'TICK_UNTIL_RESULT'."""
        return Metaclass_ControlTreeExecution_Request.__constants['TICK_UNTIL_RESULT']

    @property
    def STOP(self):
        """Message constant 'STOP'."""
        return Metaclass_ControlTreeExecution_Request.__constants['STOP']

    @property
    def RESET(self):
        """Message constant 'RESET'."""
        return Metaclass_ControlTreeExecution_Request.__constants['RESET']

    @property
    def SHUTDOWN(self):
        """Message constant 'SHUTDOWN'."""
        return Metaclass_ControlTreeExecution_Request.__constants['SHUTDOWN']

    @property
    def SETUP_AND_SHUTDOWN(self):
        """Message constant 'SETUP_AND_SHUTDOWN'."""
        return Metaclass_ControlTreeExecution_Request.__constants['SETUP_AND_SHUTDOWN']


class ControlTreeExecution_Request(metaclass=Metaclass_ControlTreeExecution_Request):
    """
    Message class 'ControlTreeExecution_Request'.

    Constants:
      DO_NOTHING
      TICK_ONCE
      TICK_PERIODICALLY
      TICK_UNTIL_RESULT
      STOP
      RESET
      SHUTDOWN
      SETUP_AND_SHUTDOWN
    """

    __slots__ = [
        '_command',
        '_tick_frequency_hz',
    ]

    _fields_and_field_types = {
        'command': 'uint8',
        'tick_frequency_hz': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.command = kwargs.get('command', int())
        self.tick_frequency_hz = kwargs.get('tick_frequency_hz', float())

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
        if self.command != other.command:
            return False
        if self.tick_frequency_hz != other.tick_frequency_hz:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def command(self):
        """Message field 'command'."""
        return self._command

    @command.setter
    def command(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'command' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'command' field must be an unsigned integer in [0, 255]"
        self._command = value

    @builtins.property
    def tick_frequency_hz(self):
        """Message field 'tick_frequency_hz'."""
        return self._tick_frequency_hz

    @tick_frequency_hz.setter
    def tick_frequency_hz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'tick_frequency_hz' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'tick_frequency_hz' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._tick_frequency_hz = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ControlTreeExecution_Response(type):
    """Metaclass of message 'ControlTreeExecution_Response'."""

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
                'ros_bt_py_interfaces.srv.ControlTreeExecution_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__control_tree_execution__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__control_tree_execution__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__control_tree_execution__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__control_tree_execution__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__control_tree_execution__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ControlTreeExecution_Response(metaclass=Metaclass_ControlTreeExecution_Response):
    """Message class 'ControlTreeExecution_Response'."""

    __slots__ = [
        '_success',
        '_error_message',
        '_tree_state',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'error_message': 'string',
        'tree_state': 'string',
    }

    SLOT_TYPES = (
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
        self.tree_state = kwargs.get('tree_state', str())

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
        if self.tree_state != other.tree_state:
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
    def tree_state(self):
        """Message field 'tree_state'."""
        return self._tree_state

    @tree_state.setter
    def tree_state(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'tree_state' field must be of type 'str'"
        self._tree_state = value


class Metaclass_ControlTreeExecution(type):
    """Metaclass of service 'ControlTreeExecution'."""

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
                'ros_bt_py_interfaces.srv.ControlTreeExecution')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__control_tree_execution

            from ros_bt_py_interfaces.srv import _control_tree_execution
            if _control_tree_execution.Metaclass_ControlTreeExecution_Request._TYPE_SUPPORT is None:
                _control_tree_execution.Metaclass_ControlTreeExecution_Request.__import_type_support__()
            if _control_tree_execution.Metaclass_ControlTreeExecution_Response._TYPE_SUPPORT is None:
                _control_tree_execution.Metaclass_ControlTreeExecution_Response.__import_type_support__()


class ControlTreeExecution(metaclass=Metaclass_ControlTreeExecution):
    from ros_bt_py_interfaces.srv._control_tree_execution import ControlTreeExecution_Request as Request
    from ros_bt_py_interfaces.srv._control_tree_execution import ControlTreeExecution_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
