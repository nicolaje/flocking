#! /usr/bin/env python3

import sys
from pymorse import Morse

def callback(data):
    print("I received: "+str(data))

with Morse() as simu:
    simu.robot.pose.subscribe(callback)
    simu.sleep(10)
