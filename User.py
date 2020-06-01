class User():

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        # wanted to do a boolean. but describe() makes it tedious
        # self.is_boy = is_boy
    
    def describe_user(self):
        print(self.first_name + " " + 
              self.last_name.title() + 
              ' is a ' + str(self.age) + 'year old ' + self.gender)
    
    def greet_user(self):
        print('yo ' + self.first_name)
