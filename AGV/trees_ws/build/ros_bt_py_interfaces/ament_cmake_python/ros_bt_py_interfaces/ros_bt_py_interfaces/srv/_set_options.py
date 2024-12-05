# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/SetOptions.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SetOptions_Request(type):
    """Metaclass of message 'SetOptions_Request'."""

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
                'ros_bt_py_interfaces.srv.SetOptions_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_options__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_options__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_options__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_options__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_options__request

            from ros_bt_py_interfaces.msg import NodeData
            if NodeData.__class__._TYPE_SUPPORT is None:
                NodeData.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetOptions_Request(metaclass=Metaclass_SetOptions_Request):
    """Message class 'SetOptions_Request'."""

    __slots__ = [
        '_node_name',
        '_rename_node',
        '_new_name',
        '_options',
    ]

    _fields_and_field_types = {
        'node_name': 'string',
        'rename_node': 'boolean',
        'new_name': 'string',
        'options': 'sequence<ros_bt_py_interfaces/NodeData>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'NodeData')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.node_name = kwargs.get('node_name', str())
        self.rename_node = kwargs.get('rename_node', bool())
        self.new_name = kwargs.get('new_name', str())
        self.options = kwargs.get('options', [])

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
        if self.rename_node != other.rename_node:
            return False
        if self.new_name != other.new_name:
            return False
        if self.options != other.options:
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
    def rename_node(self):
        """Message field 'rename_node'."""
        return self._rename_node

    @rename_node.setter
    def rename_node(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'rename_node' field must be of type 'bool'"
        self._rename_node = value

    @builtins.property
    def new_name(self):
        """Message field 'new_name'."""
        return self._new_name

    @new_name.setter
    def new_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'new_name' field must be of type 'str'"
        self._new_name = value

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


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_SetOptions_Response(type):
    """Metaclass of message 'SetOptions_Response'."""

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
                'ros_bt_py_interfaces.srv.SetOptions_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_options__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_options__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_options__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_options__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_options__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetOptions_Response(metaclass=Metaclass_SetOptions_Response):
    """Message class 'SetOptions_Response'."""

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


class Metaclass_SetOptions(type):
    """Metaclass of service 'SetOptions'."""

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
                'ros_bt_py_interfaces.srv.SetOptions')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__set_options

            from ros_bt_py_interfaces.srv import _set_options
            if _set_options.Metaclass_SetOptions_Request._TYPE_SUPPORT is None:
                _set_options.Metaclass_SetOptions_Request.__import_type_support__()
            if _set_options.Metaclass_SetOptions_Response._TYPE_SUPPORT is None:
                _set_options.Metaclass_SetOptions_Response.__import_type_support__()


class SetOptions(metaclass=Metaclass_SetOptions):
    from ros_bt_py_interfaces.srv._set_options import SetOptions_Request as Request
    from ros_bt_py_interfaces.srv._set_options import SetOptions_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
