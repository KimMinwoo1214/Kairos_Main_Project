# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:msg/Tree.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Tree(type):
    """Metaclass of message 'Tree'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'IDLE': 'IDLE',
        'EDITABLE': 'EDITABLE',
        'TICKING': 'TICKING',
        'WAITING_FOR_TICK': 'WAITING_FOR_TICK',
        'STOP_REQUESTED': 'STOP_REQUESTED',
        'ERROR': 'ERROR',
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
                'ros_bt_py_interfaces.msg.Tree')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__tree
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__tree
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__tree
            cls._TYPE_SUPPORT = module.type_support_msg__msg__tree
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__tree

            from ros_bt_py_interfaces.msg import Node
            if Node.__class__._TYPE_SUPPORT is None:
                Node.__class__.__import_type_support__()

            from ros_bt_py_interfaces.msg import NodeDataLocation
            if NodeDataLocation.__class__._TYPE_SUPPORT is None:
                NodeDataLocation.__class__.__import_type_support__()

            from ros_bt_py_interfaces.msg import NodeDataWiring
            if NodeDataWiring.__class__._TYPE_SUPPORT is None:
                NodeDataWiring.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'IDLE': cls.__constants['IDLE'],
            'EDITABLE': cls.__constants['EDITABLE'],
            'TICKING': cls.__constants['TICKING'],
            'WAITING_FOR_TICK': cls.__constants['WAITING_FOR_TICK'],
            'STOP_REQUESTED': cls.__constants['STOP_REQUESTED'],
            'ERROR': cls.__constants['ERROR'],
        }

    @property
    def IDLE(self):
        """Message constant 'IDLE'."""
        return Metaclass_Tree.__constants['IDLE']

    @property
    def EDITABLE(self):
        """Message constant 'EDITABLE'."""
        return Metaclass_Tree.__constants['EDITABLE']

    @property
    def TICKING(self):
        """Message constant 'TICKING'."""
        return Metaclass_Tree.__constants['TICKING']

    @property
    def WAITING_FOR_TICK(self):
        """Message constant 'WAITING_FOR_TICK'."""
        return Metaclass_Tree.__constants['WAITING_FOR_TICK']

    @property
    def STOP_REQUESTED(self):
        """Message constant 'STOP_REQUESTED'."""
        return Metaclass_Tree.__constants['STOP_REQUESTED']

    @property
    def ERROR(self):
        """Message constant 'ERROR'."""
        return Metaclass_Tree.__constants['ERROR']


class Tree(metaclass=Metaclass_Tree):
    """
    Message class 'Tree'.

    Constants:
      IDLE
      EDITABLE
      TICKING
      WAITING_FOR_TICK
      STOP_REQUESTED
      ERROR
    """

    __slots__ = [
        '_name',
        '_path',
        '_root_name',
        '_nodes',
        '_data_wirings',
        '_tick_frequency_hz',
        '_state',
        '_public_node_data',
    ]

    _fields_and_field_types = {
        'name': 'string',
        'path': 'string',
        'root_name': 'string',
        'nodes': 'sequence<ros_bt_py_interfaces/Node>',
        'data_wirings': 'sequence<ros_bt_py_interfaces/NodeDataWiring>',
        'tick_frequency_hz': 'double',
        'state': 'string',
        'public_node_data': 'sequence<ros_bt_py_interfaces/NodeDataLocation>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'Node')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'NodeDataWiring')),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'NodeDataLocation')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.name = kwargs.get('name', str())
        self.path = kwargs.get('path', str())
        self.root_name = kwargs.get('root_name', str())
        self.nodes = kwargs.get('nodes', [])
        self.data_wirings = kwargs.get('data_wirings', [])
        self.tick_frequency_hz = kwargs.get('tick_frequency_hz', float())
        self.state = kwargs.get('state', str())
        self.public_node_data = kwargs.get('public_node_data', [])

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
        if self.name != other.name:
            return False
        if self.path != other.path:
            return False
        if self.root_name != other.root_name:
            return False
        if self.nodes != other.nodes:
            return False
        if self.data_wirings != other.data_wirings:
            return False
        if self.tick_frequency_hz != other.tick_frequency_hz:
            return False
        if self.state != other.state:
            return False
        if self.public_node_data != other.public_node_data:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def name(self):
        """Message field 'name'."""
        return self._name

    @name.setter
    def name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'name' field must be of type 'str'"
        self._name = value

    @builtins.property
    def path(self):
        """Message field 'path'."""
        return self._path

    @path.setter
    def path(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'path' field must be of type 'str'"
        self._path = value

    @builtins.property
    def root_name(self):
        """Message field 'root_name'."""
        return self._root_name

    @root_name.setter
    def root_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'root_name' field must be of type 'str'"
        self._root_name = value

    @builtins.property
    def nodes(self):
        """Message field 'nodes'."""
        return self._nodes

    @nodes.setter
    def nodes(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import Node
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
                 all(isinstance(v, Node) for v in value) and
                 True), \
                "The 'nodes' field must be a set or sequence and each value of type 'Node'"
        self._nodes = value

    @builtins.property
    def data_wirings(self):
        """Message field 'data_wirings'."""
        return self._data_wirings

    @data_wirings.setter
    def data_wirings(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import NodeDataWiring
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
                 all(isinstance(v, NodeDataWiring) for v in value) and
                 True), \
                "The 'data_wirings' field must be a set or sequence and each value of type 'NodeDataWiring'"
        self._data_wirings = value

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

    @builtins.property
    def state(self):
        """Message field 'state'."""
        return self._state

    @state.setter
    def state(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'state' field must be of type 'str'"
        self._state = value

    @builtins.property
    def public_node_data(self):
        """Message field 'public_node_data'."""
        return self._public_node_data

    @public_node_data.setter
    def public_node_data(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import NodeDataLocation
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
                 all(isinstance(v, NodeDataLocation) for v in value) and
                 True), \
                "The 'public_node_data' field must be a set or sequence and each value of type 'NodeDataLocation'"
        self._public_node_data = value
