### creating and using a class

class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")
    

    def roll_over(self):
        """Simulate dog rolling over in response to a command"""
        print(self.name.title() + " rolled over!")

'''
This has some similarities to Java. 
** __init__() is kinda like a constructor

__init__() and self
'self' is required and must come FIRST in the definition
every method call associated with a class automatically passes self, which is a reference to the instance itself

** this makes it like 'this' in Java! **

when we make a Dog instance, self if passed automatically, so we just have to pass 'name' and 'age' arguments

self.name = name SAME AS this.name = name in Java!
'''


## Making an instance from a class
my_dog = Dog('willie', 6)

print("my dog's name is " + my_dog.name.title())
print("my dog is " + str(my_dog.age) + ' yrs old.')


## calling methods ie functions!
my_dog.sit()
my_dog.roll_over()

## multiple instances
your_dog = Dog('lucy', 3)
your_dog.sit()

## 9.1 Restaurant

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    

    # YOU NEED TO USE SELF.RESTAURANT_NAME
    # OTHERWISE, NAMEERROR WHEN YOU CALL THE FUNCTION AS RESTAURANT_NAME IS NOT DEFINED!
    def describe_restaurant(self):
        # print(restaurant_name + " sells " + cuisine_type +" food.")
        print(self.restaurant_name + " sells " + self.cuisine_type +" food.")

    
    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")


hwangs = Restaurant("Hwang's", 'korean')
# call attributes. NO () IS REQUIRED
print(hwangs.restaurant_name + " is found in NUS and sells " + hwangs.cuisine_type + " food.")
# call methods. () IS REQUIRED
hwangs.describe_restaurant()
hwangs.open_restaurant()

# 9.2 3 restaurants
wacow = Restaurant('wa cow', 'donburi')
twothreefivenine = Restaurant('2359', 'fusion')
supersnack = Restaurant('super snack', 'chicken sandwich')

wacow.describe_restaurant()
twothreefivenine.describe_restaurant()
supersnack.describe_restaurant()

# 9.3 users
# ** NO NEED FOR USER()??? ***
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

kw = User('kanye', 'west', 45, 'male')
kw.describe_user()
kw.greet_user()




### Working with classes and instances

## setting default vals for an attribute ie odometer_reading
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



my_car = Car('audi', 'a4', '2016')
my_car.get_descriptive_name()
print(my_car.get_descriptive_name())

my_car.read_odometer()


### modifying attribute values

## modify directly
my_car.odometer_reading = 23
my_car.read_odometer()


## modify through a method
# added update_odometer to the Car class.

# ** THE INSTANCE OF CAR YOU CREATED BEFORE THE UPDATE_ODOMETER() DOES NOT HAVE THE METHOD!!! ie the instance is not updated when you update the class!
my_car.update_odometer(47)

my_car2 = Car('bmw', 's class', 2018)
my_car2.read_odometer()
my_car2.update_odometer(47)
my_car2.read_odometer()

'''
we can improve the method by adding logic to make sure that no one can decrease the mileage!!
'''
my_car3 = Car('XYZ', 'model 3', 2069)
my_car3.read_odometer()
my_car3.update_odometer(47)
my_car3.read_odometer()
my_car3.update_odometer(30)
my_car3.read_odometer()


## increnting attribute value through method
# new method increment_odometer() added to Car class..
my_car4 = Car('ABC', 'model abc', 2020)
my_car4.read_odometer()
my_car4.increment_odometer(40)
my_car4.read_odometer()


## 9.4 number served using 9.1
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

hwangs = Restaurant2('hwangs', 'korean')

print(hwangs.num_served)
hwangs.num_served = 4
print(hwangs.num_served)
hwangs.set_number_served(3)
print(hwangs.num_served)
hwangs.set_number_served(7)
print(hwangs.num_served)
hwangs.increment_num_served(3)
print(hwangs.num_served)

# 9.5 login attempts
class User2():

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        # wanted to do a boolean. but describe() makes it tedious
        # self.is_boy = is_boy
        self.login_attempts = 0
    
    def describe_user(self):
        print(self.first_name + " " + 
              self.last_name.title() + 
              ' is a ' + str(self.age) + 'year old ' + self.gender)
    
    def greet_user(self):
        print('yo ' + self.first_name)
    
    # dont forget to put self in the arguments!!
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

snoop = User2('snoop', 'dog', 50, 'male')

print(snoop.login_attempts)

snoop.increment_login_attempts()
print(snoop.login_attempts)

snoop.reset_login_attempts()
print(snoop.login_attempts)
