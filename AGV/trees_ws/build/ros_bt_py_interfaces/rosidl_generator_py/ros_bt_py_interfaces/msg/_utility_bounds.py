# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:msg/UtilityBounds.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_UtilityBounds(type):
    """Metaclass of message 'UtilityBounds'."""

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
                'ros_bt_py_interfaces.msg.UtilityBounds')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__utility_bounds
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__utility_bounds
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__utility_bounds
            cls._TYPE_SUPPORT = module.type_support_msg__msg__utility_bounds
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__utility_bounds

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class UtilityBounds(metaclass=Metaclass_UtilityBounds):
    """Message class 'UtilityBounds'."""

    __slots__ = [
        '_can_execute',
        '_has_upper_bound_success',
        '_upper_bound_success',
        '_has_lower_bound_success',
        '_lower_bound_success',
        '_has_upper_bound_failure',
        '_upper_bound_failure',
        '_has_lower_bound_failure',
        '_lower_bound_failure',
    ]

    _fields_and_field_types = {
        'can_execute': 'boolean',
        'has_upper_bound_success': 'boolean',
        'upper_bound_success': 'double',
        'has_lower_bound_success': 'boolean',
        'lower_bound_success': 'double',
        'has_upper_bound_failure': 'boolean',
        'upper_bound_failure': 'double',
        'has_lower_bound_failure': 'boolean',
        'lower_bound_failure': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.can_execute = kwargs.get('can_execute', bool())
        self.has_upper_bound_success = kwargs.get('has_upper_bound_success', bool())
        self.upper_bound_success = kwargs.get('upper_bound_success', float())
        self.has_lower_bound_success = kwargs.get('has_lower_bound_success', bool())
        self.lower_bound_success = kwargs.get('lower_bound_success', float())
        self.has_upper_bound_failure = kwargs.get('has_upper_bound_failure', bool())
        self.upper_bound_failure = kwargs.get('upper_bound_failure', float())
        self.has_lower_bound_failure = kwargs.get('has_lower_bound_failure', bool())
        self.lower_bound_failure = kwargs.get('lower_bound_failure', float())

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
        if self.can_execute != other.can_execute:
            return False
        if self.has_upper_bound_success != other.has_upper_bound_success:
            return False
        if self.upper_bound_success != other.upper_bound_success:
            return False
        if self.has_lower_bound_success != other.has_lower_bound_success:
            return False
        if self.lower_bound_success != other.lower_bound_success:
            return False
        if self.has_upper_bound_failure != other.has_upper_bound_failure:
            return False
        if self.upper_bound_failure != other.upper_bound_failure:
            return False
        if self.has_lower_bound_failure != other.has_lower_bound_failure:
            return False
        if self.lower_bound_failure != other.lower_bound_failure:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def can_execute(self):
        """Message field 'can_execute'."""
        return self._can_execute

    @can_execute.setter
    def can_execute(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'can_execute' field must be of type 'bool'"
        self._can_execute = value

    @builtins.property
    def has_upper_bound_success(self):
        """Message field 'has_upper_bound_success'."""
        return self._has_upper_bound_success

    @has_upper_bound_success.setter
    def has_upper_bound_success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'has_upper_bound_success' field must be of type 'bool'"
        self._has_upper_bound_success = value

    @builtins.property
    def upper_bound_success(self):
        """Message field 'upper_bound_success'."""
        return self._upper_bound_success

    @upper_bound_success.setter
    def upper_bound_success(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'upper_bound_success' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'upper_bound_success' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._upper_bound_success = value

    @builtins.property
    def has_lower_bound_success(self):
        """Message field 'has_lower_bound_success'."""
        return self._has_lower_bound_success

    @has_lower_bound_success.setter
    def has_lower_bound_success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'has_lower_bound_success' field must be of type 'bool'"
        self._has_lower_bound_success = value

    @builtins.property
    def lower_bound_success(self):
        """Message field 'lower_bound_success'."""
        return self._lower_bound_success

    @lower_bound_success.setter
    def lower_bound_success(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lower_bound_success' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'lower_bound_success' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._lower_bound_success = value

    @builtins.property
    def has_upper_bound_failure(self):
        """Message field 'has_upper_bound_failure'."""
        return self._has_upper_bound_failure

    @has_upper_bound_failure.setter
    def has_upper_bound_failure(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'has_upper_bound_failure' field must be of type 'bool'"
        self._has_upper_bound_failure = value

    @builtins.property
    def upper_bound_failure(self):
        """Message field 'upper_bound_failure'."""
        return self._upper_bound_failure

    @upper_bound_failure.setter
    def upper_bound_failure(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'upper_bound_failure' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'upper_bound_failure' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._upper_bound_failure = value

    @builtins.property
    def has_lower_bound_failure(self):
        """Message field 'has_lower_bound_failure'."""
        return self._has_lower_bound_failure

    @has_lower_bound_failure.setter
    def has_lower_bound_failure(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'has_lower_bound_failure' field must be of type 'bool'"
        self._has_lower_bound_failure = value

    @builtins.property
    def lower_bound_failure(self):
        """Message field 'lower_bound_failure'."""
        return self._lower_bound_failure

    @lower_bound_failure.setter
    def lower_bound_failure(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lower_bound_failure' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'lower_bound_failure' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._lower_bound_failure = value
