#! /usr/bin/env morseexec

from morse.builder import *
from flocking.builder.sensors import Flockingsensor
from math import pi

# TODO: you must instantiate 30 ATRV robot in random states. A single instantiation is given as an example.

robot = ATRV('robot')

flockSensor=Flockingsensor()
flockSensor.frequency(2)
flockSensor.add_interface('socket')

# When you will be ready with MOOSDB running in the background, add your MOOS interface
#flockSensor.add_stream('moos','flocking.sensors.FlockingNotifier.FlockingNotifier',moos_port=9001)
robot.append(flockSensor)

differential_actuator=MotionVW()
differential_actuator.add_interface('socket')
differential_actuator.frequency(10)
robot.append(differential_actuator)

robot.translate(x=0,y=1)
robot.rotate(z=pi/2)
robot.add_default_interface('socket')

# set 'fastmode' to True to switch to wireframe mode
env = Environment('flat.blend', fastmode = False)
env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])
