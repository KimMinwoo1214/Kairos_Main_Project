# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:msg/CapabilityImplementation.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CapabilityImplementation(type):
    """Metaclass of message 'CapabilityImplementation'."""

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
                'ros_bt_py_interfaces.msg.CapabilityImplementation')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__capability_implementation
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__capability_implementation
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__capability_implementation
            cls._TYPE_SUPPORT = module.type_support_msg__msg__capability_implementation
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__capability_implementation

            from ros_bt_py_interfaces.msg import Precondition
            if Precondition.__class__._TYPE_SUPPORT is None:
                Precondition.__class__.__import_type_support__()

            from ros_bt_py_interfaces.msg import Tree
            if Tree.__class__._TYPE_SUPPORT is None:
                Tree.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CapabilityImplementation(metaclass=Metaclass_CapabilityImplementation):
    """Message class 'CapabilityImplementation'."""

    __slots__ = [
        '_name',
        '_version',
        '_preconditions',
        '_tags_dict',
        '_tree',
    ]

    _fields_and_field_types = {
        'name': 'string',
        'version': 'string',
        'preconditions': 'sequence<ros_bt_py_interfaces/Precondition>',
        'tags_dict': 'string',
        'tree': 'ros_bt_py_interfaces/Tree',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'Precondition')),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'Tree'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.name = kwargs.get('name', str())
        self.version = kwargs.get('version', str())
        self.preconditions = kwargs.get('preconditions', [])
        self.tags_dict = kwargs.get('tags_dict', str())
        from ros_bt_py_interfaces.msg import Tree
        self.tree = kwargs.get('tree', Tree())

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
        if self.version != other.version:
            return False
        if self.preconditions != other.preconditions:
            return False
        if self.tags_dict != other.tags_dict:
            return False
        if self.tree != other.tree:
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
    def preconditions(self):
        """Message field 'preconditions'."""
        return self._preconditions

    @preconditions.setter
    def preconditions(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import Precondition
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
                 all(isinstance(v, Precondition) for v in value) and
                 True), \
                "The 'preconditions' field must be a set or sequence and each value of type 'Precondition'"
        self._preconditions = value

    @builtins.property
    def tags_dict(self):
        """Message field 'tags_dict'."""
        return self._tags_dict

    @tags_dict.setter
    def tags_dict(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'tags_dict' field must be of type 'str'"
        self._tags_dict = value

    @builtins.property
    def tree(self):
        """Message field 'tree'."""
        return self._tree

    @tree.setter
    def tree(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import Tree
            assert \
                isinstance(value, Tree), \
                "The 'tree' field must be a sub message of type 'Tree'"
        self._tree = value
