alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# print VALUES by selecting the KEYS
print(alien_0['color'])
print(alien_0['points'])

# YOU CAN'T PRINT KEYS BY SELECTING THE VALUE!
print(alien_0['green'])

new_points = alien_0['points']
print('you earned ' + str(new_points) + ' points!')

# adding new key value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

x = {}
x['key'] = 'val'

# modifying values
alien_0 = {'color': 'green'} # redefine dict
print('alien color is ' + alien_0['color'])

alien_0['color'] = 'yellow'
print('alien color is NOW ' + alien_0['color'])

# more practical example !!
alien_0 = {
    'x_position':0, 
    'y_position':25,
    'speed':'medium'
}

print('original x pos: ' + str(alien_0['x_position']))

# move alien to the right
# determine how far to move based on speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# new pos = old pos + increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('new x pos is ' + str(alien_0['x_position']))


# removing key val pairs
alien_0 = {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0)

## dictionaries of similar items
fav_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
print("sarah's fav lang is " + fav_languages['sarah'])

## exercises skipped


### looping through all k v pairs
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}
user_0.items() # returns a list of k v pairs!! so...

for k,v in user_0.items():
    print('\nKey: ' + k)
    print('Value: ' + v) # KEY VAL PAIRS ARE NOT RETURNED IN ORDER!!

fav_languages2 = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
for name, language in fav_languages.items():
    print(name.title() + "'s fav language is " + language)

## looping through all the keys in a dict
# ** LOOPING THROUGH KEYS IS ACTUALLY THE DEFAULT BEHAVIOR WHEN LOOPING THROUGH A DICTIONARY!! **
fav_languages2.keys()

for name in fav_languages2.keys():
    print(name.title())

# same as:
for name in fav_languages2:
    print(name.title())

## looping through a dict keys in order: sorted()
for name in sorted(fav_languages.keys()):
    print(name.title() + ', thank you for taking the poll')

## looping through all VALUES in a dict; and removing duplicates
set(fav_languages2.values())

# exercise skipped


### nesting

## a LIST of DICTIONARIES
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]

# not efficient if we had to make more alines so...
aliens = []

# make 30 aliens.
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

# for the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('.......')

# show how many aliens have been created
print('Total # of aliens: ' + str(len(aliens)))

# now we can change them in bulk
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10 

for alien in aliens[:5]:
    print(alien)



## a LIST IN A DICTIONARY
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
}

# summarize the order.
print('you ordered a ' + pizza['crust'] + '-crust pizza' + " with the following toppings:")
for topping in pizza['toppings']:
    print('\t' + topping)


fav_languages3 = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in fav_languages3.items():
    print("\n" + name.title() + "'s fav languages are:")
    for l in languages:
        print("\t" + l.title())

# don't nest too much!


## a DICT IN A DICT
users = {
    'aeinstein': {
        'first':'albert',
        'last':'einstein',
        'location':'princeton', # you can have this comma! *******
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }, # you can also have this comma here!!!! ********
}

for username, user_info in users.items():
    print("\n Username: " + username)

    # compiling the input
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    # printing the output
    print("\tfull name: " + full_name.title())
    print("\tlocation: " + location.title())



## exercises
# 6.7 people
ppl = []
p1 = {
    'f' : 'fabian',
    'l' : 'tan',
    'g' : 'boy'
}
ppl.append(p1)
p2 = {
    'f' : 'darrel',
    'l' : 'peng',
    'g' : 'boy'
}
ppl.append(p2)

for p in ppl:
    full_name = p['f'] + " " + p['l']
    full_name + " is a " + p['g']

# 6.9 fav places
fav_places = {
    'fabian': ['tokyo', 'taiwan', 'kyoto'],
    'darrel': ['taiwan', 'hong kong', 'singapore']
}
fav_places['raihan'] = ['krabi', 'kyoto', 'osaka']

for name, places in fav_places.items(): # don't forget items()
    print("\n" + name.title() + "'s favourite places are: ")
    for place in places:
        print("\t" + place)

# 6.10 cities
cities = {
    'tokyo': {
        'country':'japan',
        'population': 9273000,
        'fact': 'tokyo has the most top rated restaurants in the world'
    },
    'texas': {
        'country':'USA',
        'population': 29000000,
        'fact': "texas produces 7% of the world's cotton"
    },
    'taipei': {
        'country':'taiwan',
        'population': 23780000,
        'fact': "Beethoven's 'Fur Elise' is played when garbage trucks are coming so you have to go out and pass them the garbage!"
    },
}

for city, city_info in cities.items():
    print("\n" + city + " stats: ")

    print("coutry: " + city_info['country'])
    print("population: " + str(city_info['population']))
    print("fact: " + city_info['fact'])







