import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.sensor


from morse.core.services import service, async_service
from morse.core import status
from morse.helpers.components import add_data, add_property
from morse.core import blenderapi
from math import pi

class Flockingsensor(morse.core.sensor.Sensor):

    _name = "Flockingsensor"
    _short_desc = "This sensors measures the state of its carrier and of all the surrounding robots"

    add_data('state',[],'list','Vecteur d etat du robot: x,y,theta')
    add_data('states', [], 'list', 'Vecteurs d etat des autres robots: [(x1,y1,theta1),...]')

    def __init__(self, obj, parent=None):
        logger.info("%s initialization" % obj.name)
        morse.core.sensor.Sensor.__init__(self, obj, parent)
        logger.info('Component initialized')

    def default_action(self):
        robot = self.robot_parent.bge_object

        self.local_data['state'] = [0,0,0] # ! Fill the vector! Hint: robot.position_3d (powered by MORSE, so does not suffer from a shift in the Yaw)
        self.local_data['states'] = []
        for obj in blenderapi.scene().objects:
            try:
                obj["Robot_Tag"]
                # Skip distance to self
                if robot != obj:
                    self.local_data['states'].append((0,0,0)) # ! Fill the vector! Hint: worldPosition and worldOrientation methods !
            except KeyError:
                pass
