# generated from rosidl_generator_py/resource/_idl.py.em
# with input from custom_msgs:srv/Gstam.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Gstam_Request(type):
    """Metaclass of message 'Gstam_Request'."""

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
                'custom_msgs.srv.Gstam_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__gstam__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__gstam__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__gstam__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__gstam__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__gstam__request

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


class Gstam_Request(metaclass=Metaclass_Gstam_Request):
    """Message class 'Gstam_Request'."""

    __slots__ = [
        '_a',
        '_b',
        '_c',
        '_d',
        '_e',
        '_f',
        '_g',
        '_h',
        '_i',
        '_j',
    ]

    _fields_and_field_types = {
        'a': 'custom_msgs/Pose3D',
        'b': 'custom_msgs/Pose3D',
        'c': 'custom_msgs/Pose3D',
        'd': 'custom_msgs/Pose3D',
        'e': 'custom_msgs/Pose3D',
        'f': 'custom_msgs/Pose3D',
        'g': 'custom_msgs/Pose3D',
        'h': 'custom_msgs/Pose3D',
        'i': 'custom_msgs/Pose3D',
        'j': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['custom_msgs', 'msg'], 'Pose3D'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['custom_msgs', 'msg'], 'Pose3D'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['custom_msgs', 'msg'], 'Pose3D'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['custom_msgs', 'msg'], 'Pose3D'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['custom_msgs', 'msg'], 'Pose3D'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['custom_msgs', 'msg'], 'Pose3D'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['custom_msgs', 'msg'], 'Pose3D'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['custom_msgs', 'msg'], 'Pose3D'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['custom_msgs', 'msg'], 'Pose3D'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from custom_msgs.msg import Pose3D
        self.a = kwargs.get('a', Pose3D())
        from custom_msgs.msg import Pose3D
        self.b = kwargs.get('b', Pose3D())
        from custom_msgs.msg import Pose3D
        self.c = kwargs.get('c', Pose3D())
        from custom_msgs.msg import Pose3D
        self.d = kwargs.get('d', Pose3D())
        from custom_msgs.msg import Pose3D
        self.e = kwargs.get('e', Pose3D())
        from custom_msgs.msg import Pose3D
        self.f = kwargs.get('f', Pose3D())
        from custom_msgs.msg import Pose3D
        self.g = kwargs.get('g', Pose3D())
        from custom_msgs.msg import Pose3D
        self.h = kwargs.get('h', Pose3D())
        from custom_msgs.msg import Pose3D
        self.i = kwargs.get('i', Pose3D())
        self.j = kwargs.get('j', float())

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
        if self.b != other.b:
            return False
        if self.c != other.c:
            return False
        if self.d != other.d:
            return False
        if self.e != other.e:
            return False
        if self.f != other.f:
            return False
        if self.g != other.g:
            return False
        if self.h != other.h:
            return False
        if self.i != other.i:
            return False
        if self.j != other.j:
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
            from custom_msgs.msg import Pose3D
            assert \
                isinstance(value, Pose3D), \
                "The 'a' field must be a sub message of type 'Pose3D'"
        self._a = value

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

    @builtins.property
    def d(self):
        """Message field 'd'."""
        return self._d

    @d.setter
    def d(self, value):
        if __debug__:
            from custom_msgs.msg import Pose3D
            assert \
                isinstance(value, Pose3D), \
                "The 'd' field must be a sub message of type 'Pose3D'"
        self._d = value

    @builtins.property
    def e(self):
        """Message field 'e'."""
        return self._e

    @e.setter
    def e(self, value):
        if __debug__:
            from custom_msgs.msg import Pose3D
            assert \
                isinstance(value, Pose3D), \
                "The 'e' field must be a sub message of type 'Pose3D'"
        self._e = value

    @builtins.property
    def f(self):
        """Message field 'f'."""
        return self._f

    @f.setter
    def f(self, value):
        if __debug__:
            from custom_msgs.msg import Pose3D
            assert \
                isinstance(value, Pose3D), \
                "The 'f' field must be a sub message of type 'Pose3D'"
        self._f = value

    @builtins.property
    def g(self):
        """Message field 'g'."""
        return self._g

    @g.setter
    def g(self, value):
        if __debug__:
            from custom_msgs.msg import Pose3D
            assert \
                isinstance(value, Pose3D), \
                "The 'g' field must be a sub message of type 'Pose3D'"
        self._g = value

    @builtins.property
    def h(self):
        """Message field 'h'."""
        return self._h

    @h.setter
    def h(self, value):
        if __debug__:
            from custom_msgs.msg import Pose3D
            assert \
                isinstance(value, Pose3D), \
                "The 'h' field must be a sub message of type 'Pose3D'"
        self._h = value

    @builtins.property
    def i(self):
        """Message field 'i'."""
        return self._i

    @i.setter
    def i(self, value):
        if __debug__:
            from custom_msgs.msg import Pose3D
            assert \
                isinstance(value, Pose3D), \
                "The 'i' field must be a sub message of type 'Pose3D'"
        self._i = value

    @builtins.property
    def j(self):
        """Message field 'j'."""
        return self._j

    @j.setter
    def j(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'j' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'j' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._j = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Gstam_Response(type):
    """Metaclass of message 'Gstam_Response'."""

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
                'custom_msgs.srv.Gstam_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__gstam__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__gstam__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__gstam__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__gstam__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__gstam__response

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


class Gstam_Response(metaclass=Metaclass_Gstam_Response):
    """Message class 'Gstam_Response'."""

    __slots__ = [
        '_final',
    ]

    _fields_and_field_types = {
        'final': 'custom_msgs/Pose3D',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['custom_msgs', 'msg'], 'Pose3D'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from custom_msgs.msg import Pose3D
        self.final = kwargs.get('final', Pose3D())

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
        if self.final != other.final:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def final(self):
        """Message field 'final'."""
        return self._final

    @final.setter
    def final(self, value):
        if __debug__:
            from custom_msgs.msg import Pose3D
            assert \
                isinstance(value, Pose3D), \
                "The 'final' field must be a sub message of type 'Pose3D'"
        self._final = value


class Metaclass_Gstam(type):
    """Metaclass of service 'Gstam'."""

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
                'custom_msgs.srv.Gstam')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__gstam

            from custom_msgs.srv import _gstam
            if _gstam.Metaclass_Gstam_Request._TYPE_SUPPORT is None:
                _gstam.Metaclass_Gstam_Request.__import_type_support__()
            if _gstam.Metaclass_Gstam_Response._TYPE_SUPPORT is None:
                _gstam.Metaclass_Gstam_Response.__import_type_support__()


class Gstam(metaclass=Metaclass_Gstam):
    from custom_msgs.srv._gstam import Gstam_Request as Request
    from custom_msgs.srv._gstam import Gstam_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
