// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from custom_msgs:srv/Gstam.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "custom_msgs/srv/detail/gstam__struct.h"
#include "custom_msgs/srv/detail/gstam__functions.h"

bool custom_msgs__msg__pose3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * custom_msgs__msg__pose3_d__convert_to_py(void * raw_ros_message);
bool custom_msgs__msg__pose3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * custom_msgs__msg__pose3_d__convert_to_py(void * raw_ros_message);
bool custom_msgs__msg__pose3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * custom_msgs__msg__pose3_d__convert_to_py(void * raw_ros_message);
bool custom_msgs__msg__pose3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * custom_msgs__msg__pose3_d__convert_to_py(void * raw_ros_message);
bool custom_msgs__msg__pose3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * custom_msgs__msg__pose3_d__convert_to_py(void * raw_ros_message);
bool custom_msgs__msg__pose3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * custom_msgs__msg__pose3_d__convert_to_py(void * raw_ros_message);
bool custom_msgs__msg__pose3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * custom_msgs__msg__pose3_d__convert_to_py(void * raw_ros_message);
bool custom_msgs__msg__pose3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * custom_msgs__msg__pose3_d__convert_to_py(void * raw_ros_message);
bool custom_msgs__msg__pose3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * custom_msgs__msg__pose3_d__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool custom_msgs__srv__gstam__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[37];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("custom_msgs.srv._gstam.Gstam_Request", full_classname_dest, 36) == 0);
  }
  custom_msgs__srv__Gstam_Request * ros_message = _ros_message;
  {  // a
    PyObject * field = PyObject_GetAttrString(_pymsg, "a");
    if (!field) {
      return false;
    }
    if (!custom_msgs__msg__pose3_d__convert_from_py(field, &ros_message->a)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // b
    PyObject * field = PyObject_GetAttrString(_pymsg, "b");
    if (!field) {
      return false;
    }
    if (!custom_msgs__msg__pose3_d__convert_from_py(field, &ros_message->b)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // c
    PyObject * field = PyObject_GetAttrString(_pymsg, "c");
    if (!field) {
      return false;
    }
    if (!custom_msgs__msg__pose3_d__convert_from_py(field, &ros_message->c)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // d
    PyObject * field = PyObject_GetAttrString(_pymsg, "d");
    if (!field) {
      return false;
    }
    if (!custom_msgs__msg__pose3_d__convert_from_py(field, &ros_message->d)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // e
    PyObject * field = PyObject_GetAttrString(_pymsg, "e");
    if (!field) {
      return false;
    }
    if (!custom_msgs__msg__pose3_d__convert_from_py(field, &ros_message->e)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // f
    PyObject * field = PyObject_GetAttrString(_pymsg, "f");
    if (!field) {
      return false;
    }
    if (!custom_msgs__msg__pose3_d__convert_from_py(field, &ros_message->f)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // g
    PyObject * field = PyObject_GetAttrString(_pymsg, "g");
    if (!field) {
      return false;
    }
    if (!custom_msgs__msg__pose3_d__convert_from_py(field, &ros_message->g)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // h
    PyObject * field = PyObject_GetAttrString(_pymsg, "h");
    if (!field) {
      return false;
    }
    if (!custom_msgs__msg__pose3_d__convert_from_py(field, &ros_message->h)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // i
    PyObject * field = PyObject_GetAttrString(_pymsg, "i");
    if (!field) {
      return false;
    }
    if (!custom_msgs__msg__pose3_d__convert_from_py(field, &ros_message->i)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // j
    PyObject * field = PyObject_GetAttrString(_pymsg, "j");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->j = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * custom_msgs__srv__gstam__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Gstam_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("custom_msgs.srv._gstam");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Gstam_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  custom_msgs__srv__Gstam_Request * ros_message = (custom_msgs__srv__Gstam_Request *)raw_ros_message;
  {  // a
    PyObject * field = NULL;
    field = custom_msgs__msg__pose3_d__convert_to_py(&ros_message->a);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "a", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // b
    PyObject * field = NULL;
    field = custom_msgs__msg__pose3_d__convert_to_py(&ros_message->b);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "b", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // c
    PyObject * field = NULL;
    field = custom_msgs__msg__pose3_d__convert_to_py(&ros_message->c);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "c", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // d
    PyObject * field = NULL;
    field = custom_msgs__msg__pose3_d__convert_to_py(&ros_message->d);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "d", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // e
    PyObject * field = NULL;
    field = custom_msgs__msg__pose3_d__convert_to_py(&ros_message->e);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "e", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // f
    PyObject * field = NULL;
    field = custom_msgs__msg__pose3_d__convert_to_py(&ros_message->f);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "f", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // g
    PyObject * field = NULL;
    field = custom_msgs__msg__pose3_d__convert_to_py(&ros_message->g);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "g", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // h
    PyObject * field = NULL;
    field = custom_msgs__msg__pose3_d__convert_to_py(&ros_message->h);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "h", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // i
    PyObject * field = NULL;
    field = custom_msgs__msg__pose3_d__convert_to_py(&ros_message->i);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "i", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // j
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->j);
    {
      int rc = PyObject_SetAttrString(_pymessage, "j", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "custom_msgs/srv/detail/gstam__struct.h"
// already included above
// #include "custom_msgs/srv/detail/gstam__functions.h"

bool custom_msgs__msg__pose3_d__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * custom_msgs__msg__pose3_d__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool custom_msgs__srv__gstam__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[38];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("custom_msgs.srv._gstam.Gstam_Response", full_classname_dest, 37) == 0);
  }
  custom_msgs__srv__Gstam_Response * ros_message = _ros_message;
  {  // final
    PyObject * field = PyObject_GetAttrString(_pymsg, "final");
    if (!field) {
      return false;
    }
    if (!custom_msgs__msg__pose3_d__convert_from_py(field, &ros_message->final)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * custom_msgs__srv__gstam__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Gstam_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("custom_msgs.srv._gstam");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Gstam_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  custom_msgs__srv__Gstam_Response * ros_message = (custom_msgs__srv__Gstam_Response *)raw_ros_message;
  {  // final
    PyObject * field = NULL;
    field = custom_msgs__msg__pose3_d__convert_to_py(&ros_message->final);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "final", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
