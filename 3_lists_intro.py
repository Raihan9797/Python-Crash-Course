### lists: a collection of items in a particular order. Can be of different types


## accessing positions of a list
bicycles = ['trek', 'connondale', 'redline', 'specialized']
print(bicycles) # prints out like the list you made!

print(bicycles[0])
print(bicycles[-0]) # it may be from the back, but 0 from the back is the first element!


print(bicycles[-1].upper())
msg = 'my first bike was a ' + bicycles[0].title() + "."
print(msg)


## changing adding and removing elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# adding elements
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
motorcycles

# insert elements
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
motorcycles

# removing using deleting elements
del motorcycles[0] # delete ducati
motorcycles

# removing using pop()
# it deletes the element from the LAST ITEM of the list and returns the deleted element for you to use
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.pop()

# actly, you can pop() from any pos lol
motorcycles = ['honda', 'yamaha', 'suzuki']
h = motorcycles.pop(0) # pops first element
print(h)


# removing via value
# remove() deletes the FIRST OCCURRENCE of the val in the list. DUPLICATES WON'T BE DELETED
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_ex = 'ducati'
motorcycles.remove(too_ex)
print('\nA ' + too_ex + " is too expensive for me")


### exercises
# 3.4 guest list
guest_list = ['David Goggins', 'Marcus Aurelius', 'Seneca the Younger']
invite0 = "Would you go on a run with me " + guest_list[0] + '?'
invite2 = "Would you go on a run with me " + guest_list[2] + '?'
print(invite0)

# 3.5 changies g list
print(guest_list)
ma = "Marcus Aurelius"
cmi = ma + " can't make it; he's feeling sick"
guest_list.remove(ma)
new_guest = 'Mike Tyson'
guest_list.append(new_guest)
print(guest_list)

# 3.6 more guest
guest_list.insert(0, 'Big Boss')
print(guest_list)
guest_list.insert(1, 'Naked Snake')
print(guest_list)
guest_list.append('Old Snake')
print(guest_list)


# 3.7 shrinking guest list
sorry = 'Sorry '
bye = sorry + guest_list.pop()
print(bye)
bye = sorry + guest_list.pop()
print(bye)

print(guest_list)
del guest_list[0]
guest_list.remove('Naked Snake')
print(guest_list)


## organising a list: sort() vs sorted()
# WHEN SORTING, CAPS DOES MAKE A DIFFERENCE!
cars1 = ['bmw', 'aud1', 'toyota', 'subaru']
cars.sort(reverse=True) # this is permanent ie YOU CAN'T CHANGE BACK TO YOUR OLD ORDER
# unless you just initialise the list again!
print(cars)

cars2 = ['bmw', 'aud1', 'toyota', 'subaru']
print(cars2)
print(sorted(cars2)) # temporarily sorts
print(cars2)

# len() of a list
len(cars2)


## errors: IndexError: list index out of range
cars2[10]