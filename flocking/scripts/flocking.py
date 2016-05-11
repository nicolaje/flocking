#! /usr/bin/env python3

import sys
from pymorse import Morse
import numpy as np
from scipy import signal

# This is a helper class, it is attached to each robot to handle its Flockingsensor data and send inputs to its MotionVW
class RobotController:

    def __init__(self,robot,alpha,beta,gamma):
        self.robot=robot
        self.alpha=alpha
        self.beta=beta
        self.gamma=gamma

        self.robot.flockSensor.subscribe(self.sensorSubscriber)

    def sensorSubscriber(self,data):
        u=0

        print("I received: "+str(data)) # Remove me

        state=np.array(data['state'])
        states = np.asarray(data['states'])

        for s in states:
            pass # That's your job!
            
        # Here we send the input you computed to the MotionVW actuator of the robot.
        self.actuatorPublisher(u)

    # Here, the input
    def actuatorPublisher(self,u):
        self.robot.differential_actuator.publish({'v':1,'w':u})

with Morse() as simu:
    alpha=1
    beta=20
    gamma=1

    for robot in [getattr(simu, attr) for attr in dir(simu) if attr.startswith('robot')]:
        try:
            RobotController(robot,alpha,beta,gamma)
        except:
            pass

    simu.sleep(10)
