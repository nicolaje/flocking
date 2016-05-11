#! /usr/bin/env morseexec

from morse.builder import *

robot = Morsy()

pose=Pose()
pose.add_interface('socket')
pose.frequency(1)
robot.append(pose)
robot.add_default_interface('socket')

env = Environment('indoors-1/boxes', fastmode = False)
env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])
