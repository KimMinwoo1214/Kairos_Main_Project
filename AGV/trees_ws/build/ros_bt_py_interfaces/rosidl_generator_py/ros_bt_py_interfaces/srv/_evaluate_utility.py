# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/EvaluateUtility.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_EvaluateUtility_Request(type):
    """Metaclass of message 'EvaluateUtility_Request'."""

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
                'ros_bt_py_interfaces.srv.EvaluateUtility_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__evaluate_utility__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__evaluate_utility__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__evaluate_utility__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__evaluate_utility__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__evaluate_utility__request

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


class EvaluateUtility_Request(metaclass=Metaclass_EvaluateUtility_Request):
    """Message class 'EvaluateUtility_Request'."""

    __slots__ = [
        '_tree',
    ]

    _fields_and_field_types = {
        'tree': 'ros_bt_py_interfaces/Tree',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'Tree'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
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
        if self.tree != other.tree:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

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


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_EvaluateUtility_Response(type):
    """Metaclass of message 'EvaluateUtility_Response'."""

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
                'ros_bt_py_interfaces.srv.EvaluateUtility_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__evaluate_utility__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__evaluate_utility__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__evaluate_utility__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__evaluate_utility__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__evaluate_utility__response

            from ros_bt_py_interfaces.msg import UtilityBounds
            if UtilityBounds.__class__._TYPE_SUPPORT is None:
                UtilityBounds.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class EvaluateUtility_Response(metaclass=Metaclass_EvaluateUtility_Response):
    """Message class 'EvaluateUtility_Response'."""

    __slots__ = [
        '_utility',
    ]

    _fields_and_field_types = {
        'utility': 'ros_bt_py_interfaces/UtilityBounds',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'UtilityBounds'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from ros_bt_py_interfaces.msg import UtilityBounds
        self.utility = kwargs.get('utility', UtilityBounds())

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
        if self.utility != other.utility:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def utility(self):
        """Message field 'utility'."""
        return self._utility

    @utility.setter
    def utility(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import UtilityBounds
            assert \
                isinstance(value, UtilityBounds), \
                "The 'utility' field must be a sub message of type 'UtilityBounds'"
        self._utility = value


class Metaclass_EvaluateUtility(type):
    """Metaclass of service 'EvaluateUtility'."""

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
                'ros_bt_py_interfaces.srv.EvaluateUtility')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__evaluate_utility

            from ros_bt_py_interfaces.srv import _evaluate_utility
            if _evaluate_utility.Metaclass_EvaluateUtility_Request._TYPE_SUPPORT is None:
                _evaluate_utility.Metaclass_EvaluateUtility_Request.__import_type_support__()
            if _evaluate_utility.Metaclass_EvaluateUtility_Response._TYPE_SUPPORT is None:
                _evaluate_utility.Metaclass_EvaluateUtility_Response.__import_type_support__()


class EvaluateUtility(metaclass=Metaclass_EvaluateUtility):
    from ros_bt_py_interfaces.srv._evaluate_utility import EvaluateUtility_Request as Request
    from ros_bt_py_interfaces.srv._evaluate_utility import EvaluateUtility_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
