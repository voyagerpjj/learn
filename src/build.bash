pushd `pwd` > /dev/null
cd `dirname $0`
cd ..
clear
echo "Working Path: "`pwd`
colcon build \
  --symlink-install \
  --event-handlers console_direct+ \
  --cmake-args \
    -DCMAKE_BUILD_TYPE=Release \
  --packages-skip tester time_watcher \
  --parallel-workers 16 
#   --packages-skip livox_ros_driver2\
#   --event-handlers console_direct+ \
popd > /dev/null