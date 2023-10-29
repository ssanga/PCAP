class Vehicle:
    """
    Vehicle is a type that describes a machine that help us travel.
    """

    default_tire = 'tire'

    def __init__(self, engine, tires) -> None:
        """
        self is going to represent the instance of the class
        Customizes de initialization of the class
        """
        self.engine = engine
        self.tires = tires

    @classmethod
    def bicycle(cls, tires=None):
        if not tires:
            tires = [cls.default_tire, cls.default_tire]
        return cls(engine= None, tires = tires)
    
    @staticmethod
    def example():
        pass


    def description(self):
        print(f"A vehicle with a {self.engine} engine, and {self.tires} tires")