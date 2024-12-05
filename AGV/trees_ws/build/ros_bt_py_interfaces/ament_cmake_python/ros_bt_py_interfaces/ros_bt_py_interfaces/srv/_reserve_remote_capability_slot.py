# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/ReserveRemoteCapabilitySlot.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ReserveRemoteCapabilitySlot_Request(type):
    """Metaclass of message 'ReserveRemoteCapabilitySlot_Request'."""

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
                'ros_bt_py_interfaces.srv.ReserveRemoteCapabilitySlot_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__reserve_remote_capability_slot__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__reserve_remote_capability_slot__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__reserve_remote_capability_slot__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__reserve_remote_capability_slot__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__reserve_remote_capability_slot__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ReserveRemoteCapabilitySlot_Request(metaclass=Metaclass_ReserveRemoteCapabilitySlot_Request):
    """Message class 'ReserveRemoteCapabilitySlot_Request'."""

    __slots__ = [
        '_remote_mission_control',
        '_implementation_name',
        '_reauction_threshold',
    ]

    _fields_and_field_types = {
        'remote_mission_control': 'string',
        'implementation_name': 'string',
        'reauction_threshold': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.remote_mission_control = kwargs.get('remote_mission_control', str())
        self.implementation_name = kwargs.get('implementation_name', str())
        self.reauction_threshold = kwargs.get('reauction_threshold', float())

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
        if self.remote_mission_control != other.remote_mission_control:
            return False
        if self.implementation_name != other.implementation_name:
            return False
        if self.reauction_threshold != other.reauction_threshold:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def remote_mission_control(self):
        """Message field 'remote_mission_control'."""
        return self._remote_mission_control

    @remote_mission_control.setter
    def remote_mission_control(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'remote_mission_control' field must be of type 'str'"
        self._remote_mission_control = value

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
    def reauction_threshold(self):
        """Message field 'reauction_threshold'."""
        return self._reauction_threshold

    @reauction_threshold.setter
    def reauction_threshold(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'reauction_threshold' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'reauction_threshold' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._reauction_threshold = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ReserveRemoteCapabilitySlot_Response(type):
    """Metaclass of message 'ReserveRemoteCapabilitySlot_Response'."""

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
                'ros_bt_py_interfaces.srv.ReserveRemoteCapabilitySlot_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__reserve_remote_capability_slot__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__reserve_remote_capability_slot__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__reserve_remote_capability_slot__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__reserve_remote_capability_slot__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__reserve_remote_capability_slot__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ReserveRemoteCapabilitySlot_Response(metaclass=Metaclass_ReserveRemoteCapabilitySlot_Response):
    """Message class 'ReserveRemoteCapabilitySlot_Response'."""

    __slots__ = [
        '_success',
        '_error',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'error': 'string',
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
        self.error = kwargs.get('error', str())

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
        if self.error != other.error:
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
    def error(self):
        """Message field 'error'."""
        return self._error

    @error.setter
    def error(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'error' field must be of type 'str'"
        self._error = value


class Metaclass_ReserveRemoteCapabilitySlot(type):
    """Metaclass of service 'ReserveRemoteCapabilitySlot'."""

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
                'ros_bt_py_interfaces.srv.ReserveRemoteCapabilitySlot')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__reserve_remote_capability_slot

            from ros_bt_py_interfaces.srv import _reserve_remote_capability_slot
            if _reserve_remote_capability_slot.Metaclass_ReserveRemoteCapabilitySlot_Request._TYPE_SUPPORT is None:
                _reserve_remote_capability_slot.Metaclass_ReserveRemoteCapabilitySlot_Request.__import_type_support__()
            if _reserve_remote_capability_slot.Metaclass_ReserveRemoteCapabilitySlot_Response._TYPE_SUPPORT is None:
                _reserve_remote_capability_slot.Metaclass_ReserveRemoteCapabilitySlot_Response.__import_type_support__()


class ReserveRemoteCapabilitySlot(metaclass=Metaclass_ReserveRemoteCapabilitySlot):
    from ros_bt_py_interfaces.srv._reserve_remote_capability_slot import ReserveRemoteCapabilitySlot_Request as Request
    from ros_bt_py_interfaces.srv._reserve_remote_capability_slot import ReserveRemoteCapabilitySlot_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
