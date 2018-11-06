#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev.ev3 import TouchSensor
from threading import Thread
from ev3dev2.sound import Sound
from time import sleep

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
face = LargeMotor(OUTPUT_D)
touch = TouchSensor('in2')
sound = Sound()
sound.speak('starting')
global stopper
stopper = 8

def program1():
	for i in range(0, 16):
		if touch.value():
			tank_drive.on(SpeedPercent(50), SpeedPercent(50))
		else:
			tank_drive.off()
		sleep(0.5)
t1 = Thread(target=program1)

def program2():
	for i in range(0, 4):
		face.on_for_seconds(SpeedPercent(20), 1)
		face.on_for_seconds(SpeedPercent(-20), 1)
t2 = Thread(target=program2)

def program3():
	while True:
		if stopper <= 0:
			break
		#sound.speak(str(stopper))
t3 = Thread(target=program3)

def program4():
	while True:
		sleep(1)
		stopper = stopper - 1
		sound.speak(str(stopper))
		if stopper <= 0:
			break
t4 = Thread(target=program4)

t1.start()
t2.start()
t3.start()
t4.start()