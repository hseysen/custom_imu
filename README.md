# Custom IMU
This repository contains the ROS package that I have created to read IMU data from a 6-DOF IMU sensor that I have connected to an Arduino board that has been programmed to output the IMU data to the serial output.

# Building
```bash
mkdir -p ~/cusimu_ws/src
cd ~/cusimu_ws/src
git clone https://github.com/hseysen/custom_imu.git
cd ..
catkin_make
```

# Running
Make sure to edit [the launch file](https://github.com/hseysen/custom_imu/blob/main/src/imu.launch) with your serial port and baud rates.
```bash
source ~/cusimu_ws/devel/setup.bash
roslaunch custom_imu imu.launch
```

# IMU format
The IMU data format that I have used may not match other custom IMU data formats, so make sure to edit [Line 20-21](https://github.com/hseysen/custom_imu/blob/main/src/imu.py) to match the data format.

# Orientation
My IMU did not have orientation outputs since it does not have a magnetometer, if yours does, make sure to include it as well after [Line 31](https://github.com/hseysen/custom_imu/blob/main/src/imu.py), or wherever you desire.
