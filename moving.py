#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from threading import Thread
from time import sleep

def turnInDegrees(degrees, speed, wheelRadius, robotRadius, port1, port2):
	robotPerimeter = robotRadius * 3.14 * 2 #29.202
	wheelPerimeter = wheelRadius * 3.14 * 2#16.956
	singleDegree = robotPerimeter / 360#0.104
	rotations = singleDegree / wheelPerimeter
	amountDegrees = rotations * degrees
	print(rotations)
	motors = MoveTank(port1, port2)
	print(amountDegrees)
	motors.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed * -1), amountDegrees)

def moveInCentimeters(distance, speed, wheelRadius, port1, port2):
	wheelPerimeter = wheelRadius * 3.14 * 2
	moveDistance = distance / wheelPerimeter
	motors = MoveTank(port1, port2)
	motors.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed), moveDistance)

turnInDegrees(360, 30, 2.7, 6, OUTPUT_A, OUTPUT_B)
moveInCentimeters(40, 30, 2.7, OUTPUT_A, OUTPUT_B)
sleep(1000)