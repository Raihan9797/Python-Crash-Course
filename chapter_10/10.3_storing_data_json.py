### STORING DATA

import json

numbers = [2, 3, 5, 7, 11, 13]

# observe how \ and / is used. This is because of \n => newline...
filename = 'D:\d Documents\VSCode workspace\python crash course\chapter_10/numbers.json'

with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

with open(filename) as file_object:
    numbers = json.load(file_object)
print(numbers)


## saving and readiing user-generated data
'''
saving with json is useful when you want to store users information. When the program closes it will be saved!
'''

import json
fn = 'chapter_10/username.json'

# program 1: saving usernames
username = input('you name: ')
with open(fn, 'w') as f_obj:
    json.dump(username, f_obj)
    print("we'll rmb u when u come back " + username)


# program 2: loading usernames
with open(fn) as f_obj:
    username = json.load(f_obj)
    print("Welcome back " + username)


## combining the 2 programs
file_name = 'D:\d Documents\VSCode workspace\python crash course\chapter_10/username.json'
try:
    with open(file_name) as f_o:
        usern = json.load(f_o) 

except FileNotFoundError:
    print("name not found")
    newname = input("What's your name: ")

    with open(file_name, 'w') as f_o:
        json.dump(newname, f_o)
    
    print("We'll rmb you next time " + newname)

else:
    print("welcome back " + usern)




### REFACTORING 
'''
sometimes code we can break code into smaller chunks to make it more easier to read and easier to extend

let's change the above program
'''

# VERSION 1: remember me
def greet_user():
    """ greet the user by name"""
    file_name = 'chapter_10/remember.json'
    try:
        with open(file_name) as f_o:
            usern = json.load(f_o) 
    except FileNotFoundError:
        newname = input("What's your name: ")

        with open(file_name, 'w') as f_o:
            json.dump(newname, f_o)
        
        print("We'll rmb you next time " + newname)
    else:
        print("welcome back " + usern)

greet_user()

'''
greet_user() is doing more than just greeting users; its storing and loading stuff.

let's refactor so it's doing less tasks
'''

def get_stored_username():
    """get stored username if available"""
    file_name = 'chapter_10/remember.json'
    try:
        with open(file_name) as f_o:
            usern = json.load(f_o) 

    except FileNotFoundError:
        return None

    else:
        return usern

get_stored_username()


## VERSION 2
def greet_user2():
    """ greet the user by name"""
    username = get_stored_username()
    if username:
        print("Welcome back " + username)
    else:
        username = input("What's your name?: ")
        file_name = 'chapter_10/remember.json'
        print("we'll rmb you " + username)
        with open(file_name, 'w') as f_o:
            json.dump(username, f_o)

greet_user2()

import json
'''
better, but the else case is still asking for input when you should just be greeting

get_stored_username() is very good because it has a clear purpose. 
** IT ALSO RETURNS A VALUE OR NONE WHICH ALLOWS US TO PERFORM SIMPLE TEST TO SEE IF THERE IS ANY DATA!! ****
'''

def get_new_username():
    username = input("What's your name?: ")
    file_name = 'chapter_10/username.json'
    with open(file_name, 'w') as f_o:
        json.dump(username, f_o)
    
    print("we'll rmb you " + username)
    return username

def greet_user3():
    """ greet the user by name"""
    username = get_stored_username()

    if username:
        print("Welcome back " + username)
    else:
        username = get_new_username()
        print("we'll rmb you " + username)

greet_user3()





## ex 10.1 and 10.2 fav number remembered
def set_fav_num():
    fav = input("What's your fav number?:")
    fn = 'chapter_10/fav_num.json'

    with open(fn, 'w') as fo:
        json.dump(fav, fo)
    return fav

def load_fav_num():
    fn = 'chapter_10/fav_num.json'

    try:
        with open(fn) as fo:
            fav = json.load(fo)
    except FileNotFoundError:
        return None
    else:
        return fav
        

def get_fav_num():
    fav = load_fav_num()

    if fav:
        print("your fav number is " + fav)
    else:
        set_fav_num()

get_fav_num()


## 10.13 verify user

def greet_user_VERIFIED():
    """ greet the user by name"""
    username = get_stored_username()

    if username:
        verified_username = verify_user(username)

    else:
        username = get_new_username()
        print("we'll rmb you " + username)

def verify_user(username):
    verify = input("is this your username?: " + username + " (y/n) ")
    
    if verify == 'n':
        return get_new_username()
    else:
        return username

greet_user_VERIFIED()



def vu(un):
    v = input("are you " + un + "(y/n) ")
    if v == 'n':
        return False
    else:
        return True

def greet_user_verified_final():
    """ greet the user by name"""
    username = get_stored_username()

    if username:
        if vu(username):
            print("Welcome back " + username)
        else:
            newname = get_new_username()
    else:
        username = get_new_username()

greet_user3()
