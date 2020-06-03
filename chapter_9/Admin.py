from User import User

class Admin(User):

    def __init__(self, first_name, last_name, age, gender, privileges):
        super().__init__(first_name,last_name,age,gender)
        self.privileges = Privilege(privileges) 


class Privilege():
    def __init__(self, priviliges):
        self.privileges = priviliges
    
    def show_priviliges(self):
        for p in self.privileges:
            print(p)