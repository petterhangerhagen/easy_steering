# easy_steering
Easy steering

```
cd catkin_ws/src
git clone https://github.com/petterhangerhagen/easy_steering.git
chmod +x ~/catkin_ws/src/easy_steering/scripts/easy_steering_client.py
```

Launching

ros_adapter needs to match the virtual machine.
ros_clients needs to match the host.

```
source ~/catkin_ws/devel/setup.bash
roslaunch ~/catkin_ws/src/ros_scenario/launch/launch_njord_stack.launch
```

```
source ~/catkin_ws/devel/setup.bash
roslaunch ~/catkin_ws/src/easy_steering/launch/launch_easy_steering.launch
```

```
cd catkin_ws/src/easy_steering/scripts
nano forces.txt
```
