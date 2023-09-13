// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_msgs:msg/Pose3DStamped.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSGS__MSG__DETAIL__POSE3_D_STAMPED__STRUCT_H_
#define CUSTOM_MSGS__MSG__DETAIL__POSE3_D_STAMPED__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'pose'
#include "custom_msgs/msg/detail/pose3_d__struct.h"

/// Struct defined in msg/Pose3DStamped in the package custom_msgs.
typedef struct custom_msgs__msg__Pose3DStamped
{
  custom_msgs__msg__Pose3D pose;
  double time;
} custom_msgs__msg__Pose3DStamped;

// Struct for a sequence of custom_msgs__msg__Pose3DStamped.
typedef struct custom_msgs__msg__Pose3DStamped__Sequence
{
  custom_msgs__msg__Pose3DStamped * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_msgs__msg__Pose3DStamped__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_MSGS__MSG__DETAIL__POSE3_D_STAMPED__STRUCT_H_
