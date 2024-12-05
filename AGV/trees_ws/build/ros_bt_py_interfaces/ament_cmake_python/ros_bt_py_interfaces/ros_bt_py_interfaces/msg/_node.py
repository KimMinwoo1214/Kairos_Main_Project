# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:msg/Node.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Node(type):
    """Metaclass of message 'Node'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'UNINITIALIZED': 'UNINITIALIZED',
        'IDLE': 'IDLE',
        'UNASSIGNED': 'UNASSIGNED',
        'ASSIGNED': 'ASSIGNED',
        'RUNNING': 'RUNNING',
        'SUCCEEDED': 'SUCCEEDED',
        'SUCCEED': 'SUCCEEDED',
        'SUCCESS': 'SUCCEEDED',
        'FAILED': 'FAILED',
        'FAIL': 'FAILED',
        'FAILURE': 'FAILED',
        'BROKEN': 'BROKEN',
        'PAUSED': 'PAUSED',
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
                'ros_bt_py_interfaces.msg.Node')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__node
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__node
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__node
            cls._TYPE_SUPPORT = module.type_support_msg__msg__node
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__node

            from ros_bt_py_interfaces.msg import NodeData
            if NodeData.__class__._TYPE_SUPPORT is None:
                NodeData.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'UNINITIALIZED': cls.__constants['UNINITIALIZED'],
            'IDLE': cls.__constants['IDLE'],
            'UNASSIGNED': cls.__constants['UNASSIGNED'],
            'ASSIGNED': cls.__constants['ASSIGNED'],
            'RUNNING': cls.__constants['RUNNING'],
            'SUCCEEDED': cls.__constants['SUCCEEDED'],
            'SUCCEED': cls.__constants['SUCCEED'],
            'SUCCESS': cls.__constants['SUCCESS'],
            'FAILED': cls.__constants['FAILED'],
            'FAIL': cls.__constants['FAIL'],
            'FAILURE': cls.__constants['FAILURE'],
            'BROKEN': cls.__constants['BROKEN'],
            'PAUSED': cls.__constants['PAUSED'],
            'SHUTDOWN': cls.__constants['SHUTDOWN'],
        }

    @property
    def UNINITIALIZED(self):
        """Message constant 'UNINITIALIZED'."""
        return Metaclass_Node.__constants['UNINITIALIZED']

    @property
    def IDLE(self):
        """Message constant 'IDLE'."""
        return Metaclass_Node.__constants['IDLE']

    @property
    def UNASSIGNED(self):
        """Message constant 'UNASSIGNED'."""
        return Metaclass_Node.__constants['UNASSIGNED']

    @property
    def ASSIGNED(self):
        """Message constant 'ASSIGNED'."""
        return Metaclass_Node.__constants['ASSIGNED']

    @property
    def RUNNING(self):
        """Message constant 'RUNNING'."""
        return Metaclass_Node.__constants['RUNNING']

    @property
    def SUCCEEDED(self):
        """Message constant 'SUCCEEDED'."""
        return Metaclass_Node.__constants['SUCCEEDED']

    @property
    def SUCCEED(self):
        """Message constant 'SUCCEED'."""
        return Metaclass_Node.__constants['SUCCEED']

    @property
    def SUCCESS(self):
        """Message constant 'SUCCESS'."""
        return Metaclass_Node.__constants['SUCCESS']

    @property
    def FAILED(self):
        """Message constant 'FAILED'."""
        return Metaclass_Node.__constants['FAILED']

    @property
    def FAIL(self):
        """Message constant 'FAIL'."""
        return Metaclass_Node.__constants['FAIL']

    @property
    def FAILURE(self):
        """Message constant 'FAILURE'."""
        return Metaclass_Node.__constants['FAILURE']

    @property
    def BROKEN(self):
        """Message constant 'BROKEN'."""
        return Metaclass_Node.__constants['BROKEN']

    @property
    def PAUSED(self):
        """Message constant 'PAUSED'."""
        return Metaclass_Node.__constants['PAUSED']

    @property
    def SHUTDOWN(self):
        """Message constant 'SHUTDOWN'."""
        return Metaclass_Node.__constants['SHUTDOWN']


class Node(metaclass=Metaclass_Node):
    """
    Message class 'Node'.

    Constants:
      UNINITIALIZED
      IDLE
      UNASSIGNED
      ASSIGNED
      RUNNING
      SUCCEEDED
      SUCCEED
      SUCCESS
      FAILED
      FAIL
      FAILURE
      BROKEN
      PAUSED
      SHUTDOWN
    """

    __slots__ = [
        '_module',
        '_node_class',
        '_version',
        '_max_children',
        '_name',
        '_child_names',
        '_options',
        '_inputs',
        '_outputs',
        '_state',
    ]

    _fields_and_field_types = {
        'module': 'string',
        'node_class': 'string',
        'version': 'string',
        'max_children': 'int32',
        'name': 'string',
        'child_names': 'sequence<string>',
        'options': 'sequence<ros_bt_py_interfaces/NodeData>',
        'inputs': 'sequence<ros_bt_py_interfaces/NodeData>',
        'outputs': 'sequence<ros_bt_py_interfaces/NodeData>',
        'state': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'NodeData')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'NodeData')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'NodeData')),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.module = kwargs.get('module', str())
        self.node_class = kwargs.get('node_class', str())
        self.version = kwargs.get('version', str())
        self.max_children = kwargs.get('max_children', int())
        self.name = kwargs.get('name', str())
        self.child_names = kwargs.get('child_names', [])
        self.options = kwargs.get('options', [])
        self.inputs = kwargs.get('inputs', [])
        self.outputs = kwargs.get('outputs', [])
        self.state = kwargs.get('state', str())

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
        if self.module != other.module:
            return False
        if self.node_class != other.node_class:
            return False
        if self.version != other.version:
            return False
        if self.max_children != other.max_children:
            return False
        if self.name != other.name:
            return False
        if self.child_names != other.child_names:
            return False
        if self.options != other.options:
            return False
        if self.inputs != other.inputs:
            return False
        if self.outputs != other.outputs:
            return False
        if self.state != other.state:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def module(self):
        """Message field 'module'."""
        return self._module

    @module.setter
    def module(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'module' field must be of type 'str'"
        self._module = value

    @builtins.property
    def node_class(self):
        """Message field 'node_class'."""
        return self._node_class

    @node_class.setter
    def node_class(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'node_class' field must be of type 'str'"
        self._node_class = value

    @builtins.property
    def version(self):
        """Message field 'version'."""
        return self._version

    @version.setter
    def version(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'version' field must be of type 'str'"
        self._version = value

    @builtins.property
    def max_children(self):
        """Message field 'max_children'."""
        return self._max_children

    @max_children.setter
    def max_children(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'max_children' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'max_children' field must be an integer in [-2147483648, 2147483647]"
        self._max_children = value

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
    def child_names(self):
        """Message field 'child_names'."""
        return self._child_names

    @child_names.setter
    def child_names(self, value):
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
                "The 'child_names' field must be a set or sequence and each value of type 'str'"
        self._child_names = value

    @builtins.property
    def options(self):
        """Message field 'options'."""
        return self._options

    @options.setter
    def options(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import NodeData
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
                 all(isinstance(v, NodeData) for v in value) and
                 True), \
                "The 'options' field must be a set or sequence and each value of type 'NodeData'"
        self._options = value

    @builtins.property
    def inputs(self):
        """Message field 'inputs'."""
        return self._inputs

    @inputs.setter
    def inputs(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import NodeData
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
                 all(isinstance(v, NodeData) for v in value) and
                 True), \
                "The 'inputs' field must be a set or sequence and each value of type 'NodeData'"
        self._inputs = value

    @builtins.property
    def outputs(self):
        """Message field 'outputs'."""
        return self._outputs

    @outputs.setter
    def outputs(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import NodeData
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
                 all(isinstance(v, NodeData) for v in value) and
                 True), \
                "The 'outputs' field must be a set or sequence and each value of type 'NodeData'"
        self._outputs = value

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
