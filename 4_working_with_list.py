## looping through an entire list
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print("that was a great trick, " + magician.title()+ "!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
# press enter in the VSCode terminal to run the code!

# doing something after a for loop
for magician in magicians:
    print("that was a great trick, " + magician.title()+ "!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print('Thanks everyone! What a great show!')

## avoiding inentation errors
# indent properly! when you use a for loop!
# don't forget the colon (:)
# you can use newlines \n too!

# don't indent unnecessarily! 
msg = 'hi'
    print(msg)
# indenting after for loop
for magician in magicians:
    print(magician + "inside loop 1")
    print(magician + "inside loop 2")

    print(magician + "outside loop or not?") #  NOT because of indenting!


## making numerical list
# using range()
for value in range(1,5):
    print (value) # only prints to 4

for v in range(2, 11, 2): # starts at 2, ends at 10 and keeps incrementing by 2
    print(v)


nums = list(range(1,6))
print(nums)


even_nums = list(range(2,11,2))
print(even_nums)

squares = []
for value in range(1,11):
    square = value**2
    # squares.append(value**2) ## more concise version
    squares.append(square)

print(squares)

# simple stats
digits = list(range(1,10))
digits.append(0)
print(digits)

min(digits) #max(), sum() available!



### IMPORTANT CONCEPT TO TAKE NOTE OF!
x = []
print(x)
y = x.append(1)
print(y) # returns None because append() is a function that does not return anything!!!

## list comprehension! IMPORTANT!!! 
squaresv2 = [value**2 for value in range(1,11)]
print(squaresv2) # quickly make a list in a line of code!!

## 4.3 count to twenty
for v in range(1,21):
    print(v)


# 4.4 count to 1M!
# PRESS CTRL C TO STOP THE COMMAND!
for v in range(1, 1000001):
    print(v)

# 4.5
million = list(range(1, 1000001))
min(million)
max(million)
sum(million)

# 4.6 odd numbers
odds = list(range(1, 21, 2))
for o in odds:
    print(o)

# 4.7 threes
threes = list(range(3, 31, 3))
print(threes)

# 4.8 cubes
cubes = []
for c in range(1,11):
    c3 = c**3
    cubes.append(c3)
cubes # also returns the list, but better to use print()
print(cubes)

# 4.8 list comprehension
cubesv2 = [c**3 for c in range(1,11)]
cubesv2 # nice






## working with part of a list
# slicing a list
players = ['charles', 'martin', 'michael', 'florence', 'eli']
print(players[0:3]) # prints pos 0, 1, 2!!!
print(players[:3]) # same!!

print(players[2:]) # starts from 2 to the end!

print(players[-2:]) # prints from the last to the 2nd last player!
print(players[-2]) # this also means you can print the 2nd last player specifically!



# looping throught a slice
players = ['charles', 'martin', 'michael', 'florence', 'eli']
print("here are the last three players")
for player in players[-3:]:
    print(player.title())
# IT PRINTS FROM THIRD LAST TO ACTUAL LAST IE DOES NOT REVERSE THE LIST!

# copying a list. you like a list of foods. For now, your friend also likes the same foods
my_foods = ['pizza', 'falafel', 'carrot cake']

# friend_foods = my_foods # THIS IS WRONG; IT POINTS TO THE SAME LIST!

friend_foods = my_foods[:] # THIS COPIES THE ENTIRE LIST
print(my_foods)
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods) # as you can see, the lists are now different

x = ['one', 'two', 'three']
y = x[:]
x == y # IT SEEMS LIKE EQUALITY HERE IS CHECKING THE VALUES, NOT WHETHER IT'S TRULY THE SAME BIT!


# 4.10 slicing
sentence = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
first3 = sentence[:3]
mid3 = sentence[3:6]
last3 = sentence[6:10]

first3
mid3
last3





## tuples
# used when you want to ceate a list that CANNOT CHANGE IE IMMUTABLE LIST == TUPLE

# defining a tuple
dimensions = (200, 50)
print(dimensions)

dimensions[0] = 250 # TypeError: tuple object does not support item assignment

for d in dimensions:
    print(d)


# writing over a tuple: cant assign a new values INSIDE the tuple BUT WE CAN REDEFINE THE ENTIRE TUPLE
dimensions = (200, 50)
print("original dim: ")
for d in dimensions:
    print(d)

dimensions = (420, 96)
print("new dim: ")
for d in dimensions:
    print(d)



## styling codes
# Python Enhancement Proposal

# indentation: tab should be 4 spaces

# line length: 79 chars, but ppl use 99 too

# comments: 72 chars per line

# blank lines: to group parts of your program.

# more guildelines: https://python.org/dev/peps/pep-0008/