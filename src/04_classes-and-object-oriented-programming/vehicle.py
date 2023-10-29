class Vehicle:
    """
    Vehicle is a type that describes a machine that help us travel.
    """

    def __init__(self, distance_traveled = 0, unit = 'miles') -> None:
        """
        self is going to represent the instance of the class
        Customizes de initialization of the class
        """
        self.distance_traveled = distance_traveled
        self.unit = unit

    # @classmethod
    # def bicycle(cls, tires=None):
    #     if not tires:
    #         tires = [cls.default_tire, cls.default_tire]
    #     return cls(engine= None, tires = tires)
    
    @staticmethod
    def example():
        pass


    def description(self):
        return f"A {self.__class__.__name__} that has travel {self.distance_traveled} {self.unit}"