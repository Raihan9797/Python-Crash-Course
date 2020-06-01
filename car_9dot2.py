# module level docstring
"""A class that can be used to represent a car"""

class Car():

    def __init__(self, make, model, year):
        """initialize attributes to desc a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return formatted desc name. Different from just printing!!"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print car's mileage"""
        print('this car has ' + str(self.odometer_reading) + ' miles on it')
    
    def update_odometer(self, mileage):
        """set odometer to given val. NEW MILEAGE CAN'T BE LESS THAN THE OLD READING!"""
        if (mileage < self.odometer_reading):
            print('you cannot decrease the mileage on a car!')
        else:
            self.odometer_reading = mileage
    
    def increment_odometer(self, miles):
        """Add given miles to odo reading"""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print("gas tank filled")

# commented out for section 9.3

#class ElectricCar(Car):
    #"""Represents aspects of a car, specific to electric vehicles"""
    #def __init__(self, make, model, year):
        #"""
        #Intialize attrib of the parent class.
        #Then initialize the attributes specific to electric cars
        #"""
        #super().__init__(make, model, year)
        #self.battery = Battery() # new attrib
    #
    #def fill_gas_tank(self):
        #print("THIS CAR DOESN'T HAVE A GAS TANK")



#class Battery():
    #"""modelling a car battery"""
    #def __init__(self, battery_size=70):
        #self.battery_size = battery_size
    #
    #def describe_battery(self):
        #"""Print statement describing battery size"""
        #print("This car has a " + str(self.battery_size) + "-kWh battery.")
    #
    #def get_range(self):
        #if self.battery_size == 70:
            #range =240
        #elif self.battery_size == 80:
            #range =270
        #else:
            #range = 333
        #msg = 'this car can go approx ' + str(range)
        #msg += ' miles on full charge'
        #print(msg)
    #
    #def upgrade_battery(self):
        #self.battery_size = 85