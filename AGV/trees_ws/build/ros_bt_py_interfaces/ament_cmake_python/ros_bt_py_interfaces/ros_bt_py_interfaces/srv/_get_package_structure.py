# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/GetPackageStructure.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GetPackageStructure_Request(type):
    """Metaclass of message 'GetPackageStructure_Request'."""

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
                'ros_bt_py_interfaces.srv.GetPackageStructure_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_package_structure__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_package_structure__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_package_structure__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_package_structure__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_package_structure__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetPackageStructure_Request(metaclass=Metaclass_GetPackageStructure_Request):
    """Message class 'GetPackageStructure_Request'."""

    __slots__ = [
        '_package',
        '_show_hidden',
    ]

    _fields_and_field_types = {
        'package': 'string',
        'show_hidden': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.package = kwargs.get('package', str())
        self.show_hidden = kwargs.get('show_hidden', bool())

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
        if self.package != other.package:
            return False
        if self.show_hidden != other.show_hidden:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def package(self):
        """Message field 'package'."""
        return self._package

    @package.setter
    def package(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'package' field must be of type 'str'"
        self._package = value

    @builtins.property
    def show_hidden(self):
        """Message field 'show_hidden'."""
        return self._show_hidden

    @show_hidden.setter
    def show_hidden(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'show_hidden' field must be of type 'bool'"
        self._show_hidden = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_GetPackageStructure_Response(type):
    """Metaclass of message 'GetPackageStructure_Response'."""

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
                'ros_bt_py_interfaces.srv.GetPackageStructure_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_package_structure__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_package_structure__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_package_structure__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_package_structure__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_package_structure__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetPackageStructure_Response(metaclass=Metaclass_GetPackageStructure_Response):
    """Message class 'GetPackageStructure_Response'."""

    __slots__ = [
        '_success',
        '_error_message',
        '_package_structure',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'error_message': 'string',
        'package_structure': 'string',
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
        self.package_structure = kwargs.get('package_structure', str())

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
        if self.package_structure != other.package_structure:
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
    def package_structure(self):
        """Message field 'package_structure'."""
        return self._package_structure

    @package_structure.setter
    def package_structure(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'package_structure' field must be of type 'str'"
        self._package_structure = value


class Metaclass_GetPackageStructure(type):
    """Metaclass of service 'GetPackageStructure'."""

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
                'ros_bt_py_interfaces.srv.GetPackageStructure')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__get_package_structure

            from ros_bt_py_interfaces.srv import _get_package_structure
            if _get_package_structure.Metaclass_GetPackageStructure_Request._TYPE_SUPPORT is None:
                _get_package_structure.Metaclass_GetPackageStructure_Request.__import_type_support__()
            if _get_package_structure.Metaclass_GetPackageStructure_Response._TYPE_SUPPORT is None:
                _get_package_structure.Metaclass_GetPackageStructure_Response.__import_type_support__()


class GetPackageStructure(metaclass=Metaclass_GetPackageStructure):
    from ros_bt_py_interfaces.srv._get_package_structure import GetPackageStructure_Request as Request
    from ros_bt_py_interfaces.srv._get_package_structure import GetPackageStructure_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
