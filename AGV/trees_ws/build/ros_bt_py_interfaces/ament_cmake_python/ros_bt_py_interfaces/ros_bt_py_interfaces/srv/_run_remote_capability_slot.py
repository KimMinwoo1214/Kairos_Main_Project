# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros_bt_py_interfaces:srv/RunRemoteCapabilitySlot.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RunRemoteCapabilitySlot_Request(type):
    """Metaclass of message 'RunRemoteCapabilitySlot_Request'."""

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
                'ros_bt_py_interfaces.srv.RunRemoteCapabilitySlot_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__run_remote_capability_slot__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__run_remote_capability_slot__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__run_remote_capability_slot__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__run_remote_capability_slot__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__run_remote_capability_slot__request

            from ros_bt_py_interfaces.msg import CapabilityInterface
            if CapabilityInterface.__class__._TYPE_SUPPORT is None:
                CapabilityInterface.__class__.__import_type_support__()

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


class RunRemoteCapabilitySlot_Request(metaclass=Metaclass_RunRemoteCapabilitySlot_Request):
    """Message class 'RunRemoteCapabilitySlot_Request'."""

    __slots__ = [
        '_interface',
        '_implementation_tree',
        '_node_id',
    ]

    _fields_and_field_types = {
        'interface': 'ros_bt_py_interfaces/CapabilityInterface',
        'implementation_tree': 'ros_bt_py_interfaces/Tree',
        'node_id': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'CapabilityInterface'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ros_bt_py_interfaces', 'msg'], 'Tree'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from ros_bt_py_interfaces.msg import CapabilityInterface
        self.interface = kwargs.get('interface', CapabilityInterface())
        from ros_bt_py_interfaces.msg import Tree
        self.implementation_tree = kwargs.get('implementation_tree', Tree())
        self.node_id = kwargs.get('node_id', str())

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
        if self.interface != other.interface:
            return False
        if self.implementation_tree != other.implementation_tree:
            return False
        if self.node_id != other.node_id:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def interface(self):
        """Message field 'interface'."""
        return self._interface

    @interface.setter
    def interface(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import CapabilityInterface
            assert \
                isinstance(value, CapabilityInterface), \
                "The 'interface' field must be a sub message of type 'CapabilityInterface'"
        self._interface = value

    @builtins.property
    def implementation_tree(self):
        """Message field 'implementation_tree'."""
        return self._implementation_tree

    @implementation_tree.setter
    def implementation_tree(self, value):
        if __debug__:
            from ros_bt_py_interfaces.msg import Tree
            assert \
                isinstance(value, Tree), \
                "The 'implementation_tree' field must be a sub message of type 'Tree'"
        self._implementation_tree = value

    @builtins.property
    def node_id(self):
        """Message field 'node_id'."""
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'node_id' field must be of type 'str'"
        self._node_id = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_RunRemoteCapabilitySlot_Response(type):
    """Metaclass of message 'RunRemoteCapabilitySlot_Response'."""

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
                'ros_bt_py_interfaces.srv.RunRemoteCapabilitySlot_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__run_remote_capability_slot__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__run_remote_capability_slot__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__run_remote_capability_slot__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__run_remote_capability_slot__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__run_remote_capability_slot__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RunRemoteCapabilitySlot_Response(metaclass=Metaclass_RunRemoteCapabilitySlot_Response):
    """Message class 'RunRemoteCapabilitySlot_Response'."""

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


class Metaclass_RunRemoteCapabilitySlot(type):
    """Metaclass of service 'RunRemoteCapabilitySlot'."""

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
                'ros_bt_py_interfaces.srv.RunRemoteCapabilitySlot')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__run_remote_capability_slot

            from ros_bt_py_interfaces.srv import _run_remote_capability_slot
            if _run_remote_capability_slot.Metaclass_RunRemoteCapabilitySlot_Request._TYPE_SUPPORT is None:
                _run_remote_capability_slot.Metaclass_RunRemoteCapabilitySlot_Request.__import_type_support__()
            if _run_remote_capability_slot.Metaclass_RunRemoteCapabilitySlot_Response._TYPE_SUPPORT is None:
                _run_remote_capability_slot.Metaclass_RunRemoteCapabilitySlot_Response.__import_type_support__()


class RunRemoteCapabilitySlot(metaclass=Metaclass_RunRemoteCapabilitySlot):
    from ros_bt_py_interfaces.srv._run_remote_capability_slot import RunRemoteCapabilitySlot_Request as Request
    from ros_bt_py_interfaces.srv._run_remote_capability_slot import RunRemoteCapabilitySlot_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
