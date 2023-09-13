# generated from rosidl_generator_py/resource/_idl.py.em
# with input from custom_msgs:srv/GetFromRio.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GetFromRio_Request(type):
    """Metaclass of message 'GetFromRio_Request'."""

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
            module = import_type_support('custom_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'custom_msgs.srv.GetFromRio_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_from_rio__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_from_rio__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_from_rio__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_from_rio__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_from_rio__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetFromRio_Request(metaclass=Metaclass_GetFromRio_Request):
    """Message class 'GetFromRio_Request'."""

    __slots__ = [
        '_a',
    ]

    _fields_and_field_types = {
        'a': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.a = kwargs.get('a', bool())

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
        if self.a != other.a:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def a(self):
        """Message field 'a'."""
        return self._a

    @a.setter
    def a(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'a' field must be of type 'bool'"
        self._a = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_GetFromRio_Response(type):
    """Metaclass of message 'GetFromRio_Response'."""

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
            module = import_type_support('custom_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'custom_msgs.srv.GetFromRio_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_from_rio__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_from_rio__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_from_rio__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_from_rio__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_from_rio__response

            from custom_msgs.msg import Pose3D
            if Pose3D.__class__._TYPE_SUPPORT is None:
                Pose3D.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetFromRio_Response(metaclass=Metaclass_GetFromRio_Response):
    """Message class 'GetFromRio_Response'."""

    __slots__ = [
        '_b',
        '_c',
    ]

    _fields_and_field_types = {
        'b': 'custom_msgs/Pose3D',
        'c': 'custom_msgs/Pose3D',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['custom_msgs', 'msg'], 'Pose3D'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['custom_msgs', 'msg'], 'Pose3D'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from custom_msgs.msg import Pose3D
        self.b = kwargs.get('b', Pose3D())
        from custom_msgs.msg import Pose3D
        self.c = kwargs.get('c', Pose3D())

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
        if self.b != other.b:
            return False
        if self.c != other.c:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def b(self):
        """Message field 'b'."""
        return self._b

    @b.setter
    def b(self, value):
        if __debug__:
            from custom_msgs.msg import Pose3D
            assert \
                isinstance(value, Pose3D), \
                "The 'b' field must be a sub message of type 'Pose3D'"
        self._b = value

    @builtins.property
    def c(self):
        """Message field 'c'."""
        return self._c

    @c.setter
    def c(self, value):
        if __debug__:
            from custom_msgs.msg import Pose3D
            assert \
                isinstance(value, Pose3D), \
                "The 'c' field must be a sub message of type 'Pose3D'"
        self._c = value


class Metaclass_GetFromRio(type):
    """Metaclass of service 'GetFromRio'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('custom_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'custom_msgs.srv.GetFromRio')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__get_from_rio

            from custom_msgs.srv import _get_from_rio
            if _get_from_rio.Metaclass_GetFromRio_Request._TYPE_SUPPORT is None:
                _get_from_rio.Metaclass_GetFromRio_Request.__import_type_support__()
            if _get_from_rio.Metaclass_GetFromRio_Response._TYPE_SUPPORT is None:
                _get_from_rio.Metaclass_GetFromRio_Response.__import_type_support__()


class GetFromRio(metaclass=Metaclass_GetFromRio):
    from custom_msgs.srv._get_from_rio import GetFromRio_Request as Request
    from custom_msgs.srv._get_from_rio import GetFromRio_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
