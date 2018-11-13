#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev.ev3 import TouchSensor, INPUT_2
from threading import Thread
from ev3dev2.sound import Sound
from time import sleep

wheelsMotors = MoveTank(OUTPUT_A, OUTPUT_B)
mouthMotor = LargeMotor(OUTPUT_D)
touchSensor = TouchSensor(INPUT_2)
speaker = Sound()

finished = False

speaker.speak('initializing mouth motor')

def runTimer():
	timer = 8
	global finished
	while timer > 0:
		sleep(1)
		timer = timer - 1
	finished = True
timerThread = Thread(target=runTimer)
timerThread.start()

def runWheels():
	while finished == False:
		if touchSensor.value():
			wheelsMotors.on(SpeedPercent(50), SpeedPercent(50))
		else:
			wheelsMotors.off()
		sleep(0.1)
	wheelsMotors.off()
wheelsThread = Thread(target=runWheels)
wheelsThread.start()

def runMouth():
	while finished == False:
		mouthMotor.on_for_seconds(SpeedPercent(-20), 1)
		mouthMotor.on_for_seconds(SpeedPercent(20), 1)
mouthThread = Thread(target=runMouth)
mouthThread.start()

def runSpeak():
	while finished == False:
		sleep(0.5)
		speaker.speak('woof woof')
speakThread = Thread(target=runSpeak)
speakThread.start()