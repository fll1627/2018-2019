#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.sound import Sound
from threading import Thread
from time import sleep
wheelRadius = 3
robotRadius = 7.7
def turn(degrees, speed, wheelRadius, robotRadius, port1, port2):
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
def move(distance, speed, wheelRadius, port1, port2):
	wheelPerimeter = wheelRadius * 3.14 * 2
	moveDistance = distance / wheelPerimeter
	motors = MoveTank(port1, port2)
	motors.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed), moveDistance)
def waitStart():
	speaker = Sound()
	speaker.speak('ready to run')
	touch = TouchSensor(INPUT_1)
	while not touch.is_pressed:
		sleep(0.1)
	mainThread = Thread(target=main)
	mainThread.start()



def main():
	global wheelRadius
	global robotRadius
	# Get to position of M03
	move(83, 50, wheelRadius, OUTPUT_B, OUTPUT_C)
	turn(-90, 30, wheelRadius, robotRadius, OUTPUT_B, OUTPUT_C)
	move(25, -20, wheelRadius, OUTPUT_B, OUTPUT_C)
	move(50, 50, wheelRadius, OUTPUT_B, OUTPUT_C)
	turn(-90, 30, wheelRadius, robotRadius, OUTPUT_B, OUTPUT_C)
	
	# Move grabber arm down
	arm = MediumMotor(OUTPUT_A)
	arm.on_for_degrees(-20, 170)
	
	# Move back and scoop up piece
	move(10, -20, wheelRadius, OUTPUT_B, OUTPUT_C)
	arm.on_for_degrees(-15, 60)
	turn(90, 30, wheelRadius, robotRadius, OUTPUT_B, OUTPUT_C)
	move(40, -50, wheelRadius, OUTPUT_B, OUTPUT_C)
	turn(90, 30, wheelRadius, robotRadius, OUTPUT_B, OUTPUT_C)
	move(70, -50, wheelRadius, OUTPUT_B, OUTPUT_C)
	
waitStart()