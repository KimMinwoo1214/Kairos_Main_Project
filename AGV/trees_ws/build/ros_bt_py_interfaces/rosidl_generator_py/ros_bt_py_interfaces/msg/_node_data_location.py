# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:msg/NodeDataLocation.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_NodeDataLocation(type):
    """Metaclass of message 'NodeDataLocation'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'INPUT_DATA': 'inputs',
        'OUTPUT_DATA': 'outputs',
        'OPTION_DATA': 'options',
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
                'ros_bt_py_interfaces.msg.NodeDataLocation')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__node_data_location
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__node_data_location
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__node_data_location
            cls._TYPE_SUPPORT = module.type_support_msg__msg__node_data_location
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__node_data_location

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'INPUT_DATA': cls.__constants['INPUT_DATA'],
            'OUTPUT_DATA': cls.__constants['OUTPUT_DATA'],
            'OPTION_DATA': cls.__constants['OPTION_DATA'],
        }

    @property
    def INPUT_DATA(self):
        """Message constant 'INPUT_DATA'."""
        return Metaclass_NodeDataLocation.__constants['INPUT_DATA']

    @property
    def OUTPUT_DATA(self):
        """Message constant 'OUTPUT_DATA'."""
        return Metaclass_NodeDataLocation.__constants['OUTPUT_DATA']

    @property
    def OPTION_DATA(self):
        """Message constant 'OPTION_DATA'."""
        return Metaclass_NodeDataLocation.__constants['OPTION_DATA']


class NodeDataLocation(metaclass=Metaclass_NodeDataLocation):
    """
    Message class 'NodeDataLocation'.

    Constants:
      INPUT_DATA
      OUTPUT_DATA
      OPTION_DATA
    """

    __slots__ = [
        '_node_name',
        '_data_kind',
        '_data_key',
    ]

    _fields_and_field_types = {
        'node_name': 'string',
        'data_kind': 'string',
        'data_key': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.node_name = kwargs.get('node_name', str())
        self.data_kind = kwargs.get('data_kind', str())
        self.data_key = kwargs.get('data_key', str())

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
        if self.node_name != other.node_name:
            return False
        if self.data_kind != other.data_kind:
            return False
        if self.data_key != other.data_key:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

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
    def data_kind(self):
        """Message field 'data_kind'."""
        return self._data_kind

    @data_kind.setter
    def data_kind(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'data_kind' field must be of type 'str'"
        self._data_kind = value

    @builtins.property
    def data_key(self):
        """Message field 'data_key'."""
        return self._data_key

    @data_key.setter
    def data_key(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'data_key' field must be of type 'str'"
        self._data_key = value
