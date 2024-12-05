# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/GetSubtree.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GetSubtree_Request(type):
    """Metaclass of message 'GetSubtree_Request'."""

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
                'ros_bt_py_interfaces.srv.GetSubtree_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_subtree__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_subtree__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_subtree__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_subtree__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_subtree__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetSubtree_Request(metaclass=Metaclass_GetSubtree_Request):
    """Message class 'GetSubtree_Request'."""

    __slots__ = [
        '_subtree_root_name',
    ]

    _fields_and_field_types = {
        'subtree_root_name': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.subtree_root_name = kwargs.get('subtree_root_name', str())

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
        if self.subtree_root_name != other.subtree_root_name:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def subtree_root_name(self):
        """Message field 'subtree_root_name'."""
        return self._subtree_root_name

    @subtree_root_name.setter
    def subtree_root_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'subtree_root_name' field must be of type 'str'"
        self._subtree_root_name = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_GetSubtree_Response(type):
    """Metaclass of message 'GetSubtree_Response'."""

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
                'ros_bt_py_interfaces.srv.GetSubtree_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_subtree__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_subtree__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_subtree__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_subtree__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_subtree__response

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


class GetSubtree_Response(metaclass=Metaclass_GetSubtree_Response):
    """Message class 'GetSubtree_Response'."""

    __slots__ = [
        '_success',
        '_error_message',
        '_subtree',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'error_message': 'string',
        'subtree': 'ros_bt_py_interfaces/Tree',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'Tree'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())
        self.error_message = kwargs.get('error_message', str())
        from ros_bt_py_interfaces.msg import Tree
        self.subtree = kwargs.get('subtree', Tree())

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
        if self.subtree != other.subtree:
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

    @builtins.property
    def subtree(self):
        """Message field 'subtree'."""
        return self._subtree

    @subtree.setter
    def subtree(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import Tree
            assert \
                isinstance(value, Tree), \
                "The 'subtree' field must be a sub message of type 'Tree'"
        self._subtree = value


class Metaclass_GetSubtree(type):
    """Metaclass of service 'GetSubtree'."""

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
                'ros_bt_py_interfaces.srv.GetSubtree')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__get_subtree

            from ros_bt_py_interfaces.srv import _get_subtree
            if _get_subtree.Metaclass_GetSubtree_Request._TYPE_SUPPORT is None:
                _get_subtree.Metaclass_GetSubtree_Request.__import_type_support__()
            if _get_subtree.Metaclass_GetSubtree_Response._TYPE_SUPPORT is None:
                _get_subtree.Metaclass_GetSubtree_Response.__import_type_support__()


class GetSubtree(metaclass=Metaclass_GetSubtree):
    from ros_bt_py_interfaces.srv._get_subtree import GetSubtree_Request as Request
    from ros_bt_py_interfaces.srv._get_subtree import GetSubtree_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')