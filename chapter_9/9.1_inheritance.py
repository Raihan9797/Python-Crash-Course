### inheritance

class Car():

    def __init__(self, make, model, year):
        """initialize attributes to desc a car"""
        self.make = make
        self.model = model
        self.year = year
        # defaulted to 0 as new cars have no mileage!
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return formatted desc name. Different from just printing!!"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print car's mileage"""
        print('this car has ' + str(self.odometer_reading) + ' miles on it')
    
    # new method 1
    def update_odometer(self, mileage):
        """set odometer to given val. NEW MILEAGE CAN'T BE LESS THAN THE OLD READING!"""
        # updated method
        if (mileage < self.odometer_reading):
            print('you cannot decrease the mileage on a car!')
        else:
            self.odometer_reading = mileage
    
    # new method 2
    def increment_odometer(self, miles):
        """Add given miles to odo reading"""
        self.odometer_reading += miles
    
    ## NO ARGUMENT --> STATIC ie can be called as Car.fill_gas_tank!
    def fill_gas_tank(self):
        print("gas tank filled")


## PARENT MUST APPEAR BEFORE THE CHILD
## PARENT MUST BE INSIDE THE CHILD ie ElectricCar(Car)
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Intialize attrib of the parent class.
        Then initialize the attributes specific to electric cars
        """
        super().__init__(make, model, year)

        # battery_size updated to use Battery class
        self.battery = Battery() # new attrib
    
    ## method moved to Battery Class
    # def describe_battery(self):
        # """Print statement describing battery size"""
        # print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        print("THIS CAR DOESN'T HAVE A GAS TANK")

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.get_descriptive_name()


## Define attributes and methods for Child Class
## new attribute battery_size and describe_battery() added.

my_tesla2 = ElectricCar('tesla', 'MODEL 2', 2016)
my_tesla2.get_descriptive_name()
my_tesla2.describe_battery()


## overriding parent methods eg. fill_gas_tank()
## electric cars don't have gas tanks!
## added fill_gas_tank() to Car parent class

c = Car('bmw', 'model bla', 2020)
c.fill_gas_tank()
ec = ElectricCar('tsla', 'model m', 2020)
ec.fill_gas_tank()

# Car.fill_gas_tank()


## instances as attributes ie CLASSES IN ANOTHER CLASS. ElectricCar HAS A Battery!
# do this when you have to many attributes; you can break a class up into smaller classes.

class Battery():
    """modelling a car battery"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    # method moved to Battery Class
    def describe_battery(self):
        """Print statement describing battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 70:
            range =240
        elif self.battery_size == 80:
            range =270
        msg = 'this car can go approx ' + str(range)
        msg += ' miles on full charge'
        print(msg)


mt3 = ElectricCar('tes', 'M3', 2033)


## THIS TELLS PYTHON TO FIND THE BATTERY ATTRIBUTE IN MT3 AND CALL THE METHOD DESCRIBE_BATTERY() IN THE ATTRIBUTE
mt3.battery.describe_battery()



## making a separate class allows us to add more functions without cluttering ElectricCar Class!
# add get_range()
mt4 = ElectricCar('tes', 'M3', 2033)
mt4.battery.get_range()

## modelling real world objects
'''
basically, you might have to change methods(), create new classes and attributes as you go along. But that's to be expected.
'''

## 9.6 ice cream stand (using restaurant class from 9.4)
class Restaurant2():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.num_served = 0
    

    def describe_restaurant(self):
        print(self.restaurant_name + " sells " + self.cuisine_type +" food.")

    
    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")
    
    def set_number_served(self, num):
        if num < self.num_served:
            print("you can't unserve people...")
        else:
            self.num_served = num
    
    def increment_num_served(self, inc):
        if inc < 0:
            print("you can't unserve people...")
        else:
            self.num_served += inc 

class IceCreamStand(Restaurant2):
    def __init__(self, rn, cuisine, flavors):
        super().__init__(rn, cuisine) # no need for self
        self.flavors = flavors 
    
    def get_flavors(self):
        print(self.restaurant_name + "'s ice cream flavors:")
        for f in self.flavors:
            print('- ' + f)

ics = IceCreamStand('ben n jerrys', 'ice cream', ['flav1', 'flav2', 'flav 31'])
ics.get_flavors()



## 9.7 Admin using 9.5 user class
class User:

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        # wanted to do a boolean. but describe() makes it tedious
        # self.is_boy = is_boy
    
    def describe_user(self):
        print(self.first_name + " " + 
              self.last_name.title() + 
              ' is a ' + str(self.age) + 'year old ' + self.gender)
    
    def greet_user(self):
        print('yo ' + self.first_name)

class Admin(User):

    def __init__(self, first_name, last_name, age, gender, priviliges):
        super().__init__(first_name,last_name,age,gender)
        self.priviliges = priviliges
    
    def show_priviliges(self):
        for p in self.priviliges:
            print(p)


# 9.8 privileges
class Privilege():

    def __init__(self, priviliges):
        self.privileges = priviliges
    
    def show_priviliges(self):
        for p in self.privileges:
            print(p)


class User2:

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        # wanted to do a boolean. but describe() makes it tedious
        # self.is_boy = is_boy
    
    def describe_user(self):
        print(self.first_name + " " + 
              self.last_name.title() + 
              ' is a ' + str(self.age) + 'year old ' + self.gender)
    
    def greet_user(self):
        print('yo ' + self.first_name)

class Admin2(User2):

    def __init__(self, first_name, last_name, age, gender, privileges):
        super().__init__(first_name,last_name,age,gender)
        self.privileges = Privilege(privileges) 

aliA = Admin2('ali', 'abdaal', 32, 'male', ['can do surgeries', 'can teach you things', 'free skillshare access'])

aliA.privileges.show_priviliges()
aliA.describe_user()
aliA.greet_user()
# aliA.show_priviliges() # error






## 9.9 battery upgrade
class Car2():

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





class ElectricCar2(Car2):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Intialize attrib of the parent class.
        Then initialize the attributes specific to electric cars
        """
        super().__init__(make, model, year)

        self.battery = Battery2() # new attrib
    
    def fill_gas_tank(self):
        print("THIS CAR DOESN'T HAVE A GAS TANK")


class Battery2():
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

tsla99 = ElectricCar2('tesla', 'model 99', 2222)

tsla99.battery.get_range()

tsla99.battery.upgrade_battery()
tsla99.battery.battery_size

tsla99.battery.get_range() #unboundlocalerror?






        