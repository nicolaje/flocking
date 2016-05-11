import logging; logger = logging.getLogger("morse." + __name__)
import pymoos.MOOSCommClient
from morse.middleware.moos import AbstractMOOS
from morse.core import blenderapi

class FlockingNotifier(AbstractMOOS):
    def default(self, ci='unused'):
#        cur_time=pymoos.MOOSCommClient.MOOSTime()
#        # post the simulation time so that it can be synced to MOOSTime
#        self.m.Notify('actual_time', blenderapi.persistantstorage().current_time, cur_time)
#        for key, value in self.data['distances'].items():
#        self.m.Notify(str(key), value, cur_time)
        
        cur_time=pymoos.MOOSCommClient.MOOSTime()
        # Notify the MOOSDB of the robot state
        state=self.data['state']
        self.m.Notify("state",",".join(map(str,state)),cur_time)
        # Go through all the states of the other robots measured
        # by the sensor and serialize them in a big string
        res=[]
        for otherState in self.data['states']:
          res.append(",".join(map(str,otherState)))
          # Publish it in the MOOSDB
          self.m.Notify("states", ",".join(res), cur_time)
