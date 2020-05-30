### INPUT ### 

msg = input("tell me smth, ill repeat it: ") # immediately asks you to type in your input, so lave some whitespace to make it look nice
print(msg)

## write clear prompts
name = input("Please enter your name: ")
print('hi ' + name)


# multiline strings
prompt = "we can personalise ur msg if we know your name."
prompt += "\nWhat's your name? "
name = input(prompt)

print('\nHello ' + name)

## use int() to accept numerical input
age = input("how old are you? ")
age >= 18 # TypeError BECAUSE INPUT() RETURNS A STRING! NOT AN INT!
age = int(age) # convert to number!
age >= 18

height = int(input("how tall are you? "))

if height >= 36:
    print("\nYou are tall enough to ride!")
else:
    print("\n You can ride this when you are older!")


## modulo operator: returns the remainder of a division
4 % 3 # returns 1 as 4/3 = 1 remainder 1

## use raw_input() for python 2.7
## input() in Python 2.7 interprets the user's input as Python code!!!!

## 7.2 restaurant seating
size = int(input("How many people are in your dinner group? "))

if size > 8:
    print("apologies, you have to wait for a table")
else:
    print("please follow me!")



### while loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something and i'll repeat it: "
prompt += "\nEnter 'quit' to end the program \n"

test ='\t test'
test # you will see \t
print(test) # \t disappears to be a tab!!

message = ""
while message != 'quit':
    message = input(prompt)
    print(message) # ** IT LOOKS LIKE THEY REPEAT INPUT TWICE BUT ONE IS YOUR INPUT, THE OTHER IS THE PROGRAM REPEATING YOU!!! ***
    # print(message + " repeated! ") # to see the difference!

## using a flag
# in our previous case, there was only one stopping condition. But what if many events can cause something to end eg. in a GTA mission, you could die, the target could die, the vehicle could explode etc.
# so we should have 1 flag to confirm whether the loop should continue ie. Mission Possible flag.

prompt = "\nTell me something and i'll repeat it: "
prompt += "\nEnter 'quit' to end the program \n"

message = ''

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    elif message == 'shit':
        print("no swearing, goodbye")
        active = False
    else:
        print(message)

## using (break) to exit a loop
p = 'enter city names. (enter "quit" when done): '

while True: # runs forever!
    city = input(p)

    if city == 'quit':
        break
    else:
        print("i'd wanna go " + city + " too")

## using (continue) in a loop
current_number = 0
while current_number < 10:
    current_number+=1
    if current_number % 2 == 0:
        continue # skips even numbers
    print(current_number)

## avoid infinite loops! conditions must be met!
## CTRL-C to interrupt the program! 
x = 1
while x <= 5:
    print(x) # DOESNT END!

## 7.5 movie tix
prompt = 'Hi, how old are you?\n'

flag = True
while flag:
    msg = input(prompt)
    # age = int(msg) # error when you type in 'quit'!!!
    
    if msg == 'quit':
        break
    elif msg == 'cinema_closed':
        print("sorry, cinema is now closed")
        flag = False
    elif int(msg) < 3: # we have to change it here instead!
        print("free!")
    elif int(msg) <= 12:
        print("$10 please")
    else:
        print("$15 please")

## ****** INPUT IS JUST LIKE SCANNER.NEXT() !! THIS MEANS IT DOESNT ACCEPT WHITESPACE!!
## ******* ALSO INT(MSG) CAN'T BE IN FROM AS WHEN YOU INPUT 'QUIT', YOU WILL GET AN ERROR WHEN YOU TRY TO CONVERT IT TO INT!!





### using a while loop with lists dictionaries

## moving items from one list to another

# start with users that need to be verified
# and an empty list to hold confirmed users
unconfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = []

# verify each user until no more unconfirmed users
while unconfirmed_users:
    curr_user = unconfirmed_users.pop()
    print("Verifying user: " + curr_user.title())
    confirmed_users.append(curr_user)

print("the following users have been confirmed")
for u in confirmed_users:
    print(u.title())


## removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'catfish', 'cat']

while 'cat' in pets:
    pets.remove('cat') # does NOT REMOVE 'CATFISH'

print(pets)


## filling a dict with user input
# you can prompt for a lot of input using while loop!

responses = {}

# flag
polling_active = True
while polling_active:
    # ask for name and response
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    # store response in the 'responses' dict
    responses[name] = response

    # find out if anyone else is taking the poll
    repeat = input("Would you like to let another person respond? (y/n) ")
    if repeat.lower() == 'n':
        polling_active = False

# polling ended. show results
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

## ***** IT SEEMS THAT INPUT() DOES ACCEPT WHITE SPACE?? eg. 'mt. fuji'?? ********

## ex 7.8 deli sandwiches
sandwich_orders = ['pastrami', 'reuben', 'grilled cheese', 'blt', 'pastrami', 'grilled chicked', 'pastrami', 'duck pastrami', 'ice cream']

completed_sandwiches = []

while sandwich_orders:
    sw = sandwich_orders.pop()
    print('made your ' + sw + ' sandwich!')
    completed_sandwiches.append(sw)

print('here are the completed sandwiches: ')
for cs in completed_sandwiches:
    print(cs + ' sandwich')


## 7.9 no pastramis!
sandwich_orders = ['pastrami', 'reuben', 'grilled cheese', 'blt', 'pastrami', 'grilled chicked', 'pastrami', 'duck pastrami', 'ice cream']

completed_sandwiches = []

while sandwich_orders:
    sw = sandwich_orders.pop()
    
    if sw == 'pastrami':
        print("Sorry, we have run out of pastrami sandwiches :( ")
        # do not add pastrami to the completed sandwiches!!
    else:
        print('made your ' + sw + ' sandwich!')
        completed_sandwiches.append(sw)

print('here are the completed sandwiches: ')
for cs in completed_sandwiches:
    print(cs + ' sandwich')






