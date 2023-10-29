from amphibious import AmphibiousVehicle
from boat import Boat
from car import Car
from bicycle import Bicycle
from vehicle import Vehicle

civic = Vehicle(100, 'miles')
print(civic.description())

bike = Bicycle([1,2], 2, 'miles')
print(bike.description())

prius = Car('4-cylinder',None, 98_365, 'kilometers')
print(prius.description())

zodiac = Boat(boat_type='plastic')
print(zodiac.description())

water_car = AmphibiousVehicle('4-cylinder')
water_car.travel(10, 15)
print(water_car.description())
print(water_car.distance_traveled)
# Method resolution order
print(AmphibiousVehicle.__mro__)