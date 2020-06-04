
class Employee():

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    
    def give_raise(self, bonus = 5000):
        if bonus == 5000:
            self.salary += 5000
        else:
            self.salary += bonus