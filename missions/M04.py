#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.senser import INPUT_1
from threading import Thread
waitStart();
def turnInDegrees(degrees, speed, wheelRadius, robotRadius, port1, port2):
	robotPerimeter = (robotRadius * 3.14 * 2)
	amountPerDegree = robotPerimeter / 360
	amountDegrees = amountPerDegree * degrees
	wheelPerimeter = wheelRadius * 3.14 * 2
	distance = amountDegrees / wheelPerimeter
	motors = MoveTank(port1, port2)
	if degrees < 0:
		motors.on_for_rotations(SpeedPercent(speed * -1), SpeedPercent(speed), abs(distance))
	else:
		motors.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed * -1), distance)
def moveInCentimeters(distance, speed, wheelRadius, port1, port2):
	wheelPerimeter = wheelRadius * 3.14 * 2
	moveDistance = distance / wheelPerimeter
	motors = MoveTank(port1, port2)
	motors.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed), moveDistance)
def waitStart():
	touch = TouchSensor(INPUT_1)
	while not touch.is_pressed:
		sleep(0.1)
	mainThread = Thread(target=main)
	mainThread.start()



def main():
	moveInCentimeters(80, 50, 2.6, OUTPUT_A, OUTPUT_B)
	turnInDegrees(-90, 30, 2.6, 5.5, OUTPUT_A, OUTPUT_B)
	moveInCentimeters(6, 20, 2.6, OUTPUT_A, OUTPUT_B)
	moveInCentimeters(60, 50, 2.6, OUTPUT_A, OUTPUT_B)