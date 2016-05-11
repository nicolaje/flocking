from morse.builder.creator import SensorCreator

class Flockingsensor(SensorCreator):
    _classpath = "flocking.sensors.FlockingSensor.Flockingsensor"
    _blendname = "FlockingSensor"

    def __init__(self, name=None):
        SensorCreator.__init__(self, name)

