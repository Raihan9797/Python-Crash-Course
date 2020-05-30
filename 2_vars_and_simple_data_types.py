print("hello world")

# 2.1 variables
message = "hello again!"
print(message)

# recc naming of vars
# cannot start with number. no spaces. no using keywords
# should be short, descriptive
# student_name > s_n, name_length > length_of_persons_name


## 2.2 Strings
'This is a string'
"This is also a string"

## 2.2.1 basic string functions
name = "ada lovelace"
a = name
print(name.title())
print(name.lower())
print(name.upper())
print(a)

first_name = "Peter"
last_name = "Parker"
full_name = first_name + " " + last_name
print('hello ' + full_name.title() + "!")

## 2.2.2 whitespace: tabs and newlines
print("python")
print("\tpython")
print("Languages:\npython\n\tC\nJava")

## 2.2.3 stripping whitespace
fav_lang = '   python   '
print(fav_lang.rstrip())
print(fav_lang.lstrip())
print(fav_lang.strip())


## 2.2.4 string errors
string_right = "There's nothing wrong here"
string_wrong = 'There's something wrong here
# make sure to use the right apostrophe

### exercises

# 2-3
name = 'fabian'
print("hello "+ name + " how are you?")

# 2-4
name.lower()
name.upper()
name.title()

# 2-5
quote = '"Stay Hard".'
print("David goggins once said, " + quote)

# 2-6
person = "David Goggins"
truth = person + " once said, " + quote
print(truth)

# 2-7
big_name = ' \t\nArun\n\t'
print(big_name.rstrip())
print(big_name.lstrip())
print(big_name.strip())


### 2.3 Numbers
# +, -, *, /, ** for exponent
1+2
3/2
2*4
2**3

# floats: any number with a decimal point in Python
0.2 + 0.1 # can sometimes give weird rounding off errors
0.1 + 0.1

# converting int to string is NOT implicit
age = 23
msg = "Happy " + str(age) + "rd Birthday!"
print(msg)