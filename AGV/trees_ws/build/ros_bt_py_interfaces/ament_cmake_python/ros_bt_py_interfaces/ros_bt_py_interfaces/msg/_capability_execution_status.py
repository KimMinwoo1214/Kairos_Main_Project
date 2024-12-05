# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:msg/CapabilityExecutionStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CapabilityExecutionStatus(type):
    """Metaclass of message 'CapabilityExecutionStatus'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'IDLE': 'IDLE',
        'SETUP': 'SETUP',
        'EXECUTING': 'EXECUTING',
        'FAILED': 'FAILED',
        'SUCCEEDED': 'SUCCEEDED',
        'SHUTDOWN': 'SHUTDOWN',
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
                'ros_bt_py_interfaces.msg.CapabilityExecutionStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__capability_execution_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__capability_execution_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__capability_execution_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__capability_execution_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__capability_execution_status

            from ros_bt_py_interfaces.msg import CapabilityInterface
            if CapabilityInterface.__class__._TYPE_SUPPORT is None:
                CapabilityInterface.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'IDLE': cls.__constants['IDLE'],
            'SETUP': cls.__constants['SETUP'],
            'EXECUTING': cls.__constants['EXECUTING'],
            'FAILED': cls.__constants['FAILED'],
            'SUCCEEDED': cls.__constants['SUCCEEDED'],
            'SHUTDOWN': cls.__constants['SHUTDOWN'],
        }

    @property
    def IDLE(self):
        """Message constant 'IDLE'."""
        return Metaclass_CapabilityExecutionStatus.__constants['IDLE']

    @property
    def SETUP(self):
        """Message constant 'SETUP'."""
        return Metaclass_CapabilityExecutionStatus.__constants['SETUP']

    @property
    def EXECUTING(self):
        """Message constant 'EXECUTING'."""
        return Metaclass_CapabilityExecutionStatus.__constants['EXECUTING']

    @property
    def FAILED(self):
        """Message constant 'FAILED'."""
        return Metaclass_CapabilityExecutionStatus.__constants['FAILED']

    @property
    def SUCCEEDED(self):
        """Message constant 'SUCCEEDED'."""
        return Metaclass_CapabilityExecutionStatus.__constants['SUCCEEDED']

    @property
    def SHUTDOWN(self):
        """Message constant 'SHUTDOWN'."""
        return Metaclass_CapabilityExecutionStatus.__constants['SHUTDOWN']


class CapabilityExecutionStatus(metaclass=Metaclass_CapabilityExecutionStatus):
    """
    Message class 'CapabilityExecutionStatus'.

    Constants:
      IDLE
      SETUP
      EXECUTING
      FAILED
      SUCCEEDED
      SHUTDOWN
    """

    __slots__ = [
        '_interface',
        '_node_name',
        '_status',
    ]

    _fields_and_field_types = {
        'interface': 'ros_bt_py_interfaces/CapabilityInterface',
        'node_name': 'string',
        'status': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'CapabilityInterface'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from ros_bt_py_interfaces.msg import CapabilityInterface
        self.interface = kwargs.get('interface', CapabilityInterface())
        self.node_name = kwargs.get('node_name', str())
        self.status = kwargs.get('status', str())

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
        if self.node_name != other.node_name:
            return False
        if self.status != other.status:
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

    @builtins.property
    def node_name(self):
        """Message field 'node_name'."""
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'node_name' field must be of type 'str'"
        self._node_name = value

    @builtins.property
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'status' field must be of type 'str'"
        self._status = value
