def greet_user():
    # below is a DOCSTRING. python looks for this when it generates documentation for the functions in your programs
    """display simple greeting."""

    print("hello")

greet_user()

def greet_user2(username):
    """display simple greeting."""
    print('hello, ' + username.title())

greet_user2('jeSsE')


## positional arguments: follow the order of the arguments!
def describe_pet(pet_type, pet_name):
    """Display info about a pet"""
    print("I have a " + pet_type + ".")
    print("My " + pet_type + "'s name is " + pet_name + ".")

describe_pet('hamster', 'Harry')
describe_pet('Harry', 'hamster') # no error in this case as both are string arguments but doesn't make sense. 


## keyword arguments
describe_pet(pet_type = 'hamster', pet_name ='Harry')
describe_pet(pet_name = 'Harry', pet_type ='hamster') # order changed but still correct!! because we are using KEYWORD ARGUMENTS

## default values
# when writing a function you can define a default val for ea param


# ********* THE DEFAULT VALUE HAS TO BE MOVED TO A THE END OF THE FUNCTION. THE ARGUMENT WITH NO DEFAULT NEEDS TO BE IN FRONT ********
def describe_petVERSION2(pet_name, animal_type = 'dog'):
    """Display info abt a pet"""
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")

describe_petVERSION2('willie') # defaults to a dog! so no need to specify
describe_petVERSION2('harry', 'hamster') # still can specify for other animal types




## argument errors
# 1. wrong number of arguments
# describe_pet()

# 2. wrong type
# describe_petVERSION2(3) # using int vs string.


## 8.3 tshirt
def make_shirt(size, msg):
    print(size + ' shirt made with the message: ' + msg)

make_shirt('small', 'hello world')


## 8.4
def make_shirt2(msg, size = 'large'):
    print(size + ' shirt made with the message: ' + msg)

make_shirt2('i love ny')


## 8.5 cities
def desc_city(city='tokyo', country = 'japan'):
    print(city + " is in " + country)

desc_city('tokyo')
desc_city()





### RETURN VALUES

def get_formatted_name(first_name, last_name):
    """Return a full name formatted"""
    fullname = first_name + " " + last_name
    return fullname.title()

musician = get_formatted_name('jimi', 'hendrix') # storing the returned value
print(musician)

print(get_formatted_name("john", 'lennon'))


## making arguments optional: use default values

# make the middle name optional
def get_formatted_name2(first_name, last_name, middle_name = ''):
    """Return a full name formatted"""
    if middle_name:
        fullname = first_name + " " + middle_name + ' ' + last_name
    else:
        fullname = first_name + " " + last_name
    return fullname.title()

musician = get_formatted_name2('jimi', 'hendrix') # storing the returned value
print(musician)
print(get_formatted_name2("john", 'lennon'))


# if you don't specify, you have to change the position of the middle_name!!
m = get_formatted_name(first_name = 'anna', middle_name='nicole', last_name='smith')
print(m)



## returning a dict
def build_person(firstn, lastn, age=''):
    """Return a dict of info abt the person."""
    person = {'first':firstn, 'last':lastn}
    if age:
        person['age'] = age 
    return person

guitarist = build_person('jimi', 'hendrix')
soldier = build_person('solid', 'snake','29')
print(guitarist)
print(soldier)


## using function with a while loop
def get_formatted_name3(first_name, last_name, middle_name = ''):
    """Return a full name formatted"""
    if middle_name:
        fullname = first_name + " " + middle_name + ' ' + last_name
    else:
        fullname = first_name + " " + last_name
    return fullname.title()

while True:
    print("Please tell me your name: ")
    print("(enter 'q' at any time to quit)")

    fname = input("first name: ")
    if fname == 'q':
        break

    lname = input("last name: ")
    if lname == 'q':
        break

    formatted_name = get_formatted_name(fname, lname)
    print("\n Hello, " + formatted_name + "!")







## 8.7 album
def make_album(title, artist, num_tracks = ''):
    album = {
        'title' : title,
        'artist' : artist,
    }
    if num_tracks:
        album['num_tracks'] = num_tracks # NOTICE HOW THIS USES '=' BUT THE ABOVE ASSIGNMENT OF VALS TO KEYS USES ':'
    return album

dp = make_album('in rock', 'deep purple', '14')
eminem = make_album('MM LP', 'marshall mathers')
md = make_album('rust in peace', 'megadeth')
gnr = make_album('appetite for destruction', 'gnr', '18')



def count_tracks(album):
    if album['num_tracks']:
        return int(album['num_tracks'])
    else:
        return 0

count_tracks(dp)
count_tracks(eminem)
count_tracks(md)
count_tracks(gnr)

# 8.8 user albums
while True:
    print('describe your album')
    print('(press q to end)')

    at = input("album title: ")
    if at == 'q':
        break
    
    an = input("artist name: ")
    if an == 'q':
        break
    
    alb = make_album(at, an)
    print(alb)


### passing a list
def greet(names):
    """greets ea user in a list"""
    for name in names:
        print("hi " + name + "!")

ns = ['tom', 'dick', 'harry', 'bob']
greet(ns)


## modify list in a fn

# start with designs that need to be printed
unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
completed = []

# simulate printing; move each design to completed afted printing
while unprinted:
    curr_design = unprinted.pop()
    print("printing " + curr_design)
    completed.append(curr_design)

# display completed models
print('\n The following models have been printed:')
for c in completed:
    print(c)





## THIS CAN BE REORGANIZED USING FUNCTIONS!

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing all designs till none left.
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        u = unprinted_designs.pop()
        print("printing " + u)
        completed_models.append(u)
    
    show_completed_models(completed_models) # calling a function in a function!

def show_completed_models(completed_models):
    """Show all completed models"""
    print("\nthe following designs have been printed:")
    for c in completed_models:
        print(c)

# now run the code!
unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
completed = []

print_models(unprinted, completed) # just takes 1 line to run!!1



## *** Preventing functions from (directly) modifying a list
# use function_name(list_name[:])
# this will create a copy of the list for the function to work on!
# you should pass the original list UNLESS YOU HAVE A SPECIFIC REASON TO PASS A COPY. MORE EFFICIENT FOR A FN TO WORK ON EXISTING LIST TO AVOID USING TIME AND MEMORY TO MAKE A COPY, ESP FOR LARGE LISTS

# lets use the old example
unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
completed = []

print_models(unprinted[:], completed) # copy the list!
print(unprinted) # no change!

print_models(unprinted, completed) # copy the list!
print(unprinted) # now empty!


# 8.9 magicians
list_of_magicians = ['houdini', 'abra', 'kadabra', 'david blain', 'chris angel']
def show_magicians(listm):
    for m in listm:
        print(m)

show_magicians(list_of_magicians)

# 8.10 great magicians
def make_great(listm):
    for m in listm:
        print(m)
        m = 'the great ' + m
        print(m)

def make_great2(listm): ## ***** PASS BY REF VS BY VAL; LOCAL AND GLOBAL VARIABLE
    great_listm = []
    for m in listm:
        gm = 'the great ' + m
        great_listm.append(gm)
    return great_listm

great_listm = make_great2(list_of_magicians)
print(great_listm)
print(list_of_magicians)


def make_great3(listm): ## ***** PASS BY REF VS BY VAL; LOCAL AND GLOBAL VARIABLE
    great_listm = []
    while listm:
        m = listm.pop()
        gm = 'the great ' + m
        great_listm.append(gm)
    return great_listm


great_listm3 = make_great3(list_of_magicians)
print(great_listm3)
print(list_of_magicians) # changed!!




## 8.11 unchanged magicians
## basically v2 lol
def make_great4(listm): ## ***** PASS BY REF VS BY VAL; LOCAL AND GLOBAL VARIABLE
    great_listm = []
    for m in listm:
        gm = 'the great ' + m
        great_listm.append(gm)
    return great_listm

great_listm = make_great4(list_of_magicians)
print(great_listm)
print(list_of_magicians)


### passing an arbitraty number of arguments
'''
sometimes, you might not know how many arguments a function needs to accept. Eg. you don't know how many toppings a customer would want on his pizza. so we use *toppings

this tells python to make TUPLE to store all the incoming values!
'''

def make_pizza(*toppings):
    """Print list of toppings requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

def make_pizza2(*toppings):
    """Summarizes our pizza"""
    print('\nMaking a pizza with:')
    for t in toppings:
        print('- ' + t)


make_pizza2('pepperoni')
make_pizza2('mushroom', 'green peppers', 'extra cheese')


## mixing positional and arbitraty arguments
## ** ARBITRARY ARGUMENTS PLACED LAST IN THE FN DEFINITION

def make_pizza3(size, *toppings): # size first, then *toppings
    """summarizes our pizza"""
    print('\nmaking a ' + str(size)
    + '-inch pizza with:')

    for t in toppings:
        print('- ' + t)

make_pizza3(16, 'pepperoni')
make_pizza3(12, 'mushroom', 'green peppers', 'extra cheese')



## using arbitrary keyword arguments
"""
when you want to accept arbitrary number of arguments, but you don't know what kind of info will be passed to the fn. eg. building user profile: you don't know what kind of info you will receive
"""

def build_profile(first, last, **user_info):
    """Build dict containing everything we know about a user"""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

user_profile = build_profile('albert', 'einstein',
                             location = 'princeton',
                             field = 'physics')

print(user_profile)


## 8.12 sandwiches
def make_sandwich(itemlist):
    """Makes a sandwich and outputs what the ingredients"""
    print('sandwich made has:')
    for i in itemlist:
        print('- ' + i)

s1 = ['bread']
s2 = ['bread', 'lettuce', 'tomato']
s3 = ['bacon', 'lettuce', 'tomato', 'mayo']

make_sandwich(s1)
make_sandwich(s2)
make_sandwich(s3)


## 8.13 user profile

# from pg 153, build_profile
def build_profile2(first, last, **user_info):
    """Build dict containing everything we know about a user"""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

build_profile2('raihan','tarmidi', location = 'new zealand', age = 23)


## 8.14 cars
def make_car(manufac, model_name, **info):
    car = {}
    car['manufac'] = manufac
    car['model name'] = model_name
    for k,v in info.items():
        car[k] = v
    return car

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)