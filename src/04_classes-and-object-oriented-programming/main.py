from bicycle import Bicycle
from vehicle import Vehicle

civic = Vehicle(100, 'miles')
print(civic.description())

bike = Bicycle([1,2], 2, 'miles')
print(bike.description())