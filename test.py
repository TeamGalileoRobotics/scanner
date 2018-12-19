#!/usr/bin/env python
import time
import nxt.locator
from nxt.sensor import *
from nxt.motor import *

def run():
	MOTOR.turn(-20, 5000)

BRICK = nxt.locator.find_one_brick()
MOTOR = Motor(BRICK, PORT_A)

run()