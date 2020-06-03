## Exceptions
print(5/0) # Exception object is created when you make an error
# if an exception object is created, 

try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")


## using exceptions to prevent crashes

print("gimme 2 numbers to divide")
print("press 'q' to quit")

while True:
    fn = input("First number: ")
    if fn == 'q':
        break

    sn = input("second number: ")
    if sn == 'q':
        break

    try:
        ans = int(fn) / int(sn)
    except ZeroDivisionError:
        '''prevents the program from crashing'''
        print("bro you cant divide by 0")
    else:
        print(ans)


## Handling FileNotFoundError Exception
fn = 'alice.txt'

with open(fn) as fo:
    contents = fo.read() # filenotfounderror


try:
    with open(fn) as fo:
        contents = fo.read()
except FileNotFoundError:
    print("sry file: " + fn + " not found")


## Analyzing Text
alice2 = 'D:\d Documents\VSCode workspace\python crash course\chapter_10/alice.txt'

try:
    with open(alice2) as fo:
        contents = fo.read()
except FileNotFoundError:
    print("sry file: " + alice2 + " not found")

else:
    # count the number of words in the file
    '''split by space and stores the words in a list'''
    words = contents.split() 
    num_words = len(words)
    print('word count: ' + str(num_words))
    

## working with multiple files
def count_words(filename):
    try:
        with open(filename) as fo:
            contents = fo.read()
    except FileNotFoundError:
        print("sry file: " + filename + " not found")

    else:
        # count the number of words in the file
        '''split by space and stores the words in a list'''
        words = contents.split() 
        num_words = len(words)
        print('word count: ' + str(num_words))

count_words(alice2)

sidd = 'D:\d Documents\VSCode workspace\python crash course\chapter_10\siddartha.txt'
moby = 'D:\d Documents\VSCode workspace\python crash course\chapter_10\moby_dick.txt'
lilw = 'D:\d Documents\VSCode workspace\python crash course\chapter_10\little_women.txt'

filenames = [alice2, sidd, moby, lilw]

for fn in filenames:
    count_words(fn)




## Failing Silently
'''
sometimes, you don't want to show them the error.
So we can just suppress it by using (pass)
'''

def count_words2(filename):
    try:
        with open(filename) as fo:
            contents = fo.read()
    except FileNotFoundError:

        pass # ie ignore the error!

    else:
        # count the number of words in the file
        '''split by space and stores the words in a list'''
        words = contents.split() 
        num_words = len(words)
        print('word count: ' + str(num_words))

for fn in filenames:
    count_words2(fn) # siddartha error not shown!



## 10.6 and 10.7 addition calculator
print('-------- add 2 numbers ------')
print('press q to quit')

while True:
    fn = input('first number: ')
    if fn == 'q':
        break

    sn = input('second number: ')
    if sn == 'q':
        break

    try:
        ans = int(fn) + int(sn)
    except ValueError:
        print('numbers only!')
    else:
        print(ans)


## 10.8 andd 10.9 (Silent) Cats and Dogs
# you can move it around to get the filenotfounderror

c = 'D:\d Documents\VSCode workspace\python crash course\chapter_10\cats.txt'
d = 'D:\d Documents\VSCode workspace\python crash course\chapter_10\dogs.txt'


files = [c, d]
for f in files:
    try:
        with open(f) as fo:
            names = fo.read()
    except FileNotFoundError:
        print("sry we can't find the file")
        # pass # or you can just suppress it!!
    else:
        print(names)


## 10.10 common words
def count_the(filename):
    try:
        with open(filename) as file_object:
            text = file_object.read()
    except FileNotFoundError:
        print("sorry we can't find your file")
    else:
        num_the = text.lower().count('the')
        print("'the' count: " + str(num_the))
    

count_the("D:\d Documents\VSCode workspace\python crash course\chapter_10\siddhartha.txt")
