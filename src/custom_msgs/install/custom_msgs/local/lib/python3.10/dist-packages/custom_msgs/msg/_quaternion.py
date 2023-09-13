# generated from rosidl_generator_py/resource/_idl.py.em
# with input from custom_msgs:msg/Quaternion.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Quaternion(type):
    """Metaclass of message 'Quaternion'."""

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
                'custom_msgs.msg.Quaternion')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__quaternion
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__quaternion
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__quaternion
            cls._TYPE_SUPPORT = module.type_support_msg__msg__quaternion
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__quaternion

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Quaternion(metaclass=Metaclass_Quaternion):
    """Message class 'Quaternion'."""

    __slots__ = [
        '_w',
        '_i',
        '_j',
        '_k',
    ]

    _fields_and_field_types = {
        'w': 'float',
        'i': 'float',
        'j': 'float',
        'k': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.w = kwargs.get('w', float())
        self.i = kwargs.get('i', float())
        self.j = kwargs.get('j', float())
        self.k = kwargs.get('k', float())

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
        if self.w != other.w:
            return False
        if self.i != other.i:
            return False
        if self.j != other.j:
            return False
        if self.k != other.k:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def w(self):
        """Message field 'w'."""
        return self._w

    @w.setter
    def w(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'w' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'w' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._w = value

    @builtins.property
    def i(self):
        """Message field 'i'."""
        return self._i

    @i.setter
    def i(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'i' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'i' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
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
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'j' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._j = value

    @builtins.property
    def k(self):
        """Message field 'k'."""
        return self._k

    @k.setter
    def k(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'k' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'k' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._k = value
