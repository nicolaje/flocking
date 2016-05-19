#! /usr/bin/env python3

import sys
from pymorse import Morse
import numpy as np
from scipy import signal

class RobotController:

    def __init__(self,robot,alpha,beta,gamma):
        self.robot=robot
        self.alpha=alpha
        self.beta=beta
        self.gamma=gamma

        self.robot.flockSensor.subscribe(self.sensorSubscriber)

    def sensorSubscriber(self,data):
        u=0

        state=np.array(data['state'])
        states = np.asarray(data['states'])

        H=np.zeros((2,2*states.shape[0]))

        k=0

        for s in states:
            v=self.gamma*np.array([np.cos(s[2]),np.sin(s[2])])
            H[:,k]=v

            k=k+1
            dp=state[0:2]-s[0:2]
            v=-self.alpha*dp+self.beta*dp/(np.linalg.norm(dp)**3)
            v=v/np.linalg.norm(v)
            if np.any(np.isnan(v)):
                v[:]=0
            H[:,k]=v
            k=k+1

        Hbar=np.mean(H,1)

        u=((float(np.angle(Hbar[0]+Hbar[1]*1j))-state[2]+np.pi)%(2*np.pi))-np.pi
        if np.isnan(u):
            u=0
        self.actuatorPublisher(u)


    def actuatorPublisher(self,u):
        self.robot.differential_actuator.publish({'v':1,'w':u})

with Morse() as simu:
    alpha=1
    beta=20
    gamma=1

    for robot in [getattr(simu, attr) for attr in dir(simu) if attr.startswith('robot')]:
        RobotController(robot,alpha,beta,gamma)

    simu.sleep(10)
