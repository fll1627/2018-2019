#!/usr/bin/env python3
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
sound = Sound()
sound.speak('starting')
tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50))