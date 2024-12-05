# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/GetAvailableNodes.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GetAvailableNodes_Request(type):
    """Metaclass of message 'GetAvailableNodes_Request'."""

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
                'ros_bt_py_interfaces.srv.GetAvailableNodes_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_available_nodes__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_available_nodes__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_available_nodes__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_available_nodes__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_available_nodes__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetAvailableNodes_Request(metaclass=Metaclass_GetAvailableNodes_Request):
    """Message class 'GetAvailableNodes_Request'."""

    __slots__ = [
        '_node_modules',
    ]

    _fields_and_field_types = {
        'node_modules': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.node_modules = kwargs.get('node_modules', [])

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
        if self.node_modules != other.node_modules:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def node_modules(self):
        """Message field 'node_modules'."""
        return self._node_modules

    @node_modules.setter
    def node_modules(self, value):
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
                "The 'node_modules' field must be a set or sequence and each value of type 'str'"
        self._node_modules = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_GetAvailableNodes_Response(type):
    """Metaclass of message 'GetAvailableNodes_Response'."""

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
                'ros_bt_py_interfaces.srv.GetAvailableNodes_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_available_nodes__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_available_nodes__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_available_nodes__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_available_nodes__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_available_nodes__response

            from ros_bt_py_interfaces.msg import DocumentedNode
            if DocumentedNode.__class__._TYPE_SUPPORT is None:
                DocumentedNode.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetAvailableNodes_Response(metaclass=Metaclass_GetAvailableNodes_Response):
    """Message class 'GetAvailableNodes_Response'."""

    __slots__ = [
        '_available_nodes',
        '_success',
        '_error_message',
    ]

    _fields_and_field_types = {
        'available_nodes': 'sequence<ros_bt_py_interfaces/DocumentedNode>',
        'success': 'boolean',
        'error_message': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'DocumentedNode')),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.available_nodes = kwargs.get('available_nodes', [])
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
        if self.available_nodes != other.available_nodes:
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
    def available_nodes(self):
        """Message field 'available_nodes'."""
        return self._available_nodes

    @available_nodes.setter
    def available_nodes(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import DocumentedNode
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
                 all(isinstance(v, DocumentedNode) for v in value) and
                 True), \
                "The 'available_nodes' field must be a set or sequence and each value of type 'DocumentedNode'"
        self._available_nodes = value

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


class Metaclass_GetAvailableNodes(type):
    """Metaclass of service 'GetAvailableNodes'."""

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
                'ros_bt_py_interfaces.srv.GetAvailableNodes')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__get_available_nodes

            from ros_bt_py_interfaces.srv import _get_available_nodes
            if _get_available_nodes.Metaclass_GetAvailableNodes_Request._TYPE_SUPPORT is None:
                _get_available_nodes.Metaclass_GetAvailableNodes_Request.__import_type_support__()
            if _get_available_nodes.Metaclass_GetAvailableNodes_Response._TYPE_SUPPORT is None:
                _get_available_nodes.Metaclass_GetAvailableNodes_Response.__import_type_support__()


class GetAvailableNodes(metaclass=Metaclass_GetAvailableNodes):
    from ros_bt_py_interfaces.srv._get_available_nodes import GetAvailableNodes_Request as Request
    from ros_bt_py_interfaces.srv._get_available_nodes import GetAvailableNodes_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
