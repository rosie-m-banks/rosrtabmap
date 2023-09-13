cmake_minimum_required(VERSION 3.8)
project(vision)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(custom_msgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(wpilib REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)

add_executable(networkTables src/networkTables.cpp)
add_executable(rioPub src/rioPublish.cpp)
add_executable(rioGet src/rioGetter.cpp)

target_link_libraries(rioPub ntcore)
target_link_libraries(rioGet ntcore)
ament_target_dependencies(networkTables rclcpp std_msgs geometry_msgs custom_msgs tf2 tf2_ros)
ament_target_dependencies(rioGet rclcpp std_msgs geometry_msgs custom_msgs)
ament_target_dependencies(rioPub rclcpp std_msgs geometry_msgs custom_msgs)

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
