# simple example
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

## conditional tests
# basically, if and else are based on a conditional test.

# check equality
car = 'bmw'
car == 'bmw'
car == 'audi'

# check inequality
car = 'Audi'
car != 'BMW'
car != 'audi' # EQUALITY IS CASE SENSITIVE
car != 'Audi'

# numerical comparison
guess = 17  # try a random number
my_age = 23

if guess < my_age:
    print('too young')
elif guess > my_age:
    print('too old')
else:
    print('damn u smart!')


# using (and) and (or)
a1 = 21
a2 = 27
if a1 >= 21 and a2 >= 21:
    print("both are above 21")

a3 = 12
if a1 >= 21 or a3 >= 21:
    print("one of you is 21 and above!")



## checking values in a list using (in)
requested_toppings = ['mushroom', 'onions', 'pineapple']
'mushroom' in requested_toppings
'pepperoni' in requested_toppings
'anchovies' not in requested_toppings


banned_users = ['andrew', 'ryan', 'carolina']
user = 'marie'

if user not in banned_users:
    print("welcome " + user.title())

# boolean expressions
# usually used to keep track of certain conditions
game_active = True
isBoy = False 



## if statements

# the basic structure is shown below
# if conditional_test:
#     do_something

age = 19
if age >= 18:
    print('you are old enough to vote!')
    print('you should register')


# if else chain
age = 17
if age >= 18:
    print('you are old enough to vote!')
    print('you should register')
else:
    print('you are too young!')


# if-elif-else chain
# mrt admission:
# 1. kids below 5yo get to ride for free
# 2. adults pay 2$
# 3. seniors pay 1$

# LOOK AT THE REPETITION. THIS IS NOT EFFICIENT CODE
age = 7
if age <= 5:
    print('admission price: $0')
if age >= 5:
    print('admission price: $2')
else:
    print('admission price: $1')


age = 7
if age <= 5:
    price = 0
if age >= 5:
    price = 2
else:
    price = 1
print('admission price: $' + str(price))

# PYTHON DOESNT REQUIRE (ELSE) STATEMENT!
# (else) is a catchall statement. using this might make it hard to understand which condition it didn't meet. If you are unsure. use elif instead to understand what condition your value is meeting
age = 7
if age <= 5:
    price = 0
if age >= 5:
    price = 2
else:
    price = 1
print('admission price: $' + str(price))



# *** testing multiple conditions: USE MULTIPLE (IF)s NOT IF-ELIF-ELSE! ****
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('adding mushrooms.')

if 'pepperoni' in requested_toppings:
    print('adding pepperoni.')

if 'extra cheese' in requested_toppings:
    print('adding extra cheese.')


# using if-elif-else will only result in 1 condition running!!!
if 'mushrooms' in requested_toppings:
    print('adding mushrooms.')

elif 'pepperoni' in requested_toppings:
    print('adding pepperoni.')

elif 'extra cheese' in requested_toppings:
    print('adding extra cheese.') # only mushrooms will be added!!

# 5.3 alien colours 1
alien_color = 'red'
if alien_color == 'green':
    points = 5

print('you earned ' + str(points) + " points") # error cos you didn't reach any conditions!

# 5.4 alien colours 2
if alien_color == 'green':
    points = 5
else:
    points = 10 

print('you earned ' + str(points) + " points")


# 5.4 alien colours 3
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15 

print('you earned ' + str(points) + " points")

# 5.5 stages of life
age = 20 

if age < 2:
    print('baby')
elif age <= 4: 
    # =< DOESNT WORK!!! 
    # tecnically, this is correct, cos we are checking those who are below 2 first before we look at those below 4 and so on...
    print('toddler')
elif 4 <=  age < 13:
    # no need for (and), we can chain inequalities like in math!
    print('kid')
elif 13 <= age and age < 20:
    # eg using (and)
    print('teen')
elif 20 <= age and age < 65:
    print('adult')
else:
    print('elder')



## Using If statements with Lists

# checking for special items in lists
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for r_t in requested_toppings: # item which requires a different output
    if requested_toppings == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print('Adding ' + requested_toppings + '.')


# checking a list is NOT empty
cars3 = []
if cars3: # checks if there are even cars in the list!!
    # run the for loop
    for car in cars3:
        print("you have a " + car.title())
    print('That is all the cars in your garage')

else: # NO CARS
    print("Are you sure this is your garage??")


# using multiple lists: nested for loops
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for r_t in requested_toppings:
    if r_t in available_toppings:
        print('Adding ' + r_t + '.')
    else:
        print("Sorry, we don't have " + r_t + '.')
print("Pizza made!!")

# 5.8
users = ['alice', 'charlie', 'david', 'bob', 'admin', 'thanos']

for u in users:
    if u == 'admin':
        print('Hi admin. Would you like to see a report?')
    else:
        print('Hello, '+ u)

# 5.9 no users
users = []
if users:
    for u in users:
        if u == 'admin':
            print('Hi admin. Would you like to see a report?')
        else:
            print('Hello, '+ u)
else:
    print('We need to get some users man')

# 5.10 check usernames
# *** WE SHOULD MAKE SURE THAT OUR CURRENT_USERS MUST BE LOWERCASED FOR US TO BE ABLE TO COMPARE CASE INSENSITIVELY!
current_users = ['Alice', 'CHARLIE', 'dAvId', 'bob', 'admin', 'thanos']

current_users_lower = [c.lower() for c in current_users]
new_users = ['dave', 'Charlie', 'Alice', 'Thanos', 'DAVID']

for n in new_users:
    if n.lower() in current_users_lower:
        print('sorry this name is taken')
    else:
        print('welcome '+ n)

## styling if statements
if age < 4: # good example

if age<4: # bad example

