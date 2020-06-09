### importing a class from a module

from chapter_9.car_9dot2 import Car # if you get an importError, restart VSCode

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()





### importing multiple classes from a module

from chapter_9.car_9dot2 import Car, ElectricCar

my_beetle = Car('volkswage', 'beetle', 2006)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2020)
print(my_tesla.get_descriptive_name())




### importing an entire module
import chapter_9.car_9dot2


# different way to make an instance!
myb2 = chapter_9.car_9dot2.Car('volkswage', 'b', 2006)
print(myb2.get_descriptive_name())

myt2 = chapter_9.car_9dot2.ElectricCar('t', 'roadster', 2020)
print(myt2.get_descriptive_name())



# from car_9dot2 import *
# unused import battery from wildcard ie we import Battery, but we never use.
myb3 = Car('vw', 'b3', 2006)
print(myb3.get_descriptive_name())

myt3 = ElectricCar('t', 'roadster', 2020)
print(myt3.get_descriptive_name())


### importing a module into a module
## NO NEED TO COMMENT electriccar() and battery() OUT FROM CAR_9DOT2

from chapter_9.car_9dot2 import Car
from chapter_9.electric_car_9dot2 import ElectricCar # MAKE SURE TO IMPORT CAR IN ELECTRICCAR.PY!!!

mb4 = Car('VW' , 'b4', 2024)
print(mb4.get_descriptive_name())

myt3 = ElectricCar('t', 'roadster', 2020)
print(myt3.get_descriptive_name())
