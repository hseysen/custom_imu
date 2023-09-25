#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
import serial
from std_msgs.msg import Header


def imu_publisher():
	rospy.init_node("custom_imu")
	imu_pub = rospy.Publisher("imu_data", Imu, queue_size=1)
	
	PARAM_SERIAL_PORT = rospy.get_param("~serial_port", "/dev/ttyACM0")
	PARAM_BAUD_RATE = rospy.get_param("~baud_rate", 115200)

	serial_port = serial.Serial(PARAM_SERIAL_PORT, PARAM_BAUD_RATE)

	while not rospy.is_shutdown():
		# My current data comes as () Ax Ay Az Gx Gy Gz
		data = serial_port.readline()
		Ax, Ay, Az, Gx, Gy, Gz = map(float, data[2:].strip().split())

		imu_msg = Imu()
		imu_msg.header = Header()
		imu_msg.header.stamp = rospy.Time.now()
		imu_msg.angular_velocity.x = Gx
		imu_msg.angular_velocity.y = Gy
		imu_msg.angular_velocity.z = Gz
		imu_msg.linear_acceleration.x = Ax
		imu_msg.linear_acceleration.y = Ay
		imu_msg.linear_acceleration.z = Az

		# Publish
		imu_pub.publish(imu_msg)


if __name__ == "__main__":
	try:
		imu_publisher()
	except rospy.ROSInterruptException:
		pass
