from car_9dot2 import Car


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Intialize attrib of the parent class.
        Then initialize the attributes specific to electric cars
        """
        super().__init__(make, model, year)

        self.battery = Battery() # new attrib
    
    def fill_gas_tank(self):
        print("THIS CAR DOESN'T HAVE A GAS TANK")


class Battery():
    """modelling a car battery"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print statement describing battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 70:
            range =240
        elif self.battery_size == 80:
            range =270
        else:
            range = 333
        msg = 'this car can go approx ' + str(range)
        msg += ' miles on full charge'
        print(msg)
    
    def upgrade_battery(self):
        self.battery_size = 85