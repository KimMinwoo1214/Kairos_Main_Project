# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/AddNodeAtIndex.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AddNodeAtIndex_Request(type):
    """Metaclass of message 'AddNodeAtIndex_Request'."""

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
                'ros_bt_py_interfaces.srv.AddNodeAtIndex_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__add_node_at_index__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__add_node_at_index__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__add_node_at_index__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__add_node_at_index__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__add_node_at_index__request

            from ros_bt_py_interfaces.msg import Node
            if Node.__class__._TYPE_SUPPORT is None:
                Node.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AddNodeAtIndex_Request(metaclass=Metaclass_AddNodeAtIndex_Request):
    """Message class 'AddNodeAtIndex_Request'."""

    __slots__ = [
        '_parent_name',
        '_node',
        '_allow_rename',
        '_new_child_index',
    ]

    _fields_and_field_types = {
        'parent_name': 'string',
        'node': 'ros_bt_py_interfaces/Node',
        'allow_rename': 'boolean',
        'new_child_index': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'Node'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.parent_name = kwargs.get('parent_name', str())
        from ros_bt_py_interfaces.msg import Node
        self.node = kwargs.get('node', Node())
        self.allow_rename = kwargs.get('allow_rename', bool())
        self.new_child_index = kwargs.get('new_child_index', int())

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
        if self.parent_name != other.parent_name:
            return False
        if self.node != other.node:
            return False
        if self.allow_rename != other.allow_rename:
            return False
        if self.new_child_index != other.new_child_index:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def parent_name(self):
        """Message field 'parent_name'."""
        return self._parent_name

    @parent_name.setter
    def parent_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'parent_name' field must be of type 'str'"
        self._parent_name = value

    @builtins.property
    def node(self):
        """Message field 'node'."""
        return self._node

    @node.setter
    def node(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import Node
            assert \
                isinstance(value, Node), \
                "The 'node' field must be a sub message of type 'Node'"
        self._node = value

    @builtins.property
    def allow_rename(self):
        """Message field 'allow_rename'."""
        return self._allow_rename

    @allow_rename.setter
    def allow_rename(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'allow_rename' field must be of type 'bool'"
        self._allow_rename = value

    @builtins.property
    def new_child_index(self):
        """Message field 'new_child_index'."""
        return self._new_child_index

    @new_child_index.setter
    def new_child_index(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'new_child_index' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'new_child_index' field must be an integer in [-2147483648, 2147483647]"
        self._new_child_index = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AddNodeAtIndex_Response(type):
    """Metaclass of message 'AddNodeAtIndex_Response'."""

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
                'ros_bt_py_interfaces.srv.AddNodeAtIndex_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__add_node_at_index__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__add_node_at_index__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__add_node_at_index__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__add_node_at_index__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__add_node_at_index__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AddNodeAtIndex_Response(metaclass=Metaclass_AddNodeAtIndex_Response):
    """Message class 'AddNodeAtIndex_Response'."""

    __slots__ = [
        '_success',
        '_actual_node_name',
        '_error_message',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'actual_node_name': 'string',
        'error_message': 'string',
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
        self.actual_node_name = kwargs.get('actual_node_name', str())
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
        if self.actual_node_name != other.actual_node_name:
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
    def actual_node_name(self):
        """Message field 'actual_node_name'."""
        return self._actual_node_name

    @actual_node_name.setter
    def actual_node_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'actual_node_name' field must be of type 'str'"
        self._actual_node_name = value

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


class Metaclass_AddNodeAtIndex(type):
    """Metaclass of service 'AddNodeAtIndex'."""

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
                'ros_bt_py_interfaces.srv.AddNodeAtIndex')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__add_node_at_index

            from ros_bt_py_interfaces.srv import _add_node_at_index
            if _add_node_at_index.Metaclass_AddNodeAtIndex_Request._TYPE_SUPPORT is None:
                _add_node_at_index.Metaclass_AddNodeAtIndex_Request.__import_type_support__()
            if _add_node_at_index.Metaclass_AddNodeAtIndex_Response._TYPE_SUPPORT is None:
                _add_node_at_index.Metaclass_AddNodeAtIndex_Response.__import_type_support__()


class AddNodeAtIndex(metaclass=Metaclass_AddNodeAtIndex):
    from ros_bt_py_interfaces.srv._add_node_at_index import AddNodeAtIndex_Request as Request
    from ros_bt_py_interfaces.srv._add_node_at_index import AddNodeAtIndex_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
