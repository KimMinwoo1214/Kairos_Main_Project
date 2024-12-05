# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/SetSimulateTick.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SetSimulateTick_Request(type):
    """Metaclass of message 'SetSimulateTick_Request'."""

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
                'ros_bt_py_interfaces.srv.SetSimulateTick_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_simulate_tick__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_simulate_tick__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_simulate_tick__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_simulate_tick__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_simulate_tick__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetSimulateTick_Request(metaclass=Metaclass_SetSimulateTick_Request):
    """Message class 'SetSimulateTick_Request'."""

    __slots__ = [
        '_simulate_tick',
        '_succeed_always',
    ]

    _fields_and_field_types = {
        'simulate_tick': 'boolean',
        'succeed_always': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.simulate_tick = kwargs.get('simulate_tick', bool())
        self.succeed_always = kwargs.get('succeed_always', bool())

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
        if self.simulate_tick != other.simulate_tick:
            return False
        if self.succeed_always != other.succeed_always:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def simulate_tick(self):
        """Message field 'simulate_tick'."""
        return self._simulate_tick

    @simulate_tick.setter
    def simulate_tick(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'simulate_tick' field must be of type 'bool'"
        self._simulate_tick = value

    @builtins.property
    def succeed_always(self):
        """Message field 'succeed_always'."""
        return self._succeed_always

    @succeed_always.setter
    def succeed_always(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'succeed_always' field must be of type 'bool'"
        self._succeed_always = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_SetSimulateTick_Response(type):
    """Metaclass of message 'SetSimulateTick_Response'."""

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
                'ros_bt_py_interfaces.srv.SetSimulateTick_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_simulate_tick__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_simulate_tick__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_simulate_tick__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_simulate_tick__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_simulate_tick__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetSimulateTick_Response(metaclass=Metaclass_SetSimulateTick_Response):
    """Message class 'SetSimulateTick_Response'."""

    __slots__ = [
        '_success',
        '_error_message',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'error_message': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
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


class Metaclass_SetSimulateTick(type):
    """Metaclass of service 'SetSimulateTick'."""

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
                'ros_bt_py_interfaces.srv.SetSimulateTick')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__set_simulate_tick

            from ros_bt_py_interfaces.srv import _set_simulate_tick
            if _set_simulate_tick.Metaclass_SetSimulateTick_Request._TYPE_SUPPORT is None:
                _set_simulate_tick.Metaclass_SetSimulateTick_Request.__import_type_support__()
            if _set_simulate_tick.Metaclass_SetSimulateTick_Response._TYPE_SUPPORT is None:
                _set_simulate_tick.Metaclass_SetSimulateTick_Response.__import_type_support__()


class SetSimulateTick(metaclass=Metaclass_SetSimulateTick):
    from ros_bt_py_interfaces.srv._set_simulate_tick import SetSimulateTick_Request as Request
    from ros_bt_py_interfaces.srv._set_simulate_tick import SetSimulateTick_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
