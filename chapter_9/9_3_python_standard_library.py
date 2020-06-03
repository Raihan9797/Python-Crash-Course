'''
Basically, Python has some standard libraries that you can use to make your life easier
'''

from collections import OrderedDict
'''
ordered dict follows the order in which you inputted the data!
'''

# CREATING AN ORDERED DICT:
fav_languages = OrderedDict()

fav_languages['jen'] = 'python'
fav_languages['sarah'] = 'c'
fav_languages['edward'] = 'ruby'
fav_languages['phil'] = 'python'


for name, lang in fav_languages.items():
    print(name.title() + "'s fav lang is " + lang)

### SEE THE DIFF
fav_l = {}
fav_l['jen'] = 'python'
fav_l['sarah'] = 'c'
fav_l['edward'] = 'ruby'
fav_l['phil'] = 'python'

# NOT PRINTED IN THE SAME ORDER!!
for name, lang in fav_l.items():
    print(name.title() + "'s fav lang is " + lang)





## ex 9.14 dice
from random import randint
x = randint(1, 6)
x

class Die():

    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_dice(self):
        return randint(1, self.sides)


tensides = Die(10)
tensides.roll_dice()

twentysides = Die(20)
twentysides.roll_dice()



### Styling Classes
'''
1. Classes should be written in CamelCase*********

2. every class should have a docstring immediately after the class defo eg
Class class_name():
""" this is the docstring"""

3. don't use blank lines excessively

4. import only what you need
'''




