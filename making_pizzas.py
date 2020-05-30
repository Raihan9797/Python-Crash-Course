import pizza # import all functions from the module

# x = __import__('8.1_modules_pizza')

pizza.make_pizza(15, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



## importing specific functions
"""
to import just one function:
from module_name import functiona_name

to import multiple functions:
from module_name import function_0, function_1, function_2

this allows you to call the fn without having to write the module name!
"""
from pizza import make_pizza

make_pizza(15, 'pepperoni') # no need to call pizza.make_pizza()
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

## using (as) to give a function an alias
from pizza import make_pizza as mp

mp(15,'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


## using as to give module an alias
import pizza as p

p.make_pizza(15,'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


## importing ALL functions in a module
"""
not reccomended when you are using large modules with alot of files.

also, there might be functions in that module with the same name but do different things, so be careful
"""
from pizza import *

## styling functions
""" make sure to describe exactly what each function does"""

def fn_name(p_0, p_1='default value') # no spaces on '=' sign!!

## PEP 8 reccs code limit of 79 chars per line

## if too many params, ENTER AND TAB TWICE
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    """describe the fn"""
    # function body
)

# import statements in the beginning of a page