#! /usr/bin/env morseexec

from morse.builder import *
from flocking.builder.sensors import Flockingsensor
from random import uniform, gauss
from math import pi

for i in range(1,30):
    robot = ATRV('robot')
    AbstractComponent.close_context()

    flockSensor=Flockingsensor()
    flockSensor.frequency(2)
    flockSensor.add_interface('socket')
    #flockSensor.add_stream('moos','flocking.sensors.FlockingNotifier.FlockingNotifier',moos_port=9000+i)
    robot.append(flockSensor)

    differential_actuator=MotionVW()
    differential_actuator.add_interface('socket')
    differential_actuator.frequency(10)
    robot.append(differential_actuator)

    robot.translate(x=gauss(0,10),y=gauss(0,10))
    robot.rotate(z=uniform(0,2*pi))
    robot.add_default_interface('socket')

# set 'fastmode' to True to switch to wireframe mode
env = Environment('flat.blend', fastmode = False)
env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])
