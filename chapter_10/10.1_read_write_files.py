### Reading from a file


## this way makes it more accessible from other locations
with open('D:\d Documents\VSCode workspace\python crash course\chapter_10\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)


## this assumes the file is in the same location that you are running the code
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents) # error. because the file is in a different folder than the folder you are working on right now!

## close() can be used but if there is a bug that affects the open(), the close() might never close!!
## better to let Python decide. that's why we use (with)

## the book claims that read() will print the output and an extra blank line. But i don't see it
## in any case, you can use rstrip() to remove the whitespace

filename = 'chapter_10\pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip()) # use rstrip() to remove the extra blank lines



### making a list of lines from a file
'''
when you use (with), the file object returned by open() is ONLY AVAILABLE INSIDE THE (with) BLOCK!!
'''
filename = 'chapter_10\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

# valueError: I/O operation on a CLOSED file
print(file_object.read())

for line in lines:
    print(line.rstrip())




### working with a files contents
pi_string = ''
for line in lines:
    # ** THERE ARE SPACES BW THE LINES TOO! **
    pi_string += line.strip() 

print(pi_string) 
print(len(pi_string))

pi = float(pi_string)






### large files: 1 million digits
'''
the same code above can be used for a file with a million digits. no need to change the code
'''
filename = 'D:\d Documents\VSCode workspace\python crash course\chapter_10\pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_million = ''
for line in lines:
    pi_million += line.strip() 

print(pi_million[:52] + '...') 
print(len(pi_million))

## is your bday in pi
bday = input('enter you bday, ddmmyyyy: ')

if bday in pi_million:
    print('your bday appears in the first million digits of pi')
else:
    print('your bday doesnt appear in the first million digits of pi')

## ex 10.1 learning Python
fn = 'chapter_10\learning_python.txt'

with open(fn) as file_obj:
    lines = file_obj.readlines()

for l in lines:
    print(l.strip())

## 10.2 learning C
msg = 'i like dogs'
msg.replace('dog', 'cat') # changes dog even though 'dogs' is the word in the sentence!1

for l in lines:
    print(l.strip().replace('python', 'C'))

for l in lines: # case Sensitive but can be separated by commas!
    print(l.strip().replace('Python', 'C'))

# for case insensitive replacement, regex is the best way: [https://stackoverflow.com/questions/919056/case-insensitive-replace]








### WRITING TO A FILE

## writing to an empty file
file_name4 = 'chapter_10\programming.txt'

'''
read mode ('r')
write mode ('w')
append mode ('a')
read and write mode ('r+')

Python automatically creates the file if it doesn't exist.
However, be careful if it does, as Python will erase the file to be written over!
'''


# python can only write strings to a txt file
with open(file_name4, 'w') as file_obj4:
    file_obj4.write("I love programming")
# returns number of characters written


with open(file_name4, 'w') as file_obj4:
    file_obj4.write("I love programming\n")
    file_obj4.write("I love creating new games\n")
# /n is considered 1 character


## appending to a file
with open(file_name4, 'a') as file_obj5:
    file_obj5.write("i also like to data mine.\n")
    file_obj5.write("I also love making apps that can run in a browser.\n")




## 10.3 and 10.4 Guest Book

fn104 = 'chapter_10\guest_book.txt'
with open(fn104, 'w') as fo104:
    while True:
        print("Press 'q' to quit.")
        g = input("What's your name?: ")
        
        if g == 'q':
            break
        else:
            fo104.write(g + '\n')
## you can also use 'a' to continue appending
