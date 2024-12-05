# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:msg/NodeDataWiring.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_NodeDataWiring(type):
    """Metaclass of message 'NodeDataWiring'."""

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
                'ros_bt_py_interfaces.msg.NodeDataWiring')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__node_data_wiring
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__node_data_wiring
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__node_data_wiring
            cls._TYPE_SUPPORT = module.type_support_msg__msg__node_data_wiring
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__node_data_wiring

            from ros_bt_py_interfaces.msg import NodeDataLocation
            if NodeDataLocation.__class__._TYPE_SUPPORT is None:
                NodeDataLocation.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NodeDataWiring(metaclass=Metaclass_NodeDataWiring):
    """Message class 'NodeDataWiring'."""

    __slots__ = [
        '_source',
        '_target',
    ]

    _fields_and_field_types = {
        'source': 'ros_bt_py_interfaces/NodeDataLocation',
        'target': 'ros_bt_py_interfaces/NodeDataLocation',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'NodeDataLocation'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'NodeDataLocation'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from ros_bt_py_interfaces.msg import NodeDataLocation
        self.source = kwargs.get('source', NodeDataLocation())
        from ros_bt_py_interfaces.msg import NodeDataLocation
        self.target = kwargs.get('target', NodeDataLocation())

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
        if self.source != other.source:
            return False
        if self.target != other.target:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def source(self):
        """Message field 'source'."""
        return self._source

    @source.setter
    def source(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import NodeDataLocation
            assert \
                isinstance(value, NodeDataLocation), \
                "The 'source' field must be a sub message of type 'NodeDataLocation'"
        self._source = value

    @builtins.property
    def target(self):
        """Message field 'target'."""
        return self._target

    @target.setter
    def target(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import NodeDataLocation
            assert \
                isinstance(value, NodeDataLocation), \
                "The 'target' field must be a sub message of type 'NodeDataLocation'"
        self._target = value
