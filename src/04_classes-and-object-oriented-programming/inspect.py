from amphibious import AmphibiousVehicle
from vehicle import Vehicle
from bicycle import Bicycle
from boat import Boat

print(AmphibiousVehicle.__bases__)
print(Vehicle.__subclasses__())
print(Bicycle.__subclasses__())
print(dir(AmphibiousVehicle))
print(hasattr(Boat, 'boat_type'))
boat = Boat()
print(hasattr(boat, 'boat_type'))
print(issubclass(Boat, Vehicle))
print(issubclass(Boat, AmphibiousVehicle))