# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/SaveTree.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SaveTree_Request(type):
    """Metaclass of message 'SaveTree_Request'."""

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
                'ros_bt_py_interfaces.srv.SaveTree_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__save_tree__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__save_tree__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__save_tree__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__save_tree__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__save_tree__request

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


class SaveTree_Request(metaclass=Metaclass_SaveTree_Request):
    """Message class 'SaveTree_Request'."""

    __slots__ = [
        '_storage_path',
        '_filepath',
        '_tree',
        '_allow_overwrite',
        '_allow_rename',
    ]

    _fields_and_field_types = {
        'storage_path': 'string',
        'filepath': 'string',
        'tree': 'ros_bt_py_interfaces/Tree',
        'allow_overwrite': 'boolean',
        'allow_rename': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'Tree'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.storage_path = kwargs.get('storage_path', str())
        self.filepath = kwargs.get('filepath', str())
        from ros_bt_py_interfaces.msg import Tree
        self.tree = kwargs.get('tree', Tree())
        self.allow_overwrite = kwargs.get('allow_overwrite', bool())
        self.allow_rename = kwargs.get('allow_rename', bool())

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
        if self.storage_path != other.storage_path:
            return False
        if self.filepath != other.filepath:
            return False
        if self.tree != other.tree:
            return False
        if self.allow_overwrite != other.allow_overwrite:
            return False
        if self.allow_rename != other.allow_rename:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def storage_path(self):
        """Message field 'storage_path'."""
        return self._storage_path

    @storage_path.setter
    def storage_path(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'storage_path' field must be of type 'str'"
        self._storage_path = value

    @builtins.property
    def filepath(self):
        """Message field 'filepath'."""
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'filepath' field must be of type 'str'"
        self._filepath = value

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

    @builtins.property
    def allow_overwrite(self):
        """Message field 'allow_overwrite'."""
        return self._allow_overwrite

    @allow_overwrite.setter
    def allow_overwrite(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'allow_overwrite' field must be of type 'bool'"
        self._allow_overwrite = value

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


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_SaveTree_Response(type):
    """Metaclass of message 'SaveTree_Response'."""

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
                'ros_bt_py_interfaces.srv.SaveTree_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__save_tree__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__save_tree__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__save_tree__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__save_tree__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__save_tree__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SaveTree_Response(metaclass=Metaclass_SaveTree_Response):
    """Message class 'SaveTree_Response'."""

    __slots__ = [
        '_success',
        '_error_message',
        '_file_path',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'error_message': 'string',
        'file_path': 'string',
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
        self.error_message = kwargs.get('error_message', str())
        self.file_path = kwargs.get('file_path', str())

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
        if self.file_path != other.file_path:
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
    def file_path(self):
        """Message field 'file_path'."""
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'file_path' field must be of type 'str'"
        self._file_path = value


class Metaclass_SaveTree(type):
    """Metaclass of service 'SaveTree'."""

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
                'ros_bt_py_interfaces.srv.SaveTree')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__save_tree

            from ros_bt_py_interfaces.srv import _save_tree
            if _save_tree.Metaclass_SaveTree_Request._TYPE_SUPPORT is None:
                _save_tree.Metaclass_SaveTree_Request.__import_type_support__()
            if _save_tree.Metaclass_SaveTree_Response._TYPE_SUPPORT is None:
                _save_tree.Metaclass_SaveTree_Response.__import_type_support__()


class SaveTree(metaclass=Metaclass_SaveTree):
    from ros_bt_py_interfaces.srv._save_tree import SaveTree_Request as Request
    from ros_bt_py_interfaces.srv._save_tree import SaveTree_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
